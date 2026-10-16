# HISTORICAL REFERENCE: see README.md before running.
import json,csv,re
from pathlib import Path
out=Path(__file__).parent
repo=Path('C:/Users/LENOVO/Dropbox/Others/GitHub/datasets')
rows=json.loads((out/'paper-data-candidates.json').read_text(encoding='utf-8'))
catalog=json.loads((repo/'research-additions.json').read_text(encoding='utf-8'))
verified=catalog['papers']
focus=[x for x in rows if re.search('new product|innovat|entrepreneur|technology|patent|start.?up|crowdfund',x['title'],re.I)]
all_rows=list(rows)
for doi in ['10.1287/mnsc.2023.00282','10.1287/msom.2017.0692','10.1287/msom.2022.0359']:
 p=verified[doi];row={'title':p['title'],'journal':p['journal'],'year':p['year'],'doi':p['url'],'cues':['Manually verified repository and data file']}
 if not any(doi in x['doi'] for x in focus):focus.append(row)
 if not any(doi in x['doi'] for x in all_rows):all_rows.append(row)
order={'Management Science':0,'Manufacturing & Service Operations Management':1,'Production and Operations Management':2}
def write(path,items):
 with path.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.writer(f);w.writerow(['Paper title','Journal','Year in database','Paper DOI','Availability clue','Review status'])
  for x in sorted(items,key=lambda x:(order.get(x['journal'],3),-x['year'],x['title'])):
   doi=x['doi'].replace('https://doi.org/','')
   status='Verified public data component — consult website access and scope notes' if doi in verified else 'Unverified metadata lead — repository contents still need checking'
   vals=[x['title'],x['journal'],str(x['year']),x['doi'],'; '.join(x['cues']),status]
   w.writerow(["'"+v if v.startswith(('=','+','-','@')) else v for v in vals])
write(out/'paper-data-shortlist.csv',all_rows)
write(out/'priority-paper-shortlist.csv',focus)
dest=repo/'_research';dest.mkdir(exist_ok=True)
write(dest/'paper-data-shortlist.csv',all_rows);write(dest/'priority-paper-shortlist.csv',focus)
(dest/'README.md').write_text('''# Paper data review queue

Source: the existing stouras.com paper-browser metadata in the personal GitHub repository (`lit/data` and `lit/data-ft50`). Screened on 16 October 2026, using the metadata year window 2006–2026. Boundary-year publication dates, completeness of journal coverage and full-text availability remain to be checked. This is not a completed twenty-year FT50 census.

The initial pass identified 355 broadly topic-related records with abstract-level sharing or availability cues. Of these, 125 also matched priority topics in their titles. Manually verified relevant papers are appended when their abstracts did not contain a matching cue. The title-focused file is the first review queue; the broader file retains additional leads. Journal order starts Management Science, M&SOM, POM.

An abstract-level phrase such as “data files are available” is a lead, not proof. A record with no sharing cue must not be classified as lacking public data. Packages may contain code only, synthetic data or incomplete restricted-data components. Before publishing an addition, check the paper identity, explicit dataset use, actual repository files, links, release/version differences, license, and limitations.

“Verified public data component” applies only to the documented dataset component in the website entry, not necessarily the complete study or every replication input.
''',encoding='utf-8')
print(json.dumps({'broad_queue':len(all_rows),'priority_queue':len(focus),'initial_sharing_leads':len(rows)}))
