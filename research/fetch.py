import pathlib,json,subprocess,concurrent.futures
root=pathlib.Path(__file__).parent;out=root.parent/'source-data';out.mkdir(exist_ok=True)
import sys
sys.path.insert(0,str(root.parent))
from topic_config import ids
(root/'selected-ids.json').write_text(json.dumps(ids))
def get(task):
 id,lang=task;p=out/f'{id}-{lang}.json'
 if not p.exists():
  for attempt in range(2):
   r=subprocess.run(['curl','-fsS','--max-time','40',f'https://hadeethenc.com/api/v1/hadeeths/one/?language={lang}&id={id}','-o',str(p)],capture_output=True)
   if not r.returncode:break
  if r.returncode:return id,lang,'ERROR '+r.stderr.decode()[:75]
 try:
  a=json.loads(p.read_text());return id,lang,a.get('grade'),a.get('attribution')
 except:return id,lang,'BAD JSON'
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for result in ex.map(get,[(id,l) for id in ids for l in ['en','ur']]):print(*result,flush=True)
