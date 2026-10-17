import pathlib,json,concurrent.futures,subprocess,re,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent.parent))
from topic_config import ENTRIES
root=pathlib.Path(__file__).parent;raw=root/'publisher-pages';raw.mkdir(exist_ok=True)
def get(row):
 id=row[0];p=raw/(id+'.html')
 if not p.exists():
  r=subprocess.run(['curl','-fsS','--max-time','40',f'https://hadeethenc.com/en/browse/hadith/{id}','-o',str(p)],capture_output=True)
  if r.returncode:return id,{'error':r.stderr.decode()[:80]}
 for t in re.findall(r'<script type="application/ld\+json">(.*?)</script>',p.read_text(),re.S):
  try:obj=json.loads(t)
  except:continue
  for g in obj.get('@graph',[]):
   if g.get('@type')=='Article':
    props={v['name']:v['value'] for v in g.get('additionalProperty',[])}
    return id,{'url':f'https://hadeethenc.com/en/browse/hadith/{id}','properties':props}
 return id,{'error':'Missing source metadata'}
out={}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for id,x in ex.map(get,ENTRIES):out[id]=x;print(id,x.get('properties',x),flush=True)
(root/'references.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
