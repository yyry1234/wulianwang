import json

with open('questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f, ensure_ascii=False)

json_str = json.dumps(data, ensure_ascii=False)

html = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>在线题库系统</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0a0e1a;--card:#111827;--card2:#1a2235;--border:#1e3a5f;
  --cyan:#00e5ff;--purple:#a855f7;--green:#22c55e;--red:#ef4444;
  --text:#e2e8f0;--text2:#94a3b8;--white:#fff;
  --glow:0 0 15px rgba(0,229,255,.3);--glow2:0 0 15px rgba(168,85,247,.3);
}
body{background:var(--bg);color:var(--text);font-family:-apple-system,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;min-height:100vh;line-height:1.6}
/* Animated bg */
body::before{content:'';position:fixed;top:0;left:0;width:100%;height:100%;background:
  radial-gradient(ellipse at 20% 50%,rgba(0,229,255,.06) 0%,transparent 50%),
  radial-gradient(ellipse at 80% 20%,rgba(168,85,247,.06) 0%,transparent 50%),
  radial-gradient(ellipse at 50% 80%,rgba(0,229,255,.04) 0%,transparent 50%);z-index:0;pointer-events:none}
.app{position:relative;z-index:1;max-width:960px;margin:0 auto;padding:20px}

/* Header */
.header{text-align:center;padding:40px 0 30px;position:relative}
.header h1{font-size:2.2rem;background:linear-gradient(135deg,var(--cyan),var(--purple));-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-shadow:none;font-weight:800;letter-spacing:2px}
.header p{color:var(--text2);margin-top:8px;font-size:.95rem}
.stats-bar{display:flex;justify-content:center;gap:30px;margin-top:18px;flex-wrap:wrap}
.stat{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:12px 24px;text-align:center;min-width:120px}
.stat .num{font-size:1.6rem;font-weight:700;color:var(--cyan)}
.stat .label{font-size:.75rem;color:var(--text2);margin-top:2px}

/* Nav */
.mode-nav{display:flex;gap:16px;justify-content:center;margin:30px 0;flex-wrap:wrap}
.mode-btn{background:var(--card);border:2px solid var(--border);border-radius:14px;padding:18px 32px;cursor:pointer;transition:all .3s;color:var(--text);font-size:1rem;min-width:200px;text-align:center}
.mode-btn:hover{border-color:var(--cyan);box-shadow:var(--glow);transform:translateY(-2px)}
.mode-btn.active{border-color:var(--cyan);background:linear-gradient(135deg,rgba(0,229,255,.1),rgba(168,85,247,.1))}
.mode-btn .icon{font-size:2rem;display:block;margin-bottom:6px}
.mode-btn .title{font-weight:700;font-size:1.1rem}
.mode-btn .desc{font-size:.75rem;color:var(--text2);margin-top:4px}

/* Exam config */
.exam-config{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:24px;margin:20px 0;display:none}
.config-row{display:flex;align-items:center;gap:12px;margin:12px 0;flex-wrap:wrap}
.config-label{color:var(--text2);font-size:.9rem;min-width:100px}
.radio-group{display:flex;gap:10px;flex-wrap:wrap}
.radio-opt{background:var(--card2);border:2px solid var(--border);border-radius:10px;padding:10px 18px;cursor:pointer;transition:all .3s;font-size:.85rem;color:var(--text)}
.radio-opt:hover{border-color:var(--purple)}
.radio-opt.selected{border-color:var(--cyan);background:rgba(0,229,255,.1);color:var(--cyan)}
.start-btn{background:linear-gradient(135deg,var(--cyan),var(--purple));color:#000;border:none;border-radius:12px;padding:14px 48px;font-size:1.1rem;font-weight:700;cursor:pointer;margin-top:20px;transition:all .3s}
.start-btn:hover{transform:translateY(-2px);box-shadow:0 0 30px rgba(0,229,255,.4)}

/* Search/Filter */
.toolbar{display:flex;gap:12px;margin:16px 0;flex-wrap:wrap;align-items:center}
.search-box{flex:1;min-width:200px;background:var(--card);border:1px solid var(--border);border-radius:10px;padding:10px 16px;color:var(--text);font-size:.9rem;outline:none;transition:border-color .3s}
.search-box:focus{border-color:var(--cyan)}
.filter-btn{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:10px 16px;color:var(--text2);cursor:pointer;transition:all .3s;font-size:.85rem}
.filter-btn:hover,.filter-btn.active{border-color:var(--purple);color:var(--purple)}

/* Question card */
.q-card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:24px;margin:16px 0;transition:all .3s}
.q-card:hover{border-color:rgba(0,229,255,.3);box-shadow:0 0 20px rgba(0,229,255,.08)}
.q-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:8px}
.q-num{background:linear-gradient(135deg,var(--cyan),var(--purple));color:#000;font-weight:700;padding:4px 14px;border-radius:20px;font-size:.8rem}
.q-kind{font-size:.75rem;padding:3px 10px;border-radius:8px;font-weight:600}
.q-kind.single{background:rgba(0,229,255,.15);color:var(--cyan)}
.q-kind.multi{background:rgba(168,85,247,.15);color:var(--purple)}
.q-stem{font-size:1rem;line-height:1.8;margin-bottom:16px;color:var(--white)}
.q-options{display:flex;flex-direction:column;gap:10px;margin-bottom:16px}
.q-opt{display:flex;align-items:flex-start;gap:10px;background:var(--card2);border:2px solid transparent;border-radius:10px;padding:10px 14px;cursor:pointer;transition:all .25s;font-size:.9rem}
.q-opt:hover{border-color:rgba(0,229,255,.3)}
.q-opt .key{font-weight:700;color:var(--cyan);min-width:24px}
.q-opt.selected{border-color:var(--cyan);background:rgba(0,229,255,.08)}
.q-opt.correct{border-color:var(--green);background:rgba(34,197,94,.1)}
.q-opt.wrong{border-color:var(--red);background:rgba(239,68,68,.1)}
.q-opt.show-correct{border-color:var(--green);background:rgba(34,197,94,.06)}
.q-explain{background:rgba(0,229,255,.05);border-left:3px solid var(--cyan);border-radius:0 10px 10px 0;padding:14px 18px;margin-top:12px;font-size:.88rem;line-height:1.7;color:var(--text2);display:none}
.q-explain.show{display:block}
.q-explain strong{color:var(--cyan)}

/* Exam controls */
.exam-bar{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:16px 24px;margin:16px 0;display:none;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}
.exam-bar .progress{font-size:.9rem;color:var(--text2)}
.exam-bar .timer{font-size:1.1rem;font-weight:700;color:var(--cyan);font-variant-numeric:tabular-nums}
.submit-btn{background:linear-gradient(135deg,var(--green),#16a34a);color:#fff;border:none;border-radius:10px;padding:10px 32px;font-weight:700;cursor:pointer;font-size:.95rem;transition:all .3s}
.submit-btn:hover{transform:translateY(-1px);box-shadow:0 0 20px rgba(34,197,94,.4)}

/* Result */
.result-panel{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:30px;margin:20px 0;text-align:center;display:none}
.result-panel .score{font-size:3rem;font-weight:800;background:linear-gradient(135deg,var(--cyan),var(--purple));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.result-panel .detail{color:var(--text2);margin:10px 0;font-size:.95rem}
.result-panel .back-btn{background:var(--card2);border:1px solid var(--border);border-radius:10px;padding:10px 28px;color:var(--text);cursor:pointer;font-size:.9rem;margin-top:16px;transition:all .3s}
.result-panel .back-btn:hover{border-color:var(--cyan)}

/* Review answer button */
.show-answer-btn{background:linear-gradient(135deg,rgba(0,229,255,.15),rgba(168,85,247,.15));border:1px solid var(--border);border-radius:10px;padding:8px 20px;color:var(--cyan);cursor:pointer;font-size:.85rem;transition:all .3s;margin-top:8px}
.show-answer-btn:hover{border-color:var(--cyan);box-shadow:var(--glow)}

/* Scrollbar */
::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:var(--cyan)}

/* Responsive */
@media(max-width:640px){
  .header h1{font-size:1.5rem}
  .mode-btn{min-width:140px;padding:14px 18px}
  .q-card{padding:16px}
}
</style>
</head>
<body>
<div class="app" id="app">
  <div class="header">
    <h1>⚡ 在线题库系统</h1>
    <p>智能复习 · 模拟考试 · 科技风格</p>
    <div class="stats-bar">
      <div class="stat"><div class="num" id="totalCount">0</div><div class="label">总题目</div></div>
      <div class="stat"><div class="num" id="singleCount">0</div><div class="label">单选题</div></div>
      <div class="stat"><div class="num" id="multiCount">0</div><div class="label">多选题</div></div>
    </div>
  </div>

  <div class="mode-nav" id="modeNav">
    <div class="mode-btn active" onclick="switchMode('review')">
      <span class="icon">📖</span>
      <div class="title">在线复习</div>
      <div class="desc">逐题练习，查看答案解析</div>
    </div>
    <div class="mode-btn" onclick="switchMode('exam')">
      <span class="icon">📝</span>
      <div class="title">模拟考试</div>
      <div class="desc">随机抽题，限时作答</div>
    </div>
  </div>

  <!-- Review Toolbar -->
  <div class="toolbar" id="reviewToolbar">
    <input class="search-box" id="searchBox" placeholder="🔍 搜索题目关键词..." oninput="filterQuestions()">
    <button class="filter-btn active" onclick="setFilter('all',this)">全部</button>
    <button class="filter-btn" onclick="setFilter('single',this)">单选</button>
    <button class="filter-btn" onclick="setFilter('multi',this)">多选</button>
  </div>

  <!-- Exam Config -->
  <div class="exam-config" id="examConfig">
    <h3 style="color:var(--cyan);margin-bottom:16px">⚙️ 考试设置</h3>
    <div class="config-row">
      <span class="config-label">题目范围：</span>
      <div class="radio-group" id="examScope">
        <div class="radio-opt selected" onclick="selectScope(this,'random')">随机抽题 (40单+15多)</div>
        <div class="radio-opt" onclick="selectScope(this','all')">全部题目 (325题)</div>
      </div>
    </div>
    <button class="start-btn" onclick="startExam()">🚀 开始考试</button>
  </div>

  <!-- Exam Bar -->
  <div class="exam-bar" id="examBar">
    <div class="progress" id="examProgress">进度: 0/0</div>
    <div class="timer" id="examTimer">00:00</div>
    <button class="submit-btn" onclick="submitExam()">✅ 交卷</button>
  </div>

  <!-- Result -->
  <div class="result-panel" id="resultPanel">
    <div class="score" id="resultScore"></div>
    <div class="detail" id="resultDetail"></div>
    <button class="back-btn" onclick="backToHome()">返回首页</button>
  </div>

  <!-- Questions Container -->
  <div id="questionList"></div>
</div>

<script>
const QUESTIONS = PLACEHOLDER_JSON;

let mode = 'review';
let filterKind = 'all';
let searchText = '';
let examScope = 'random';
let examQuestions = [];
let examAnswers = {};
let examTimer = null;
let examSeconds = 0;

// Init
document.getElementById('totalCount').textContent = QUESTIONS.length;
document.getElementById('singleCount').textContent = QUESTIONS.filter(q=>q.kind==='single').length;
document.getElementById('multiCount').textContent = QUESTIONS.filter(q=>q.kind==='multi').length;

function shuffle(arr){const a=[...arr];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}

function switchMode(m){
  mode=m;
  document.querySelectorAll('.mode-btn').forEach((b,i)=>b.classList.toggle('active',i===(m==='review'?0:1)));
  document.getElementById('reviewToolbar').style.display=m==='review'?'flex':'none';
  document.getElementById('examConfig').style.display=m==='exam'?'block':'none';
  document.getElementById('examBar').style.display='none';
  document.getElementById('resultPanel').style.display='none';
  document.getElementById('questionList').innerHTML='';
  if(m==='review') renderReview();
}

function setFilter(f,el){
  filterKind=f;
  document.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
  el.classList.add('active');
  renderReview();
}

function filterQuestions(){
  searchText=document.getElementById('searchBox').value.trim();
  renderReview();
}

function getFiltered(){
  return QUESTIONS.filter(q=>{
    if(filterKind!=='all'&&q.kind!==filterKind) return false;
    if(searchText&&!q.stem.includes(searchText)) return false;
    return true;
  });
}

function renderReview(){
  const list=document.getElementById('questionList');
  const qs=getFiltered();
  list.innerHTML=qs.map((q,i)=>renderQCard(q,i,false)).join('');
}

function renderQCard(q,idx,isExam){
  const opts=q.options.map(o=>{
    const cls=isExam?'q-opt':'q-opt';
    return `<div class="q-opt" data-qid="${q.id}" data-key="${o.key}" ${isExam?`onclick="selectAnswer(${q.id},'${o.key}',${q.kind==='multi'})"`:''} id="opt-${q.id}-${o.key}">
      <span class="key">${o.key}.</span><span>${o.text}</span></div>`;
  }).join('');
  const kindLabel=q.kind==='single'?'<span class="q-kind single">单选</span>':'<span class="q-kind multi">多选</span>';
  const answerBtn=isExam?'':`<button class="show-answer-btn" onclick="toggleAnswer(${q.id})">👁 查看答案</button>`;
  const explain=`<div class="q-explain" id="explain-${q.id}"><strong>✅ 答案：${q.answer.join(',')}</strong><br>${q.explanation}</div>`;
  return `<div class="q-card" id="qcard-${q.id}">
    <div class="q-header"><span class="q-num">#${q.id}</span>${kindLabel}</div>
    <div class="q-stem">${q.stem}</div>
    <div class="q-options">${opts}</div>
    ${answerBtn}${explain}</div>`;
}

function toggleAnswer(qid){
  const el=document.getElementById('explain-'+qid);
  if(el) el.classList.toggle('show');
}

function selectScope(el,scope){
  examScope=scope;
  document.querySelectorAll('#examScope .radio-opt').forEach(b=>b.classList.remove('selected'));
  el.classList.add('selected');
}

function startExam(){
  const allSingles=shuffle(QUESTIONS.filter(q=>q.kind==='single'));
  const allMultis=shuffle(QUESTIONS.filter(q=>q.kind==='multi'));
  if(examScope==='random'){
    examQuestions=[...allSingles.slice(0,40),...allMultis.slice(0,15)];
  }else{
    examQuestions=shuffle(QUESTIONS);
  }
  examQuestions=examQuestions.map((q,i)=>({...q,_idx:i+1}));
  examAnswers={};
  examSeconds=0;
  document.getElementById('examConfig').style.display='none';
  document.getElementById('examBar').style.display='flex';
  document.getElementById('resultPanel').style.display='none';
  const list=document.getElementById('questionList');
  list.innerHTML=examQuestions.map(q=>renderQCard(q,q._idx,true)).join('');
  updateExamProgress();
  if(examTimer) clearInterval(examTimer);
  examTimer=setInterval(()=>{
    examSeconds++;
    const m=String(Math.floor(examSeconds/60)).padStart(2,'0');
    const s=String(examSeconds%60).padStart(2,'0');
    document.getElementById('examTimer').textContent=m+':'+s;
  },1000);
}

function selectAnswer(qid,key,isMulti){
  if(!examAnswers[qid]) examAnswers[qid]=[];
  const idx=examAnswers[qid].indexOf(key);
  if(isMulti){
    if(idx>=0) examAnswers[qid].splice(idx,1); else examAnswers[qid].push(key);
  }else{
    examAnswers[qid]=idx>=0?[]:[key];
  }
  // Update UI
  const opts=document.querySelectorAll(`[data-qid="${qid}"]`);
  opts.forEach(o=>{
    const k=o.dataset.key;
    o.classList.toggle('selected',examAnswers[qid].includes(k));
  });
  updateExamProgress();
}

function updateExamProgress(){
  const answered=Object.values(examAnswers).filter(a=>a.length>0).length;
  document.getElementById('examProgress').textContent=`进度: ${answered}/${examQuestions.length}`;
}

function submitExam(){
  if(!confirm('确认交卷？')) return;
  clearInterval(examTimer);
  let correct=0;
  examQuestions.forEach(q=>{
    const userAns=(examAnswers[q.id]||[]).sort().join('');
    const rightAns=[...q.answer].sort().join('');
    if(userAns===rightAns) correct++;
  });
  const total=examQuestions.length;
  const pct=Math.round(correct/total*100);
  document.getElementById('examBar').style.display='none';
  document.getElementById('resultPanel').style.display='block';
  document.getElementById('resultScore').textContent=pct+'分';
  document.getElementById('resultDetail').innerHTML=
    `共 ${total} 题，答对 <span style="color:var(--green);font-weight:700">${correct}</span> 题，`+
    `答错 <span style="color:var(--red);font-weight:700">${total-correct}</span> 题<br>`+
    `用时 ${Math.floor(examSeconds/60)}分${examSeconds%60}秒`;
  // Show correct/wrong on cards
  examQuestions.forEach(q=>{
    const userAns=(examAnswers[q.id]||[]).sort().join('');
    const rightAns=[...q.answer].sort().join('');
    const isCorrect=userAns===rightAns;
    const opts=document.querySelectorAll(`[data-qid="${q.id}"]`);
    opts.forEach(o=>{
      const k=o.dataset.key;
      const inUser=examAnswers[q.id]&&examAnswers[q.id].includes(k);
      const inRight=q.answer.includes(k);
      o.style.pointerEvents='none';
      if(inRight) o.classList.add('correct');
      else if(inUser&&!inRight) o.classList.add('wrong');
    });
    // Show explanation
    const exp=document.getElementById('explain-'+q.id);
    if(exp){exp.classList.add('show');exp.style.display='block'}
  });
}

function backToHome(){
  document.getElementById('examConfig').style.display='none';
  document.getElementById('examBar').style.display='none';
  document.getElementById('resultPanel').style.display='none';
  document.getElementById('questionList').innerHTML='';
  mode='review';
  document.querySelectorAll('.mode-btn').forEach((b,i)=>b.classList.toggle('active',i===0));
  document.getElementById('reviewToolbar').style.display='flex';
  renderReview();
}

// Init render
renderReview();
</script>
</body>
</html>''';

html = html.replace('PLACEHOLDER_JSON', json_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done! File size: {len(html)} bytes')
