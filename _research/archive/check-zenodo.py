# HISTORICAL REFERENCE: see README.md before running.
import json,urllib.request
from pathlib import Path
records=[]
for rid in ['5172146','3709084']:
 with urllib.request.urlopen('https://zenodo.org/api/records/'+rid,timeout=30) as r: m=json.load(r)
 files=[{'name':f['key'],'size':f['size'],'url':f['links']['self']} for f in m['files']]
 target=next(f for f in files if f['name']=='tech differentiation tf-idf.csv') if rid=='5172146' else next(f for f in files if f['name'].endswith('.zip'))
 with urllib.request.urlopen(urllib.request.Request(target['url'],headers={'Range':'bytes=0-511'}),timeout=30) as r:
  sample=r.read(512);status=r.status;kind=r.headers.get('Content-Type')
 result={'id':rid,'title':m['metadata']['title'],'access':m['metadata'].get('access_right'),'license':m['metadata'].get('license'),'files':files,'checked_file':target['name'],'status':status,'type':kind,'sample':sample[:250].decode(errors='replace') if rid=='5172146' else sample[:4].hex()}
 records.append(result)
print(json.dumps(records,ensure_ascii=False,indent=2))
Path(__file__).with_name('zenodo-link-checks.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
