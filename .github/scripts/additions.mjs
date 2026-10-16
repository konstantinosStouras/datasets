import {parseCatalog} from './catalog.mjs';
export function newEntries(before, after) {
  const prior=parseCatalog(before), next=parseCatalog(after);
  const names=new Set(prior.map(e=>e.id));
  const urls=new Set(prior.flatMap(e=>[e.url,...e.links.map(l=>l.url)]).filter(Boolean));
  const additions=next.filter(e=>!names.has(e.id)&&(!e.url||!urls.has(e.url)));
  const newParents=new Set(additions.map(e=>e.id));
  for(const entry of next){
    if(newParents.has(entry.id))continue;
    for(const line of entry.details){
      const lead=line.match(/^\[([^\]]+)\]\((https?:\/\/[^)]+)\)(.*)/);
      if(lead&&!urls.has(lead[2])){additions.push({title:lead[1],url:lead[2],topic:entry.topic,description:lead[3].replace(/^\s*[-–—]\s*/,'')});urls.add(lead[2]);}
    }
  }
  return additions;
}
