import json,sys,time,urllib.request as u,urllib.parse as p
H={'User-Agent':'dataset-library-verifier (mailto:kstouras@gmail.com)'}
slug=sys.argv[1]; out=sys.argv[2]; res=[]; page=1
while True:
    for a in range(5):
        try:
            d=json.load(u.urlopen(u.Request('https://zenodo.org/api/communities/%s/records?'%slug+p.urlencode({'size':25,'page':page}),headers=H),timeout=60)); break
        except Exception as e: print(page,'ERR',str(e)[:60],flush=True); time.sleep(8); d=None
    if not d: break
    hs=d['hits']['hits']
    for h in hs:
        m=h['metadata']; res.append({'doi':h.get('doi'),'cdoi':h.get('conceptdoi'),'title':m.get('title'),'date':m.get('publication_date'),'access':m.get('access_right'),'lic':(m.get('license') or {}).get('id'),'desc':(m.get('description') or '')[:500],'rel':[(r.get('relation'),r.get('identifier')) for r in m.get('related_identifiers',[])],'files':[(f.get('key'),f.get('size')) for f in h.get('files',[])][:30]})
    print(page,d['hits']['total'],len(res),flush=True)
    if len(hs)<25: break
    page+=1; time.sleep(1.5)
json.dump(res,open(out,'w')); print('DONE',len(res),flush=True)
