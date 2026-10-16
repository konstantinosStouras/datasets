import {execFileSync} from 'node:child_process';
import {appendFileSync} from 'node:fs';
import {parseCatalog} from './catalog.mjs';

const repo = 'konstantinosStouras/datasets', upstream = 'toddrjones/datasets';
const initial = '7264eb6f6cae52b2a92fc3c0eee4b3dd2d0396a1';
const stateBranch = 'dataset-sync-state', statePath = '.github/upstream-sync-state.json';
const git = (...args) => execFileSync('git', args, {encoding:'utf8', stdio:['ignore','pipe','pipe']}).trim();
async function api(path, method = 'GET', body) {
  const response = await fetch(`https://api.github.com/repos/${repo}/${path}`, {method, headers:{Authorization:`Bearer ${process.env.GH_TOKEN}`, Accept:'application/vnd.github+json', 'X-GitHub-Api-Version':'2022-11-28'}, body:body ? JSON.stringify(body) : undefined});
  if (response.status === 404 && method === 'GET') return null;
  if (!response.ok) throw new Error(`GitHub ${method} ${path}: ${response.status} ${await response.text()}`);
  return response.status === 204 ? null : response.json();
}
async function issueOnce(marker, title, body) {
  for (let page = 1; ; page++) {
    const issues = await api(`issues?state=all&per_page=100&page=${page}`);
    const found = issues.find(i => !i.pull_request && i.body?.includes(marker));
    if (found) return found.html_url;
    if (issues.length < 100) break;
  }
  return (await api('issues','POST',{title,body:`${marker}\n\n@konstantinosStouras\n\n${body}`})).html_url;
}
function newEntries(before, after) {
  const prior = parseCatalog(before);
  const names = new Set(prior.map(e => e.id));
  const urls = new Set(prior.flatMap(e => [e.url, ...e.links.map(l => l.url)]).filter(Boolean));
  return parseCatalog(after).filter(e => !names.has(e.id) && (!e.url || !urls.has(e.url)));
}
git('config','user.name','github-actions[bot]');
git('config','user.email','41898282+github-actions[bot]@users.noreply.github.com');
git('fetch','origin','main');
git('remote','add','upstream',`https://github.com/${upstream}.git`);
git('fetch','upstream','main');
const head = git('rev-parse','upstream/main');
const stored = await api(`contents/${statePath}?ref=${stateBranch}`);
const state = stored ? JSON.parse(Buffer.from(stored.content,'base64').toString()) : {lastInspected:initial, lastSynced:initial};
const before = git('show',`${state.lastInspected}:README.md`);
const after = git('show',`${head}:README.md`);
const additions = newEntries(before, after);
let outcome = 'The fork is up to date.', conflict = false;
try {
  git('merge','--no-edit','upstream/main');
} catch (error) {
  try { git('merge','--abort'); } catch {}
  conflict = true;
  outcome = 'Automatic merging needs attention. Your additions are preserved; resolve the upstream merge manually.';
  console.error(outcome, error.message);
}
if (!conflict) {
  // A normal push rejects concurrent user changes; it never overwrites them.
  git('push','origin','HEAD:main');
  git('merge-base','--is-ancestor',head,'HEAD');
  state.lastSynced = head;
}
const compare = `https://github.com/${upstream}/compare/${state.lastInspected}...${head}`;
if (additions.length) {
  const rows = additions.map(e => `- [${e.title.replace(/[\[\]@]/g,'')}](${e.url || `https://github.com/${upstream}`}) — ${e.topic}${e.description ? ': '+e.description.replace(/@/g,'') : ''}`).join('\n');
  const url = await issueOnce(`<!-- dataset-additions:${head} -->`, `New datasets: ${additions.length} addition${additions.length === 1 ? '' : 's'} (${head.slice(0,7)})`, `${rows}\n\n[See the source changes](${compare}).\n\n${outcome}\n\n[Browse the datasets](https://www.stouras.com/datasets/).`);
  console.log('New dataset alert:',url);
}
if (conflict) await issueOnce(`<!-- dataset-conflict:${head} -->`,'Dataset sync needs attention',`${outcome}\n\n[Review the upstream changes](${compare}).`);
if (process.env.TEST_NOTIFICATION === 'true') {
  await issueOnce('<!-- dataset-sync-setup:v1 -->','Dataset alerts are ready',`This is the one-time setup check for your dataset alerts. GitHub now checks the original repository hourly and preserves your own additions when syncing. Future alerts are sent only for new dataset entries or merge conflicts.\n\n${outcome}\n\n[Browse the datasets](https://www.stouras.com/datasets/).`);
}
state.lastInspected = head;
// A monthly state commit also keeps this public repository active, preventing
// GitHub's 60-day inactivity timeout for scheduled workflows.
if (!stored || head !== JSON.parse(Buffer.from(stored.content,'base64').toString()).lastInspected || state.lastSynced !== JSON.parse(Buffer.from(stored.content,'base64').toString()).lastSynced || Date.now() - Date.parse(state.savedAt || 0) > 28*86400000) {
  if (!stored) {
    const ref = await api(`git/ref/heads/${stateBranch}`);
    if (!ref) await api('git/refs','POST',{ref:`refs/heads/${stateBranch}`,sha:git('rev-parse','HEAD')});
  }
  state.savedAt = new Date().toISOString();
  await api(`contents/${statePath}`,'PUT',{branch:stateBranch,message:'Maintain upstream sync checkpoint',content:Buffer.from(JSON.stringify(state,null,2)+'\n').toString('base64'),...(stored ? {sha:stored.sha} : {})});
}
const summary = `${outcome}\n\nNew dataset entries: ${additions.length}. Upstream: ${head}.`;
console.log(summary);
if (process.env.GITHUB_STEP_SUMMARY) appendFileSync(process.env.GITHUB_STEP_SUMMARY,summary+'\n');
if (conflict) process.exitCode = 1;
