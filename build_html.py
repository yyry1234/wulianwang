import json, html as html_mod

# Read questions
with open("/Users/lujunjian/Documents/题库练习/questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

questions_json = json.dumps(questions, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>题库练习系统</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Noto+Sans+SC:wght@300;400;500;700&display=swap');

* {{ margin: 0; padding: 0; box-sizing: border-box; }}

:root {{
  --bg-primary: #0a0e17;
  --bg-secondary: #111827;
  --bg-card: #1a1f2e;
  --bg-card-hover: #222840;
  --neon-cyan: #00f0ff;
  --neon-purple: #b44aff;
  --neon-pink: #ff2d95;
  --neon-green: #39ff14;
  --neon-orange: #ff6a00;
  --text-primary: #e0e6f0;
  --text-secondary: #8892a4;
  --border-color: #2a3050;
  --glow-cyan: 0 0 10px rgba(0,240,255,0.3), 0 0 30px rgba(0,240,255,0.1);
  --glow-purple: 0 0 10px rgba(180,74,255,0.3), 0 0 30px rgba(180,74,255,0.1);
  --glow-green: 0 0 10px rgba(57,255,20,0.3);
  --glow-pink: 0 0 10px rgba(255,45,149,0.3);
}}

body {{
  font-family: 'Noto Sans SC', sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
  overflow-x: hidden;
}}

body::before {{
  content: '';
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background:
    radial-gradient(ellipse at 20% 50%, rgba(0,240,255,0.03) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 20%, rgba(180,74,255,0.03) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 80%, rgba(255,45,149,0.02) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}}

.container {{
  max-width: 1100px;
  margin: 0 auto;
  padding: 20px;
  position: relative;
  z-index: 1;
}}

/* Header */
.header {{
  text-align: center;
  padding: 40px 0 30px;
  border-bottom: 1px solid var(--border-color);
  margin-bottom: 30px;
}}

.header h1 {{
  font-family: 'Orbitron', sans-serif;
  font-size: 2.2em;
  font-weight: 900;
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: none;
  filter: drop-shadow(0 0 20px rgba(0,240,255,0.3));
  letter-spacing: 3px;
}}

.header .subtitle {{
  color: var(--text-secondary);
  margin-top: 8px;
  font-size: 0.95em;
}}

/* Mode Selection */
.mode-selector {{
  display: flex;
  justify-content: center;
  gap: 20px;
  margin: 30px 0;
  flex-wrap: wrap;
}}

.mode-btn {{
  padding: 16px 40px;
  border: 2px solid var(--border-color);
  border-radius: 12px;
  background: var(--bg-card);
  color: var(--text-primary);
  font-size: 1.1em;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  min-width: 200px;
}}

.mode-btn::before {{
  content: '';
  position: absolute;
  top: 0; left: -100%; right: 0; bottom: 0;
  background: linear-gradient(135deg, rgba(0,240,255,0.1), rgba(180,74,255,0.1));
  transition: left 0.3s ease;
  z-index: 0;
}}

.mode-btn:hover::before {{ left: 0; }}

.mode-btn:hover {{
  border-color: var(--neon-cyan);
  box-shadow: var(--glow-cyan);
  transform: translateY(-2px);
}}

.mode-btn.active {{
  border-color: var(--neon-cyan);
  box-shadow: var(--glow-cyan);
  background: linear-gradient(135deg, rgba(0,240,255,0.15), rgba(180,74,255,0.1));
}}

.mode-btn span {{
  position: relative;
  z-index: 1;
}}

/* Exam Config Panel */
.exam-config {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 30px;
  margin: 20px 0;
  display: none;
}}

.exam-config.active {{ display: block; }}

.exam-config h3 {{
  color: var(--neon-cyan);
  margin-bottom: 20px;
  font-size: 1.2em;
}}

.config-row {{
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 15px;
  flex-wrap: wrap;
}}

.config-row label {{
  min-width: 100px;
  color: var(--text-secondary);
}}

.config-row input[type="number"] {{
  width: 80px;
  padding: 8px 12px;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  color: var(--text-primary);
  font-size: 1em;
}}

.config-row input:focus {{
  outline: none;
  border-color: var(--neon-cyan);
  box-shadow: var(--glow-cyan);
}}

.config-row select {{
  padding: 8px 12px;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  color: var(--text-primary);
  font-size: 1em;
}}

.config-row select:focus {{
  outline: none;
  border-color: var(--neon-cyan);
}}

.start-exam-btn {{
  padding: 14px 50px;
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
  border: none;
  border-radius: 8px;
  color: #000;
  font-size: 1.1em;
  font-weight: 700;
  cursor: pointer;
  margin-top: 20px;
  transition: all 0.3s ease;
  letter-spacing: 1px;
}}

.start-exam-btn:hover {{
  transform: translateY(-2px);
  box-shadow: 0 0 30px rgba(0,240,255,0.4), 0 0 60px rgba(180,74,255,0.2);
}}

/* Timer Bar */
.timer-bar {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(10,14,23,0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--border-color);
  padding: 12px 20px;
  display: none;
  justify-content: space-between;
  align-items: center;
}}

.timer-bar.active {{ display: flex; }}

.timer-display {{
  font-family: 'Orbitron', sans-serif;
  font-size: 1.5em;
  color: var(--neon-cyan);
  text-shadow: 0 0 10px rgba(0,240,255,0.5);
}}

.timer-display.warning {{ color: var(--neon-orange); text-shadow: 0 0 10px rgba(255,106,0,0.5); }}
.timer-display.danger {{ color: var(--neon-pink); text-shadow: 0 0 10px rgba(255,45,149,0.5); animation: pulse 1s infinite; }}

@keyframes pulse {{
  0%, 100% {{ opacity: 1; }}
  50% {{ opacity: 0.5; }}
}}

.timer-info {{
  display: flex;
  gap: 20px;
  align-items: center;
}}

.timer-info .answered-count {{
  color: var(--neon-green);
  font-size: 0.95em;
}}

.submit-exam-btn {{
  padding: 10px 30px;
  background: linear-gradient(135deg, var(--neon-pink), var(--neon-purple));
  border: none;
  border-radius: 6px;
  color: #fff;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
}}

.submit-exam-btn:hover {{
  box-shadow: var(--glow-pink);
  transform: translateY(-1px);
}}

/* Nav Bar */
.nav-bar {{
  position: sticky;
  top: 60px;
  z-index: 99;
  background: rgba(10,14,23,0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--border-color);
  padding: 12px 20px;
  display: none;
  overflow-x: auto;
}}

.nav-bar.active {{ display: block; }}

.nav-bar .nav-inner {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  justify-content: center;
}}

.nav-dot {{
  width: 32px;
  height: 32px;
  border-radius: 6px;
  border: 1px solid var(--border-color);
  background: var(--bg-card);
  color: var(--text-secondary);
  font-size: 0.75em;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}}

.nav-dot:hover {{
  border-color: var(--neon-cyan);
  color: var(--neon-cyan);
}}

.nav-dot.answered {{
  background: rgba(0,240,255,0.15);
  border-color: var(--neon-cyan);
  color: var(--neon-cyan);
}}

.nav-dot.current {{
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
  color: #000;
  font-weight: 700;
  border-color: transparent;
}}

/* Question Cards */
.question-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 25px;
  margin-bottom: 20px;
  transition: all 0.3s ease;
}}

.question-card:hover {{
  border-color: rgba(0,240,255,0.3);
  box-shadow: 0 0 20px rgba(0,240,255,0.05);
}}

.question-card.highlight {{
  border-color: var(--neon-cyan);
  box-shadow: var(--glow-cyan);
}}

.question-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}}

.question-number {{
  font-family: 'Orbitron', sans-serif;
  font-size: 0.85em;
  color: var(--neon-purple);
  background: rgba(180,74,255,0.1);
  padding: 4px 12px;
  border-radius: 20px;
  border: 1px solid rgba(180,74,255,0.3);
}}

.question-kind {{
  font-size: 0.8em;
  padding: 4px 10px;
  border-radius: 4px;
  font-weight: 500;
}}

.kind-single {{
  color: var(--neon-cyan);
  background: rgba(0,240,255,0.1);
  border: 1px solid rgba(0,240,255,0.3);
}}

.kind-multi {{
  color: var(--neon-orange);
  background: rgba(255,106,0,0.1);
  border: 1px solid rgba(255,106,0,0.3);
}}

.question-stem {{
  font-size: 1.05em;
  line-height: 1.8;
  margin-bottom: 18px;
  color: var(--text-primary);
}}

.options-list {{
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.option-item {{
  padding: 12px 16px;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 12px;
  background: var(--bg-secondary);
}}

.option-item:hover {{
  border-color: var(--neon-cyan);
  background: rgba(0,240,255,0.05);
}}

.option-item.selected {{
  border-color: var(--neon-cyan);
  background: rgba(0,240,255,0.1);
  box-shadow: inset 0 0 10px rgba(0,240,255,0.05);
}}

.option-item .option-key {{
  font-family: 'Orbitron', sans-serif;
  font-size: 0.85em;
  color: var(--neon-cyan);
  min-width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(0,240,255,0.3);
  border-radius: 50%;
}}

.option-item.selected .option-key {{
  background: var(--neon-cyan);
  color: #000;
}}

/* Result styles */
.option-item.correct {{
  border-color: var(--neon-green);
  background: rgba(57,255,20,0.1);
}}

.option-item.correct .option-key {{
  background: var(--neon-green);
  color: #000;
  border-color: var(--neon-green);
}}

.option-item.wrong {{
  border-color: var(--neon-pink);
  background: rgba(255,45,149,0.1);
}}

.option-item.wrong .option-key {{
  background: var(--neon-pink);
  color: #000;
  border-color: var(--neon-pink);
}}

/* Review mode toggle */
.review-toggle {{
  padding: 8px 20px;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  color: var(--neon-cyan);
  cursor: pointer;
  font-size: 0.9em;
  transition: all 0.2s ease;
  margin-top: 15px;
}}

.review-toggle:hover {{
  border-color: var(--neon-cyan);
  box-shadow: var(--glow-cyan);
}}

/* Explanation */
.explanation {{
  margin-top: 15px;
  padding: 15px;
  background: rgba(180,74,255,0.05);
  border: 1px solid rgba(180,74,255,0.2);
  border-radius: 8px;
  line-height: 1.7;
  display: none;
}}

.explanation.visible {{ display: block; }}

.explanation .label {{
  color: var(--neon-purple);
  font-weight: 700;
  margin-bottom: 5px;
  font-size: 0.9em;
}}

.explanation .answer-label {{
  color: var(--neon-green);
  font-weight: 700;
  margin-bottom: 8px;
  font-size: 0.95em;
}}

/* Review Filters */
.filters {{
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  flex-wrap: wrap;
  align-items: center;
}}

.filter-btn {{
  padding: 8px 20px;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  background: var(--bg-card);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.9em;
}}

.filter-btn:hover {{
  border-color: var(--neon-cyan);
  color: var(--neon-cyan);
}}

.filter-btn.active {{
  border-color: var(--neon-cyan);
  color: var(--neon-cyan);
  background: rgba(0,240,255,0.1);
  box-shadow: var(--glow-cyan);
}}

.search-input {{
  flex: 1;
  min-width: 200px;
  padding: 8px 16px;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  color: var(--text-primary);
  font-size: 0.95em;
}}

.search-input:focus {{
  outline: none;
  border-color: var(--neon-cyan);
  box-shadow: var(--glow-cyan);
}}

.search-input::placeholder {{
  color: var(--text-secondary);
}}

/* Pagination */
.pagination {{
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  margin: 30px 0;
  flex-wrap: wrap;
}}

.page-btn {{
  padding: 8px 14px;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  background: var(--bg-card);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.9em;
}}

.page-btn:hover {{
  border-color: var(--neon-cyan);
  color: var(--neon-cyan);
}}

.page-btn.active {{
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
  color: #000;
  font-weight: 700;
  border-color: transparent;
}}

.page-btn:disabled {{
  opacity: 0.3;
  cursor: not-allowed;
}}

.pagination .page-info {{
  color: var(--text-secondary);
  font-size: 0.9em;
  margin: 0 10px;
}}

/* Score Display */
.score-panel {{
  background: var(--bg-card);
  border: 2px solid var(--neon-cyan);
  border-radius: 16px;
  padding: 40px;
  text-align: center;
  margin: 30px 0;
  box-shadow: var(--glow-cyan);
  display: none;
}}

.score-panel.active {{ display: block; }}

.score-panel h2 {{
  font-family: 'Orbitron', sans-serif;
  font-size: 1.8em;
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 25px;
}}

.score-circle {{
  width: 180px;
  height: 180px;
  border-radius: 50%;
  margin: 0 auto 25px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 4px solid var(--neon-cyan);
  box-shadow: var(--glow-cyan), inset 0 0 30px rgba(0,240,255,0.1);
}}

.score-circle .score-num {{
  font-family: 'Orbitron', sans-serif;
  font-size: 2.8em;
  font-weight: 900;
  color: var(--neon-cyan);
  line-height: 1;
}}

.score-circle .score-label {{
  font-size: 0.85em;
  color: var(--text-secondary);
  margin-top: 5px;
}}

.score-stats {{
  display: flex;
  justify-content: center;
  gap: 30px;
  margin: 25px 0;
  flex-wrap: wrap;
}}

.stat-item {{
  padding: 12px 25px;
  border-radius: 8px;
  text-align: center;
}}

.stat-item.correct-stat {{
  background: rgba(57,255,20,0.1);
  border: 1px solid rgba(57,255,20,0.3);
}}

.stat-item.wrong-stat {{
  background: rgba(255,45,149,0.1);
  border: 1px solid rgba(255,45,149,0.3);
}}

.stat-item.skip-stat {{
  background: rgba(255,106,0,0.1);
  border: 1px solid rgba(255,106,0,0.3);
}}

.stat-item .stat-num {{
  font-family: 'Orbitron', sans-serif;
  font-size: 1.8em;
  font-weight: 700;
}}

.stat-item.correct-stat .stat-num {{ color: var(--neon-green); }}
.stat-item.wrong-stat .stat-num {{ color: var(--neon-pink); }}
.stat-item.skip-stat .stat-num {{ color: var(--neon-orange); }}

.stat-item .stat-text {{
  color: var(--text-secondary);
  font-size: 0.85em;
  margin-top: 4px;
}}

.review-results-btn {{
  margin-top: 20px;
  padding: 12px 30px;
  background: transparent;
  border: 2px solid var(--neon-cyan);
  border-radius: 8px;
  color: var(--neon-cyan);
  font-size: 1em;
  cursor: pointer;
  transition: all 0.3s ease;
}}

.review-results-btn:hover {{
  background: rgba(0,240,255,0.1);
  box-shadow: var(--glow-cyan);
}}

.back-btn {{
  padding: 10px 25px;
  background: transparent;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
  margin-bottom: 20px;
  display: inline-block;
}}

.back-btn:hover {{
  border-color: var(--neon-cyan);
  color: var(--neon-cyan);
}}

/* Scrollbar */
::-webkit-scrollbar {{ width: 8px; height: 8px; }}
::-webkit-scrollbar-track {{ background: var(--bg-primary); }}
::-webkit-scrollbar-thumb {{ background: var(--border-color); border-radius: 4px; }}
::-webkit-scrollbar-thumb:hover {{ background: var(--neon-cyan); }}

/* Responsive */
@media (max-width: 768px) {{
  .header h1 {{ font-size: 1.5em; }}
  .mode-btn {{ min-width: 150px; padding: 12px 25px; }}
  .question-card {{ padding: 18px; }}
  .score-stats {{ gap: 15px; }}
  .timer-display {{ font-size: 1.1em; }}
}}

/* Confirm Dialog */
.modal-overlay {{
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.7);
  z-index: 1000;
  align-items: center;
  justify-content: center;
}}

.modal-overlay.active {{ display: flex; }}

.modal-box {{
  background: var(--bg-card);
  border: 1px solid var(--neon-cyan);
  border-radius: 12px;
  padding: 30px;
  max-width: 450px;
  width: 90%;
  text-align: center;
  box-shadow: var(--glow-cyan);
}}

.modal-box h3 {{
  color: var(--neon-cyan);
  margin-bottom: 15px;
}}

.modal-box p {{
  color: var(--text-secondary);
  margin-bottom: 25px;
  line-height: 1.6;
}}

.modal-btns {{
  display: flex;
  gap: 15px;
  justify-content: center;
}}

.modal-btns button {{
  padding: 10px 30px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1em;
  transition: all 0.2s ease;
}}

.modal-btns .btn-confirm {{
  background: linear-gradient(135deg, var(--neon-pink), var(--neon-purple));
  border: none;
  color: #fff;
  font-weight: 700;
}}

.modal-btns .btn-cancel {{
  background: transparent;
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
}}

.modal-btns .btn-confirm:hover {{ box-shadow: var(--glow-pink); }}
.modal-btns .btn-cancel:hover {{ border-color: var(--neon-cyan); color: var(--neon-cyan); }}
</style>
</head>
<body>

<div class="container">
  <div class="header">
    <h1>题库练习系统</h1>
    <div class="subtitle">物联网技术 · {len(questions)} 道题目</div>
  </div>

  <div class="mode-selector">
    <button class="mode-btn" id="btn-review" onclick="switchMode('review')"><span>📖 复习模式</span></button>
    <button class="mode-btn" id="btn-exam" onclick="switchMode('exam')"><span>📝 考试模式</span></button>
  </div>

  <!-- Exam Config -->
  <div class="exam-config" id="exam-config">
    <h3>⚙️ 考试设置</h3>
    <div class="config-row">
      <label>题目范围：</label>
      <select id="exam-scope" onchange="toggleExamScope()">
        <option value="random">随机抽取</option>
        <option value="all">使用全部 {len(questions)} 题</option>
      </select>
    </div>
    <div id="random-config">
      <div class="config-row">
        <label>单选题数：</label>
        <input type="number" id="single-count" value="40" min="1" max="260">
        <span style="color:var(--text-secondary);font-size:0.85em;">(共 260 题)</span>
      </div>
      <div class="config-row">
        <label>多选题数：</label>
        <input type="number" id="multi-count" value="15" min="1" max="65">
        <span style="color:var(--text-secondary);font-size:0.85em;">(共 65 题)</span>
      </div>
    </div>
    <div class="config-row">
      <label>考试时长：</label>
      <input type="number" id="exam-time" value="60" min="5" max="180">
      <span style="color:var(--text-secondary);font-size:0.85em;">分钟</span>
    </div>
    <button class="start-exam-btn" onclick="startExam()">开始考试</button>
  </div>

  <!-- Timer Bar -->
  <div class="timer-bar" id="timer-bar">
    <div class="timer-display" id="timer-display">60:00</div>
    <div class="timer-info">
      <span class="answered-count" id="answered-count">已答: 0/0</span>
      <button class="submit-exam-btn" onclick="confirmSubmit()">交卷</button>
    </div>
  </div>

  <!-- Nav Bar -->
  <div class="nav-bar" id="nav-bar">
    <div class="nav-inner" id="nav-inner"></div>
  </div>

  <!-- Score Panel -->
  <div class="score-panel" id="score-panel">
    <h2>考试成绩</h2>
    <div class="score-circle">
      <div class="score-num" id="score-num">0</div>
      <div class="score-label">得分</div>
    </div>
    <div class="score-stats">
      <div class="stat-item correct-stat">
        <div class="stat-num" id="stat-correct">0</div>
        <div class="stat-text">正确</div>
      </div>
      <div class="stat-item wrong-stat">
        <div class="stat-num" id="stat-wrong">0</div>
        <div class="stat-text">错误</div>
      </div>
      <div class="stat-item skip-stat">
        <div class="stat-num" id="stat-skip">0</div>
        <div class="stat-text">未答</div>
      </div>
    </div>
    <button class="review-results-btn" onclick="reviewExamResults()">查看解析</button>
    <button class="review-results-btn" style="margin-left:15px;" onclick="backToHome()">返回首页</button>
  </div>

  <!-- Review Filters -->
  <div id="review-section" style="display:none;">
    <div class="filters">
      <button class="filter-btn active" data-filter="all" onclick="setFilter('all',this)">全部</button>
      <button class="filter-btn" data-filter="single" onclick="setFilter('single',this)">单选题</button>
      <button class="filter-btn" data-filter="multi" onclick="setFilter('multi',this)">多选题</button>
      <input type="text" class="search-input" id="search-input" placeholder="🔍 搜索题目..." oninput="onSearch()">
    </div>
    <div id="review-list"></div>
    <div class="pagination" id="pagination"></div>
  </div>

  <!-- Exam Questions -->
  <div id="exam-section" style="display:none;"></div>
</div>

<!-- Confirm Modal -->
<div class="modal-overlay" id="confirm-modal">
  <div class="modal-box">
    <h3>确认交卷</h3>
    <p id="confirm-msg">确定要交卷吗？</p>
    <div class="modal-btns">
      <button class="btn-confirm" onclick="doSubmit()">确认交卷</button>
      <button class="btn-cancel" onclick="closeModal()">继续答题</button>
    </div>
  </div>
</div>

<script>
const allQuestions = {questions_json};

let currentMode = null;
let examQuestions = [];
let examAnswers = {{}};
let timerInterval = null;
let timeLeft = 0;
let examSubmitted = false;

// Review state
let reviewFilter = 'all';
let reviewSearch = '';
let reviewPage = 1;
const PER_PAGE = 20;

function switchMode(mode) {{
  currentMode = mode;
  document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('btn-' + mode).classList.add('active');
  document.getElementById('exam-config').classList.toggle('active', mode === 'exam');
  document.getElementById('review-section').style.display = mode === 'review' ? 'block' : 'none';
  document.getElementById('exam-section').style.display = 'none';
  document.getElementById('score-panel').classList.remove('active');
  document.getElementById('timer-bar').classList.remove('active');
  document.getElementById('nav-bar').classList.remove('active');
  if (timerInterval) {{ clearInterval(timerInterval); timerInterval = null; }}
  if (mode === 'review') {{ reviewPage = 1; renderReview(); }}
}}

function toggleExamScope() {{
  const scope = document.getElementById('exam-scope').value;
  document.getElementById('random-config').style.display = scope === 'random' ? 'block' : 'none';
}}

function shuffle(arr) {{
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {{
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }}
  return a;
}}

function startExam() {{
  const scope = document.getElementById('exam-scope').value;
  let singles = allQuestions.filter(q => q.kind === 'single');
  let multis = allQuestions.filter(q => q.kind === 'multi');

  if (scope === 'random') {{
    const sc = Math.min(parseInt(document.getElementById('single-count').value) || 40, singles.length);
    const mc = Math.min(parseInt(document.getElementById('multi-count').value) || 15, multis.length);
    examQuestions = [...shuffle(singles).slice(0, sc), ...shuffle(multis).slice(0, mc)];
  }} else {{
    examQuestions = shuffle(allQuestions);
  }}

  examAnswers = {{}};
  examSubmitted = false;
  timeLeft = (parseInt(document.getElementById('exam-time').value) || 60) * 60;

  document.getElementById('exam-config').classList.remove('active');
  document.getElementById('review-section').style.display = 'none';
  document.getElementById('score-panel').classList.remove('active');
  document.getElementById('exam-section').style.display = 'block';
  document.getElementById('timer-bar').classList.add('active');
  document.getElementById('nav-bar').classList.add('active');

  renderExamQuestions();
  renderNavBar();
  startTimer();
}}

function startTimer() {{
  updateTimerDisplay();
  timerInterval = setInterval(() => {{
    timeLeft--;
    updateTimerDisplay();
    if (timeLeft <= 0) {{
      clearInterval(timerInterval);
      doSubmit();
    }}
  }}, 1000);
}}

function updateTimerDisplay() {{
  const m = Math.floor(timeLeft / 60);
  const s = timeLeft % 60;
  const display = document.getElementById('timer-display');
  display.textContent = String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
  display.className = 'timer-display' + (timeLeft <= 60 ? ' danger' : timeLeft <= 300 ? ' warning' : '');
  const answered = Object.keys(examAnswers).length;
  document.getElementById('answered-count').textContent = '已答: ' + answered + '/' + examQuestions.length;
}}

function renderNavBar() {{
  const nav = document.getElementById('nav-inner');
  nav.innerHTML = examQuestions.map((q, i) =>
    '<div class="nav-dot' + (examAnswers[i] !== undefined ? ' answered' : '') + '" onclick="scrollToQ(' + i + ')" title="第' + (i+1) + '题">' + (i+1) + '</div>'
  ).join('');
}}

function scrollToQ(idx) {{
  const el = document.getElementById('exam-q-' + idx);
  if (el) {{
    el.scrollIntoView({{ behavior: 'smooth', block: 'center' }};
    el.classList.add('highlight');
    setTimeout(() => el.classList.remove('highlight'), 1500);
  }}
  document.querySelectorAll('.nav-dot').forEach((d, i) => d.classList.toggle('current', i === idx));
}}

function renderExamQuestions() {{
  const container = document.getElementById('exam-section');
  container.innerHTML = examQuestions.map((q, i) => {{
    const isMulti = q.kind === 'multi';
    const optionsHtml = q.options.map(opt => {{
      return '<div class="option-item" data-q="' + i + '" data-key="' + opt.key + '" onclick="selectOption(' + i + ',\\'' + opt.key + '\\',' + isMulti + ')">'
        + '<span class="option-key">' + opt.key + '</span>'
        + '<span>' + escapeHtml(opt.text) + '</span>'
        + '</div>';
    }}).join('');
    return '<div class="question-card" id="exam-q-' + i + '">'
      + '<div class="question-header">'
      + '<span class="question-number">第 ' + (i+1) + ' 题</span>'
      + '<span class="question-kind ' + (isMulti ? 'kind-multi' : 'kind-single') + '">' + (isMulti ? '多选' : '单选') + '</span>'
      + '</div>'
      + '<div class="question-stem">' + escapeHtml(q.stem) + '</div>'
      + '<div class="options-list">' + optionsHtml + '</div>'
      + '<div class="explanation" id="exam-exp-' + i + '">'
      + '<div class="answer-label">正确答案：' + q.answer.join('、') + '</div>'
      + '<div class="label">解析：</div>'
      + '<div>' + escapeHtml(q.explanation || '暂无解析') + '</div>'
      + '</div>'
      + '</div>';
  }}).join('');
}}

function selectOption(qIdx, key, isMulti) {{
  if (examSubmitted) return;
  if (!isMulti) {{
    examAnswers[qIdx] = [key];
    document.querySelectorAll('[data-q="' + qIdx + '"]').forEach(el => {{
      el.classList.toggle('selected', el.dataset.key === key);
    }});
  }} else {{
    if (!examAnswers[qIdx]) examAnswers[qIdx] = [];
    const idx = examAnswers[qIdx].indexOf(key);
    if (idx >= 0) {{
      examAnswers[qIdx].splice(idx, 1);
    }} else {{
      examAnswers[qIdx].push(key);
    }}
    if (examAnswers[qIdx].length === 0) delete examAnswers[qIdx];
    document.querySelectorAll('[data-q="' + qIdx + '"]').forEach(el => {{
      el.classList.toggle('selected', examAnswers[qIdx] && examAnswers[qIdx].includes(el.dataset.key));
    }});
  }}
  renderNavBar();
}}

function confirmSubmit() {{
  const unanswered = examQuestions.length - Object.keys(examAnswers).length;
  const msg = unanswered > 0
    ? '还有 ' + unanswered + ' 题未作答，确定要交卷吗？'
    : '确定要交卷吗？';
  document.getElementById('confirm-msg').textContent = msg;
  document.getElementById('confirm-modal').classList.add('active');
}}

function closeModal() {{
  document.getElementById('confirm-modal').classList.remove('active');
}}

function doSubmit() {{
  closeModal();
  if (timerInterval) {{ clearInterval(timerInterval); timerInterval = null; }}
  examSubmitted = true;

  let correct = 0, wrong = 0, skip = 0;
  examQuestions.forEach((q, i) => {{
    const userAns = examAnswers[i];
    if (!userAns) {{ skip++; return; }}
    const correctAns = [...q.answer].sort();
    const userSorted = [...userAns].sort();
    const isCorrect = correctAns.length === userSorted.length && correctAns.every((v, j) => v === userSorted[j]);
    if (isCorrect) correct++;
    else wrong++;

    // Highlight options
    const items = document.querySelectorAll('[data-q="' + i + '"]');
    items.forEach(el => {{
      el.classList.remove('selected');
      const k = el.dataset.key;
      if (correctAns.includes(k)) el.classList.add('correct');
      if (userSorted.includes(k) && !correctAns.includes(k)) el.classList.add('wrong');
    }});
    document.getElementById('exam-exp-' + i).classList.add('visible');
  }});

  const total = examQuestions.length;
  const score = total > 0 ? Math.round(correct / total * 100) : 0;

  // Hide timer & nav, show score
  document.getElementById('timer-bar').classList.remove('active');
  document.getElementById('nav-bar').classList.remove('active');
  document.getElementById('score-panel').classList.add('active');
  document.getElementById('score-num').textContent = score;
  document.getElementById('stat-correct').textContent = correct;
  document.getElementById('stat-wrong').textContent = wrong;
  document.getElementById('stat-skip').textContent = skip;

  // Scroll to top
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

function reviewExamResults() {{
  document.getElementById('score-panel').classList.remove('active');
  document.getElementById('exam-section').style.display = 'block';
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

function backToHome() {{
  document.getElementById('score-panel').classList.remove('active');
  document.getElementById('exam-section').style.display = 'none';
  document.getElementById('timer-bar').classList.remove('active');
  document.getElementById('nav-bar').classList.remove('active');
  currentMode = null;
  document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

// Review Mode
function getFilteredQuestions() {{
  let qs = allQuestions;
  if (reviewFilter !== 'all') qs = qs.filter(q => q.kind === reviewFilter);
  if (reviewSearch.trim()) {{
    const s = reviewSearch.trim().toLowerCase();
    qs = qs.filter(q => q.stem.toLowerCase().includes(s) || q.options.some(o => o.text.toLowerCase().includes(s)));
  }}
  return qs;
}}

function renderReview() {{
  const filtered = getFilteredQuestions();
  const totalPages = Math.max(1, Math.ceil(filtered.length / PER_PAGE));
  if (reviewPage > totalPages) reviewPage = totalPages;
  const start = (reviewPage - 1) * PER_PAGE;
  const pageItems = filtered.slice(start, start + PER_PAGE);

  const list = document.getElementById('review-list');
  list.innerHTML = pageItems.map((q, idx) => {{
    const realIdx = allQuestions.indexOf(q);
    const isMulti = q.kind === 'multi';
    const optionsHtml = q.options.map(opt => {{
      const isCorrect = q.answer.includes(opt.key);
      return '<div class="option-item' + (isCorrect ? ' correct' : '') + '">'
        + '<span class="option-key">' + opt.key + '</span>'
        + '<span>' + escapeHtml(opt.text) + '</span>'
        + '</div>';
    }}).join('');
    return '<div class="question-card">'
      + '<div class="question-header">'
      + '<span class="question-number">第 ' + (q.id || (realIdx+1)) + ' 题</span>'
      + '<span class="question-kind ' + (isMulti ? 'kind-multi' : 'kind-single') + '">' + (isMulti ? '多选' : '单选') + '</span>'
      + '</div>'
      + '<div class="question-stem">' + escapeHtml(q.stem) + '</div>'
      + '<div class="options-list">' + optionsHtml + '</div>'
      + '<button class="review-toggle" onclick="toggleExplanation(this)">显示解析</button>'
      + '<div class="explanation">'
      + '<div class="answer-label">正确答案：' + q.answer.join('、') + '</div>'
      + '<div class="label">解析：</div>'
      + '<div>' + escapeHtml(q.explanation || '暂无解析') + '</div>'
      + '</div>'
      + '</div>';
  }}).join('');

  renderPagination(totalPages, filtered.length);
}}

function toggleExplanation(btn) {{
  const exp = btn.nextElementSibling;
  const visible = exp.classList.toggle('visible');
  btn.textContent = visible ? '隐藏解析' : '显示解析';
}}

function setFilter(filter, btn) {{
  reviewFilter = filter;
  reviewPage = 1;
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderReview();
}}

let searchTimer = null;
function onSearch() {{
  clearTimeout(searchTimer);
  searchTimer = setTimeout(() => {{
    reviewSearch = document.getElementById('search-input').value;
    reviewPage = 1;
    renderReview();
  }}, 300);
}}

function renderPagination(totalPages, totalItems) {{
  const pg = document.getElementById('pagination');
  if (totalPages <= 1) {{
    pg.innerHTML = '<span class="page-info">共 ' + totalItems + ' 题</span>';
    return;
  }}
  let html = '<button class="page-btn" onclick="goPage(' + (reviewPage - 1) + ')" ' + (reviewPage <= 1 ? 'disabled' : '') + '>‹</button>';
  const range = [];
  for (let i = 1; i <= totalPages; i++) {{
    if (i === 1 || i === totalPages || (i >= reviewPage - 2 && i <= reviewPage + 2)) {{
      range.push(i);
    }}
  }}
  let last = 0;
  for (const p of range) {{
    if (last && p - last > 1) html += '<span style="color:var(--text-secondary)">…</span>';
    html += '<button class="page-btn' + (p === reviewPage ? ' active' : '') + '" onclick="goPage(' + p + ')">' + p + '</button>';
    last = p;
  }}
  html += '<button class="page-btn" onclick="goPage(' + (reviewPage + 1) + ')" ' + (reviewPage >= totalPages ? 'disabled' : '') + '>›</button>';
  html += '<span class="page-info">共 ' + totalItems + ' 题</span>';
  pg.innerHTML = html;
}}

function goPage(p) {{
  const filtered = getFilteredQuestions();
  const totalPages = Math.max(1, Math.ceil(filtered.length / PER_PAGE));
  if (p < 1 || p > totalPages) return;
  reviewPage = p;
  renderReview();
  window.scrollTo({{ top: document.getElementById('review-section').offsetTop - 20, behavior: 'smooth' }});
}}

function escapeHtml(text) {{
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}}
</script>
</body>
</html>'''

with open("/Users/lujunjian/Documents/题库练习/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Done! Generated index.html with {len(questions)} questions.")
import os
size = os.path.getsize("/Users/lujunjian/Documents/题库练习/index.html")
print(f"File size: {size} bytes ({size/1024:.1f} KB)")
