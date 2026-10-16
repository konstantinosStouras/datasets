import json,sys,os,time,urllib.request as u,urllib.parse as p
H={'User-Agent':'dataset-library-verifier (mailto:kstouras@gmail.com)'}
todo=json.load(open(sys.argv[1])); out=sys.argv[2]; B=40
res=json.load(open(out)) if os.path.exists(out) else {}
start=int(sys.argv[3]) if len(sys.argv)>3 else 0
def esc(d): return d.replace('/','\\/').replace(':','\\:').replace('(','\\(').replace(')','\\)')
for i in range(start,len(todo),B):
    batch=todo[i:i+B]
    if all(d in res for d in batch): continue
    q='relatedIdentifiers.relatedIdentifier:(%s)'%' OR '.join('"%s"'%d for d in batch)
    hits={d:[] for d in batch}; page=1; ok=False
    for attempt in range(4):
        try:
            while True:
                r=json.load(u.urlopen(u.Request('https://api.datacite.org/dois?'+p.urlencode({'query':q,'page[size]':100,'page[number]':page}),headers=H),timeout=60))
                for x in r['data']:
                    at=x['attributes']
                    rel={(y.get('relatedIdentifier') or '').lower() for y in at.get('relatedIdentifiers',[])}
                    rec={'doi':x['id'],'title':(at.get('titles') or [{}])[0].get('title',''),'pub':at.get('publisher'),'year':at.get('publicationYear'),'type':(at.get('types') or {}).get('resourceTypeGeneral'),'rels':[ (y.get('relationType'),y.get('relatedIdentifier')) for y in at.get('relatedIdentifiers',[]) if y.get('relatedIdentifier','').lower() in hits]}
                    for d in batch:
                        if d in rel: hits[d].append(rec)
                tot=r.get('meta',{}).get('total',0)
                if page*100>=tot or page>=10: break
                page+=1
            ok=True; break
        except Exception as e:
            print(i,'ERR',str(e)[:80],flush=True); time.sleep(5*(attempt+1))
    if ok:
        res.update(hits)
    else:
        for d in batch: res[d]={'err':True}
    if (i//B)%25==0:
        json.dump(res,open(out,'w')); print('done',i+B,'of',len(todo),'hits so far',sum(1 for v in res.values() if isinstance(v,list) and v),flush=True)
    time.sleep(0.4)
json.dump(res,open(out,'w')); print('ALLDONE',len(res),flush=True)
