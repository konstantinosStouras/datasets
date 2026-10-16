import json,sys,re,subprocess,os,urllib.request as u
H={'User-Agent':'dataset-library-verifier (mailto:kstouras@gmail.com)'}
def g(x,raw=False):
    try:
        b=u.urlopen(u.Request(x,headers=H),timeout=90).read()
        return b if raw else json.loads(b)
    except Exception as e: return {'err':str(e)[:150]} if not raw else b''
def rd(path):
    t=''
    if path.endswith('.pdf'):
        subprocess.run(['pdftotext','-layout',path,path+'.txt'],check=False);t=open(path+'.txt',errors='replace').read() if os.path.exists(path+'.txt') else ''
    elif path.endswith('.docx'):
        import zipfile;t=re.sub(r'<[^>]+>',' ',zipfile.ZipFile(path).read('word/document.xml').decode('utf8','replace'))
    else: t=open(path,errors='replace').read()
    return re.sub(r'[ \t]+',' ',t)
os.makedirs('dvr',exist_ok=True)
for pid in sys.argv[1:]:
    host='dataverse.nl' if pid.startswith('10.34894') else 'dataverse.harvard.edu'
    r=g('https://%s/api/datasets/:persistentId/?persistentId=doi:%s'%(host,pid.upper()))
    if 'data' not in r: print('##',pid,r);continue
    v=r['data']['latestVersion']
    f={x['typeName']:x['value'] for x in v['metadataBlocks']['citation']['fields']}
    lic=v.get('license');lic=lic.get('name') if isinstance(lic,dict) else lic
    pub=f.get('publication');pubs=[ (p.get('publicationCitation',{}).get('value','')[:90], p.get('publicationIDNumber',{}).get('value',''), p.get('publicationRelationType',{}).get('value','')) for p in (pub or [])] if isinstance(pub,list) else pub
    desc=re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',(f.get('dsDescription') or [{}])[0].get('dsDescriptionValue',{}).get('value','')))[:260]
    files=v['files'];nres=sum(1 for x in files if x.get('restricted'))
    tot=sum(x['dataFile']['filesize'] for x in files)/1e6
    print('##',pid,'|',f.get('title','')[:100],'| v',v['versionNumber'],v['versionMinorNumber'],'|',lic,'| terms:',(v.get('termsOfUse') or '')[:100])
    print('   pub:',pubs);print('   desc:',desc);print('   files',len(files),'restricted',nres,'total MB',round(tot,1))
    for x in sorted(files,key=lambda x:-x['dataFile']['filesize'])[:8]: print('     ',x['dataFile']['filename'],round(x['dataFile']['filesize']/1e6,2),'MB','RESTRICTED' if x.get('restricted') else '',x['dataFile']['id'])
    rm=[x for x in files if re.search(r'readme|read_me|read me|data availab|appendix',x['dataFile']['filename'],re.I) and x['dataFile']['filename'].lower().endswith(('.pdf','.txt','.md','.docx')) and not x.get('restricted') and x['dataFile']['filesize']<3e6]
    for x in rm[:1]:
        path='dvr/%s_%s'%(pid.split('/')[-1].lower(),re.sub(r'[^A-Za-z0-9.]','_',x['dataFile']['filename']))
        b=g('https://%s/api/access/datafile/%d'%(host,x['dataFile']['id']),raw=True);open(path,'wb').write(b)
        t=rd(path)
        print('   README',x['dataFile']['filename'],len(t.split()),'words');
        for m in list(re.finditer(r'[^.\n]{0,160}(restricted|confidential|proprietary|cannot (be )?(share|publicly)|not (publicly )?available|license[d]? |access to|permission|Compustat|Data Use Agreement|DUA|public use|publicly available)[^.\n]{0,200}',t,re.I))[:5]: print('     -',re.sub(r'\s+',' ',m.group(0)).strip()[:300])
