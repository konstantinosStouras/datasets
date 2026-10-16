import json,sys,re,urllib.request as u,urllib.parse as p,time
H={'User-Agent':'dataset-library-verifier (mailto:kstouras@gmail.com)'}
host=sys.argv[1]; src=sys.argv[2]; out=sys.argv[3]
items=json.load(open(src)); res={}
def norm(s): return re.sub(r'[^a-z0-9]','',(s or '').lower())
for i,(doi,title,year) in enumerate(items):
    t=re.sub(r'[^\w\s]',' ',title); t=re.sub(r'\s+',' ',t).strip()
    words=t.split()
    q='"%s"'%' '.join(words[:12])
    try:
        if host=='dv':
            d=json.load(u.urlopen(u.Request('https://dataverse.harvard.edu/api/search?'+p.urlencode({'q':q,'type':'dataset','per_page':5}),headers=H),timeout=40))['data']
            hits=[(x['global_id'],x['name'],x.get('published_at','')[:10]) for x in d['items']]
        else:
            d=json.load(u.urlopen(u.Request('https://zenodo.org/api/records?'+p.urlencode({'q':q,'size':5}),headers=H),timeout=40))
            hits=[(x.get('doi'),x['metadata'].get('title'),x['metadata'].get('resource_type',{}).get('type')) for x in d['hits']['hits']]
        nt=norm(title)
        good=[h for h in hits if nt and (nt in norm(h[1]) or norm(h[1]) in nt or len(set(norm(title)[:30])&set(norm(h[1])))>0 and nt[:25] in norm(h[1]))]
        res[doi]={'title':title,'year':year,'hits':hits,'good':good}
        if good: print(i,doi,year,'|',title[:60],'|',good,flush=True)
    except Exception as e:
        res[doi]={'title':title,'year':year,'err':str(e)[:100]}; print(i,'ERR',str(e)[:80],flush=True); time.sleep(3)
    if i%50==0: print('..',i,flush=True); json.dump(res,open(out,'w'))
    time.sleep(1.2 if host=='dv' else 1.5)
json.dump(res,open(out,'w')); print('DONE',len(res))
