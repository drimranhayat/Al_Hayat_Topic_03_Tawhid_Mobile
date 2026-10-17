import re,unicodedata,random
from topic_config import NARRATORS
from learning_content import BANK
REVISION="topic003-focused-v1"
def norm(s):
 return ' '.join(''.join(c for c in unicodedata.normalize('NFKD',s.replace('’',"'").replace('‘',"'").replace('–','-')) if not unicodedata.combining(c)).casefold().split())
def evidence(d,item):
 kind=item['basis']
 if kind=='T':text=d['en'];label='Published English selection';url=d['source']
 elif kind=='E':text=d['explanation'];label='Published explanation';url=d['source']
 elif kind.startswith('B'):text=d['hints'][int(kind[1:])-1];label='Published benefit '+kind[1:];url=d['source']
 elif kind=='M':text=d['ref']+'. Publisher assessment: '+d['grade']+'.';label='Reference and publisher grade';url=d['primary']
 else:raise ValueError(kind)
 assert norm(item['anchor']) in norm(text),(d['number'],item['q'],item['anchor'])
 # Select an actual source sentence containing the audited anchor, retaining its wording.
 candidates=re.split(r'(?<=[.!?])\s+|[\r\n]+',text)
 passage=next((s for s in candidates if norm(item['anchor']) in norm(s)),text)
 return {'label':label,'text':passage.strip(),'url':url,'anchor':item['anchor'],'field':kind}
def build_learning(rows):
 out={};positions=[i%4 for i in range(sum(len(s['mcq']) for s in BANK))];random.Random(REVISION).shuffle(positions);cursor=0
 for i,d in enumerate(rows):
  d['narrator']=NARRATORS[i];qa=[];mc=[]
  for j,item in enumerate(BANK[i]['qa']):
   qa.append({'id':f'{d["id"]}-qa-{j+1}','group':'Meaning and understanding','q':item['q'],'a':item['a'],'origin':'Editorial explanation based on the linked publisher material','lang':'en','source':d['source'],'evidence':evidence(d,item)})
  for j,item in enumerate(BANK[i]['mcq']):
   proof=evidence(d,item);options=[item['a']]+item['wrong'];assert len(set(map(norm,options)))==4
   correct=positions[cursor];cursor+=1;options.insert(correct,options.pop(0))
   mc.append({'id':f'{d["id"]}-mc-{j+1}','q':item['q'],'options':options,'correct':correct,'feedback':[item['why'] if x==item['a'] else 'The supported answer is: '+item['a'].rstrip('.')+'. '+item['why'] for x in options],'hint':item['hint'],'category':'Content practice','source':d['source'],'evidence':proof})
  out[d['id']]={'revision':REVISION,'narrator':NARRATORS[i],'qa':qa,'mcq':mc,'source':d['source'],'coverage':{'focusedAnswers':len(qa),'thematicQuestions':len(mc),'completeSanadProvided':False}}
 return out
