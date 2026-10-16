# HISTORICAL REFERENCE: see README.md before running.
import json,re
from pathlib import Path
root=Path('C:/Users/LENOVO/Dropbox/Others/GitHub/konstantinosStouras.github.io')
focus=re.compile(r'new product|innovat|entrepreneur|technology management|patent|start.?up|crowdfund',re.I)
sharing=re.compile(r'data (?:and code |files |sets? )?(?:are |is )?available|replication|publicly available|dataverse|zenodo|osf.io|github|open data',re.I)
rows=[];seen=set();counts={}
for f in [root/'lit/data'/('papers-'+j+'.json') for j in ['ms','msom','pom']]+list((root/'lit/data-ft50').glob('papers-*.json')):
 for p in json.loads(f.read_text(encoding='utf-8')):
  doi=p.get('DOI','').lower();year=int(p.get('Year','0') or 0)
  if doi in seen or not 2006<=year<=2026:continue
  seen.add(doi);title=p.get('Title','');abstract=p.get('Abstract','')
  if not focus.search(title+' '+abstract):continue
  counts[p.get('Journal',f.stem)]=counts.get(p.get('Journal',f.stem),0)+1
  cues=[m.group(0) for m in sharing.finditer(abstract)]
  if cues:
   match=sharing.search(abstract)
   rows.append({'title':title,'doi':doi,'journal':p.get('Journal'),'year':year,'cues':cues,'evidence':abstract[max(0,match.start()-70):match.end()+220]})
Path(__file__).with_name('paper-data-candidates.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'unique_records_in_year_window':len(seen),'topic_candidates':sum(counts.values()),'sharing_cue_candidates':len(rows),'journal_counts':counts,'first_candidates':rows[:18]},ensure_ascii=False,indent=2))
