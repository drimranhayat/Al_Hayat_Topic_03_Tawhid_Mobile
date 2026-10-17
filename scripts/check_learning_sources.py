from pathlib import Path
import sys,json,collections,html
root=Path(sys.argv[1] if len(sys.argv)>1 else 'dist');base=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(base))
from learning_builder import norm,evidence,REVISION
from learning_content import BANK
from topic_config import ids,NARRATORS
rows=json.loads((root/'content.json').read_text());bank=json.loads((base/'learning-content.json').read_text())
assert [d['id'] for d in rows]==ids
positions=collections.Counter();keys=[];stems=[];qstems=[];qa_count=0;mc_count=0
for i,d in enumerate(rows):
 s=bank[d['id']];assert s['revision']==REVISION and s['narrator']==NARRATORS[i]
 assert 1<=len(s['qa'])<=3 and 1<=len(s['mcq'])<=2
 assert len(s['qa'])==len(BANK[i]['qa']) and len(s['mcq'])==len(BANK[i]['mcq'])
 for item,q in zip(BANK[i]['qa'],s['qa']):
  assert q['evidence']==evidence(d,item);assert q['q']==item['q'] and q['a']==item['a'];qstems.append(norm(q['q']));qa_count+=1
 for item,q in zip(BANK[i]['mcq'],s['mcq']):
  assert q['evidence']==evidence(d,item);assert q['options'][q['correct']]==item['a'];assert len(set(map(norm,q['options'])))==4
  assert q['hint'] and all(q['feedback']);positions[q['correct']]+=1;keys.append(q['id']);stems.append(norm(q['q']));mc_count+=1
 assert not {norm(q['q']) for q in s['qa']} & {norm(q['q']) for q in s['mcq']}
assert len(set(stems))==len(stems) and len(keys)==len(set(keys)) and len(set(qstems))==len(qstems)
assert max(positions.values())-min(positions.values())<=1
print(f'PASS: {qa_count} focused explanatory Q&A and {mc_count} MCQs, exact source anchors, four distinct choices, balanced positions, unique stems, independent phrasing, correct reporter mapping.')
