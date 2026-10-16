export const plain = s => s.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '$1').replace(/[*`]/g, '').trim();
export function parseCatalog(markdown) {
  markdown = markdown.replace(/<!--[\s\S]*?-->/g, '');
  const entries = []; let topic = '', current;
  for (const line of markdown.split(/\r?\n/)) {
    const heading = line.match(/^###\s+(.+)/);
    if (heading) { topic = heading[1].trim(); current = null; continue; }
    if (!topic || topic === 'Contents' || /^---/.test(line)) continue;
    const bullet = line.match(/^(\s*)[-*]\s+(.+)/);
    if (!bullet) continue;
    if (bullet[1].length === 0) {
      current = {topic, title: '', description: '', details: [], links: []};
      const lead = bullet[2].match(/^\[([^\]]+)\]\((https?:\/\/[^)]+)\)(.*)/);
      if (lead) { current.title = plain(lead[1]); current.url = lead[2]; current.description = plain(lead[3].replace(/^\s*[-–—]\s*/, '')); }
      else { const split = bullet[2].split(/\s[-–—]\s/); current.title = plain(split.shift()); current.description = plain(split.join(' — ')); }
      if (/(see above|see [a-z]+ above)/i.test(bullet[2]) && !lead) { current = null; continue; }
      if (!lead && current.title.length > 100) {
        const embedded = bullet[2].match(/\[([^\]]+)\]\((https?:\/\/[^)]+)\)/);
        if (embedded) { current.title = plain(embedded[1]); current.url = embedded[2]; current.description = plain(bullet[2]); }
      }
      entries.push(current);
    } else if (current) current.details.push(bullet[2]);
  }
  for (const entry of entries) {
    const text = [entry.description, ...entry.details].join(' ');
    entry.links = [...text.matchAll(/\[([^\]]+)\]\((https?:\/\/[^)]+)\)/g)].map(m => ({title:plain(m[1]), url:m[2]}));
    if (!entry.url) entry.url = entry.links[0]?.url || '';
    entry.access = /requires?|agreement|permission|not available|not publicly|rest requires/i.test(text) ? 'Agreement or mixed' : /access:\s*(public|free)|publicly available|free (to download|download)|access: public/i.test(text) ? 'Public' : 'Not specified';
    entry.years = (plain(text).match(/Years(?: covered)?:\s*([^.;]+)/i)?.[1] || '').trim();
    entry.search = plain([entry.title, entry.topic, text].join(' ')).toLowerCase();
    entry.id = entry.title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    entry.geography = /worldwide|global|countries|international|multinational/i.test(entry.search) ? 'International' : /england|wales|united kingdom/i.test(entry.search) ? 'United Kingdom' : /\b(us|u\.s\.|american|census|ssa|cdc|nchs|nber|nfl|nba|mlb|congress|texas|chicago|new york|california|seattle|los angeles)\b/i.test(entry.search) ? 'United States' : 'Other / not specified';
  }
  return entries;
}
export function filterEntries(entries, filters, saved = []) {
  const terms = (filters.q || '').toLowerCase().split(/\s+/).filter(Boolean);
  return entries.filter(e => terms.every(t => e.search.includes(t)) && (!filters.topic || e.topic === filters.topic) && (!filters.access || e.access === filters.access) && (!filters.geo || e.geography === filters.geo) && (filters.view !== 'saved' || saved.includes(e.id)));
}
