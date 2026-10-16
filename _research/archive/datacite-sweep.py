import json,sys,csv,urllib.request as u,urllib.parse as p,concurrent.futures as cf,time
H={'User-Agent':'dataset-library-verifier (mailto:kstouras@gmail.com)'}
def q(doi):
    url='https://api.datacite.org/dois?page%5Bsize%5D=10&query='+p.quote('"%s"'%doi)
    for t in range(3):
        try:
            r=json.load(u.urlopen(u.Request(url,headers=H),timeout=40))
            return doi,[{'doi':i['attributes']['doi'],'title':(i['attributes']['titles'] or [{}])[0].get('title',''),'pub':i['attributes'].get('publisher'),'year':i['attributes'].get('publicationYear'),'type':(i['attributes'].get('types') or {}).get('resourceTypeGeneral')} for i in r.get('data',[])]
        except Exception as e:
            time.sleep(1.5*(t+1)); err=str(e)
    return doi,{'err':err}
dois=[l.strip() for l in open(sys.argv[1]) if l.strip()]
out={}
with cf.ThreadPoolExecutor(6) as ex:
    for d,r in ex.map(q,dois): out[d]=r
json.dump(out,open(sys.argv[2],'w'))
hits={d:r for d,r in out.items() if isinstance(r,list) and r}
errs=[d for d,r in out.items() if isinstance(r,dict)]
print('queried',len(dois),'with hits',len(hits),'errors',len(errs))
