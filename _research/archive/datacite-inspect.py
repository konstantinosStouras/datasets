import json,sys,re,urllib.request as u
H={'User-Agent':'dataset-library-verifier (mailto:kstouras@gmail.com)'}
def g(x):
    try: return json.load(u.urlopen(u.Request(x,headers=H),timeout=40))
    except Exception as e: return {'err':str(e)[:150]}
def clean(s): return re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',s or '')).strip()
for doi in sys.argv[1:]:
    a=g('https://api.datacite.org/dois/'+doi)
    if 'data' not in a: print('##',doi,a); continue
    at=a['data']['attributes']
    print('##',doi,'|',at['titles'][0]['title'][:100],'|',at['publisher'],at['publicationYear'],'| version',at.get('version'),'| types',at.get('types',{}).get('resourceTypeGeneral'))
    print('   url',at.get('url'),'| rights',[r.get('rights') for r in at.get('rightsList',[])],'| sizes',at.get('sizes'),'| creators',[c.get('name') for c in at.get('creators',[])][:4])
    print('   related',[(x['relationType'],x['relatedIdentifier']) for x in at.get('relatedIdentifiers',[]) if 'relatedIdentifier' in x][:6])
    print('   desc',clean(' '.join(d['description'] for d in at.get('descriptions',[])))[:500])
    pub=at['publisher']
    if 'Zenodo' in pub:
        rid=doi.split('zenodo.')[-1].split('.')[0]
        z=g('https://zenodo.org/api/records/'+rid)
        if 'files' in z:
            print('   ZENODO',z['id'],z['metadata'].get('access_right'),z['metadata'].get('license'),'versions',z['metadata'].get('version'))
            for f in z['files'][:12]: print('     ',f['key'],round(f['size']/1e6,2),'MB')
    elif 'Dataverse' in pub:
        host='dataverse.harvard.edu' if 'Harvard' in pub else 'dataverse.nl'
        v=g('https://%s/api/datasets/:persistentId/?persistentId=doi:%s'%(host,doi.upper().replace('DVN/','DVN/') if 'DVN' in doi.upper() else doi.upper()))
        if 'data' in v:
            v=v['data']['latestVersion'];print('   DV',host,'v',v['versionNumber'],v['versionMinorNumber'],'license',(v.get('license') or {}).get('name') if isinstance(v.get('license'),dict) else v.get('license'),v.get('termsOfUse'))
            for f in v['files'][:14]: print('     ',f['dataFile']['filename'],round(f['dataFile']['filesize']/1e6,2),'MB','RESTRICTED' if f.get('restricted') else 'public',f['dataFile']['id'])
        else: print('   DV err',v)
