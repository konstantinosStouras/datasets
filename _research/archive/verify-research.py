# HISTORICAL REFERENCE: see README.md before running.
import urllib.request, urllib.parse, json, re
def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':'DatasetLibrary/1.0'})
    return urllib.request.urlopen(req,timeout=25)
url='https://eml.berkeley.edu/~bhhall/NBER06.html'
with get(url) as response:
    html=response.read().decode(errors="replace")
links=[urllib.parse.urljoin(url,x) for x in re.findall(r'href=["\']([^"\']+)',html,re.I)]
print(json.dumps(links[:16],indent=2))
with get('https://api.crossref.org/works/10.1287/mnsc.2022.00857') as response:
    m=json.load(response)['message']
print(json.dumps({k:m.get(k) for k in ['title','container-title','published','published-online','published-print','volume','issue','type']},indent=2))

