import json,sys,re,subprocess,urllib.request as u,urllib.parse as p,os
H={'User-Agent':'dataset-library-verifier (mailto:kstouras@gmail.com)'}
def g(x):
    return json.load(u.urlopen(u.Request(x,headers=H),timeout=40))
def fulltext(doi,out):
    w=g('https://api.openalex.org/works/doi:'+doi+'?select=locations,open_access')
    cands=[]
    for l in w.get('locations',[]):
        for k in ('pdf_url',):
            if l.get(k): cands.append((l.get(k),l.get('version'),(l.get('source') or {}).get('display_name')))
    for url,ver,src in cands:
        try:
            r=u.urlopen(u.Request(url,headers={**H,'Accept':'application/pdf'}),timeout=60);b=r.read()
            if b[:4]==b'%PDF':
                open(out+'.pdf','wb').write(b)
                subprocess.run(['pdftotext','-layout',out+'.pdf',out+'.txt'],check=False)
                return url,ver,src,len(b)
        except Exception as e: continue
    return None
if __name__=='__main__':
    doi=sys.argv[1];pat=sys.argv[2];out='oa_'+re.sub(r'[^0-9a-z]','_',doi.lower())
    r=fulltext(doi,out);print(doi,'->',r)
    if r and os.path.exists(out+'.txt'):
        t=open(out+'.txt',errors='replace').read();print('words',len(t.split()))
        lines=t.split('\n');n=0
        for i,l in enumerate(lines):
            if re.search(pat,l,re.I):
                print('  L%d: %s'%(i,re.sub(r'\s+',' ',l.strip())[:230]));n+=1
                if n>=int(sys.argv[3] if len(sys.argv)>3 else 10): break
