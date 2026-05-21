import re
import sys

with open(r'c:\Users\Windows\Desktop\application\index.html', 'r', encoding='utf-8') as f:
    old_content = f.read()

# Extract old constants
content_match = re.search(r'(const CONTENT=.*?;)', old_content, re.DOTALL)
lessons_match = re.search(r'(const LESSONS=\[.*?\];)', old_content, re.DOTALL)
worlds_match = re.search(r'(const WORLDS=\[.*?\];)', old_content, re.DOTALL)
svg_match = re.search(r'(const SVG=\{.*?\};)', old_content, re.DOTALL)

# Extract old functions that shouldn't change
onboarding_match = re.search(r'(// ONBOARDING.*?)(?=// WORLD MAP)', old_content, re.DOTALL)
levelpath_match = re.search(r'(// LEVEL PATH.*?)(?=// LEVEL ROUTER)', old_content, re.DOTALL)
levelrouter_match = re.search(r'(// LEVEL ROUTER.*?)(?=// PLACEHOLDER)', old_content, re.DOTALL)
placeholder_match = re.search(r'(// PLACEHOLDER.*?)(?=// BARTER SIM)', old_content, re.DOTALL)
barter_match = re.search(r'(// BARTER SIM.*?)(?=// LIFE CLOCK SIM)', old_content, re.DOTALL)
lifeclock_match = re.search(r'(// LIFE CLOCK SIM.*?)(?=// QUIZ ENGINE)', old_content, re.DOTALL)

new_html = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fin-Survival: Belajar Keuangan</title>
<meta name="description" content="Aplikasi edukasi keuangan interaktif untuk anak muda Indonesia.">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
/* === STYLE LAMA TETAP SAMA + PENAMBAHAN BARU === */
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#fafafa;--fg:#09090b;--primary:#18181b;--secondary:#f4f4f5;--accent:#3b82f6;--border:#e4e4e7;--muted:#71717a;--radius:1rem}
body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--fg);-webkit-font-smoothing:antialiased;overflow-x:hidden}
.app{min-height:100vh;max-width:28rem;margin:0 auto;padding:1.5rem;position:relative}

/* HEADER DASHBOARD DUOLINGO-STYLE */
.dashboard-header{background:#fff;border-bottom:1px solid var(--border);padding:1rem 1.5rem;border-radius:var(--radius);box-shadow:0 2px 8px -2px rgb(0 0 0/.1);margin-bottom:1.5rem;display:flex;align-items:center;justify-content:space-between}
.streak{display:flex;align-items:center;gap:6px;font-weight:700;font-size:1.1rem}
.streak-flame{font-size:1.8rem;animation:flame 1.2s infinite alternate}
@keyframes flame{0%{transform:scale(1)}100%{transform:scale(1.15)}}
.xp-container{display:flex;align-items:center;gap:8px}
.xp-bar{width:110px;height:8px;background:var(--secondary);border-radius:9999px;overflow:hidden}
.xp-fill{height:100%;background:linear-gradient(90deg,#3b82f6,#22c55e);transition:width .4s ease}
.level-badge{background:var(--primary);color:#fff;padding:2px 10px;border-radius:9999px;font-size:13px;font-weight:800}

/* MASCOT IMPROVEMENT */
.mascot-wrap{position:relative;margin:0 auto}
.mascot-wrap img{width:100%;height:100%;object-fit:contain;mix-blend-mode:multiply}
.mascot-shadow{position:absolute;bottom:-8px;left:50%;transform:translateX(-50%);width:65%;height:12px;background:rgba(0,0,0,.08);filter:blur(6px);border-radius:50%}
.mascot-bob{animation:bob 2.8s ease-in-out infinite}
.mascot-wiggle{animation:wiggle 2.2s ease-in-out infinite}
.mascot-excited{animation:excited 0.8s ease-in-out infinite}
.mascot-proud{animation:proud 3s ease-in-out infinite}

@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
@keyframes wiggle{0%,100%{transform:translateY(0) rotate(0)}25%{transform:translateY(-8px) rotate(-8deg)}75%{transform:translateY(-8px) rotate(8deg)}}
@keyframes excited{0%,100%{transform:scale(1) translateY(0)}50%{transform:scale(1.12) translateY(-15px)}}
@keyframes proud{0%,100%{transform:scale(1)}50%{transform:scale(1.08)}}

.card{background:#fff;border:1px solid var(--border);box-shadow:0 4px 6px -1px rgb(0 0 0/.1),0 2px 4px -2px rgb(0 0 0/.1);border-radius:var(--radius);transition:all .2s ease}
.btn{background:var(--primary);color:#fff;padding:.85rem 1.5rem;border-radius:.75rem;font-weight:700;border:none;cursor:pointer;font-size:1.05rem;font-family:inherit;transition:all .2s;display:flex;align-items:center;justify-content:center;gap:.5rem;width:100%}
.btn:active{transform:scale(.97)}
.hearts{font-size:1.6rem;display:flex;gap:4px}
.label{font-size:10px;text-transform:uppercase;font-weight:700;color:#a1a1aa;letter-spacing:.1em}
.text-center{text-align:center}
.hidden{display:none!important}
.screen{animation:fadeIn .3s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeSlide{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}
.grid-1{display:grid;grid-template-columns:1fr;gap:.75rem}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.option-card{display:flex;align-items:center;padding:1.25rem;text-align:left;cursor:pointer;font-family:inherit;background:#fff;border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 4px 6px -1px rgb(0 0 0/.1);transition:all .2s;width:100%}
.option-card:hover{border-color:#d4d4d8;transform:translateY(-2px)}
.option-card .icon{font-size:2.5rem;margin-right:1.25rem;transition:transform .2s}
.option-card:hover .icon{transform:scale(1.1)}
.option-card .info{flex:1}
.option-card .info h3{font-weight:700;font-size:1.125rem;margin-bottom:2px}
.option-card .info p{font-size:.75rem;color:var(--muted)}
.option-card .chevron{color:#d4d4d8;transition:color .2s;font-size:1.25rem}
.option-card:hover .chevron{color:var(--primary)}
.age-card{padding:1rem;text-align:center;font-weight:700;font-size:1.125rem;cursor:pointer;font-family:inherit;background:#fff;border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 4px 6px -1px rgb(0 0 0/.1);transition:all .2s}
.age-card:hover{transform:translateY(-2px);border-color:#d4d4d8}
.age-card small{display:block;font-size:.625rem;opacity:.5;font-weight:400;margin-top:2px}
.world-card{padding:1.5rem;display:flex;justify-content:space-between;align-items:center;cursor:pointer;font-family:inherit;background:#fff;border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 4px 6px -1px rgb(0 0 0/.1);transition:all .2s;position:relative;overflow:hidden;width:100%}
.world-card:hover{transform:translateY(-2px);border-color:#d4d4d8}
.world-card .emoji{font-size:3rem;transition:transform .2s}
.world-card:hover .emoji{transform:scale(1.1)}
.world-card .lock-overlay{position:absolute;inset:0;background:rgba(255,255,255,.8);backdrop-filter:blur(1px);display:flex;align-items:center;justify-content:center}
h1{font-size:1.875rem;font-weight:700;letter-spacing:-.025em;color:var(--primary)}
h2{font-size:1.5rem;font-weight:700;color:var(--primary);line-height:1.3}
.sub{color:var(--muted);font-weight:500;font-size:.625rem;text-transform:uppercase;letter-spacing:.1em}
.btn-back{background:#fff;border:1px solid #e4e4e7;border-radius:.75rem;padding:.75rem;cursor:pointer;box-shadow:0 1px 2px rgb(0 0 0/.05);transition:background .2s}
.btn-back:hover{background:var(--secondary)}
.btn-ghost{background:transparent;color:var(--muted);border:none;cursor:pointer;font-family:inherit;font-weight:700;font-size:.75rem;text-transform:uppercase;letter-spacing:.1em;transition:color .2s}
.btn-ghost:hover{color:#ef4444}
.path-line{position:absolute;top:0;bottom:0;left:50%;width:4px;background:var(--secondary);transform:translateX(-50%);z-index:0}
.level-node{position:relative;z-index:10;display:flex;flex-direction:column;align-items:center;cursor:pointer;border:none;background:transparent;font-family:inherit}
.level-icon{width:5rem;height:5rem;border-radius:1rem;display:flex;align-items:center;justify-content:center;font-size:1.875rem;transition:all .2s}
.level-icon-active{background:#fff;border:1px solid #e4e4e7;box-shadow:0 4px 6px -1px rgb(0 0 0/.1)}
.level-icon-active:hover{box-shadow:0 10px 15px -3px rgb(0 0 0/.1);transform:translateY(-4px)}
.level-icon-locked{background:var(--secondary);color:#d4d4d8;border:1px solid #f4f4f5}
.level-badge{margin-top:.75rem;padding:.375rem 1rem;border-radius:9999px;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;border:1px solid}
.level-badge-active{background:var(--primary);color:#fff;border-color:var(--primary)}
.level-badge-locked{background:var(--secondary);color:#a1a1aa;border-color:#f4f4f5}
.star-badge{position:absolute;top:-6px;right:-6px;background:var(--primary);color:#fff;padding:4px;border-radius:50%;border:2px solid #fff;box-shadow:0 1px 2px rgb(0 0 0/.1);line-height:0}
.sim-header{text-align:center;background:var(--primary);color:#fff;padding:1.5rem;border-radius:1rem;position:relative;overflow:hidden}
.sim-header .label{color:#a1a1aa}
.sim-header .value{font-size:2.5rem;font-weight:700;letter-spacing:-.025em}
.trade-card{display:flex;align-items:center;padding:1rem;cursor:pointer;font-family:inherit;width:100%}
.trade-icon{font-size:2.5rem;margin-right:1rem;transition:transform .2s}
.trade-card:hover .trade-icon{transform:scale(1.1)}
.msg-box{background:#eff6ff;padding:1rem;border-radius:.75rem;border:1px solid #bfdbfe;font-size:.875rem;font-weight:500;color:#1e40af;font-style:italic;text-align:center}
.aha-box{background:var(--secondary);padding:1.5rem;border-radius:1rem;border:1px solid #e4e4e7;text-align:left}
.aha-icon{font-size:1.5rem;background:#fff;padding:.5rem;border-radius:.5rem;border:1px solid #f4f4f5;box-shadow:0 1px 2px rgb(0 0 0/.05);display:inline-flex}
.input-field{width:100%;background:#fff;border:1px solid var(--border);border-radius:.75rem;padding:.75rem 1rem;font-weight:700;font-size:1.25rem;font-family:inherit;outline:none;transition:border-color .2s}
.input-field:focus{border-color:var(--primary)}
.input-sm{font-size:1.125rem}
.spent-panel{background:var(--primary);color:#fff;padding:1.5rem;border-radius:1rem;margin-top:auto}
.spent-value{font-size:2.5rem;font-weight:700;color:#f87171;letter-spacing:-.025em}
.tag-red{font-size:10px;color:#dc2626;font-weight:700;background:#fef2f2;padding:2px 6px;border-radius:6px}
.item-btn{display:flex;align-items:center;justify-content:space-between;padding:1rem;width:100%;cursor:pointer;font-family:inherit}
.item-icon-wrap{background:var(--secondary);padding:.625rem;border-radius:.75rem;transition:all .2s;display:flex;align-items:center;justify-content:center}
.item-btn:hover .item-icon-wrap{background:var(--primary);color:#fff}
.flex{display:flex}.items-center{align-items:center}.gap-1{gap:.25rem}.gap-2{gap:.5rem}.gap-3{gap:.75rem}.gap-4{gap:1rem}
.flex-1{flex:1}.mt-auto{margin-top:auto}.mb-2{margin-bottom:.5rem}.mb-4{margin-bottom:1rem}.mb-6{margin-bottom:1.5rem}.mb-8{margin-bottom:2rem}
.mt-3{margin-top:.75rem}.mt-8{margin-top:2rem}.mt-10{margin-top:2.5rem}.mt-12{margin-top:3rem}.py-8{padding-top:2rem;padding-bottom:2rem}.py-12{padding-top:3rem;padding-bottom:3rem}
.space-y-3>*+*{margin-top:.75rem}.space-y-4>*+*{margin-top:1rem}.space-y-6>*+*{margin-top:1.5rem}.space-y-8>*+*{margin-top:2rem}.space-y-12>*+*{margin-top:3rem}
.text-xs{font-size:.75rem}.text-sm{font-size:.875rem}.text-lg{font-size:1.125rem}.text-xl{font-size:1.25rem}.text-2xl{font-size:1.5rem}.text-3xl{font-size:1.875rem}.text-4xl{font-size:2.25rem}
.font-bold{font-weight:700}.font-black{font-weight:900}.text-zinc-400{color:#a1a1aa}.text-zinc-500{color:#71717a}.text-zinc-900{color:#18181b}
.tracking-tight{letter-spacing:-.025em}.leading-tight{line-height:1.25}
.mission-icon{font-size:1.5rem;transition:all .5s}
.mission-done{filter:none;transform:scale(1.1)}
.mission-pending{filter:grayscale(1);opacity:.3}
svg{display:inline-block;vertical-align:middle}

.progress-dots{display:flex;gap:.5rem;justify-content:center;margin-top:3rem}
.dot{height:6px;border-radius:9999px;transition:all .3s}
.dot-active{width:2rem;background:var(--primary)}
.dot-inactive{width:6px;background:#e4e4e7}
.quiz-option{padding:1rem;border-radius:.75rem;border:1px solid var(--border);font-weight:700;font-size:1rem;text-align:left;cursor:pointer;font-family:inherit;background:#fff;transition:all .2s;display:flex;align-items:center;justify-content:space-between;width:100%}
.quiz-correct{background:#f0fdf4;border-color:#bbf7d0;color:#14532d}
.quiz-wrong{background:#fef2f2;border-color:#fecaca;color:#7f1d1d}
.feedback-box{margin-top:1.5rem;padding:1rem;background:var(--secondary);border-radius:.75rem;border:1px solid #f4f4f5;font-size:.875rem;font-weight:500;color:#52525b;font-style:italic;line-height:1.6}
</style>
</head>
<body>
<div class="app" id="app"></div>

<script>
/* ==================== DATA & PROGRESS ==================== */
{CONTENT}
{LESSONS}
{WORLDS}
{SVG}

let profile = JSON.parse(localStorage.getItem('fin_profile')||'null');
let progress = JSON.parse(localStorage.getItem('fin_progress')||'[]');

/* === DUOLINGO CORE BARU === */
let streak = 0;
let xp = 0;
let userLevel = 1;
let lastLoginDate = null;
let currentWorld = null;
let currentLevel = null;

/* Load & update streak + XP */
function loadCoreProgress() {
  const today = new Date().toDateString();
  lastLoginDate = localStorage.getItem('fin_lastlogin');
  streak = parseInt(localStorage.getItem('fin_streak')||'0');
  xp = parseInt(localStorage.getItem('fin_xp')||'0');
  userLevel = Math.floor(xp / 250) + 1;

  if (lastLoginDate !== today) {
    const yesterday = new Date(Date.now() - 86400000).toDateString();
    if (lastLoginDate === yesterday) streak++;
    else streak = 1;
    localStorage.setItem('fin_streak', streak);
    localStorage.setItem('fin_lastlogin', today);
  }
}
function addXP(amount) {
  xp += amount;
  userLevel = Math.floor(xp / 250) + 1;
  localStorage.setItem('fin_xp', xp);
}

/* ==================== IMPROVED MASCOT ==================== */
function mascot(expr, size, cls='') {
  let animClass = 'mascot-bob';
  let src = 'moni-neutral.png';

  if (expr === 'happy' || expr === 'excited') {
    animClass = expr === 'excited' ? 'mascot-excited' : 'mascot-wiggle';
    src = 'moni-happy.png';
  } else if (expr === 'sad') {
    src = 'moni-sad.png';
  } else if (expr === 'proud') {
    animClass = 'mascot-proud';
    src = 'moni-happy.png';
  } else if (expr === 'thinking') {
    src = 'moni-neutral.png';
  }

  return `
    <div class="mascot-wrap ${cls}" style="width:${size}px;height:${size}px">
      <div class="mascot-shadow"></div>
      <div class="${animClass}" style="width:100%;height:100%">
        <img src="public/assets/${src}" alt="Moni" style="width:100%;height:100%;object-fit:contain;mix-blend-mode:multiply">
      </div>
    </div>`;
}

/* ==================== RENDER HEADER DASHBOARD ==================== */
function renderDashboardHeader() {
  return `
  <div class="dashboard-header">
    <div class="streak">
      🔥 <span class="streak-flame">${streak}</span> 
      <span style="font-size:0.95rem;margin-left:4px">hari streak</span>
    </div>
    <div class="xp-container">
      <div class="level-badge">Lv.${userLevel}</div>
      <div class="xp-bar"><div class="xp-fill" style="width:${Math.min(((xp % 250)/250)*100,100)}%"></div></div>
      <span style="font-weight:700;font-size:0.95rem">${xp % 250}/250</span>
    </div>
  </div>`;
}

/* ==================== RENDER UTAMA (dengan perubahan) ==================== */
function render() {
  loadCoreProgress(); // selalu update dulu
  const app = document.getElementById('app');
  if(!profile){renderOnboarding();return}
  if(!currentWorld){renderWorldMap();return}
  if(!currentLevel){renderLevelPath();return}
  renderLevel();
}

/* World Map dengan dashboard + mascot greeting */
function renderWorldMap() {
  const app = document.getElementById('app');
  const greeting = streak >= 7 ? 'Kamu gila! 🔥' : streak >= 3 ? 'Luar biasa!' : 'Semangat Moni!';
  
  let html = `<div class="screen py-8">${renderDashboardHeader()}`;
  html += `<div class="text-center mb-8">${mascot(streak >= 5 ? 'excited' : 'happy', 140)}</div>`;
  html += `<div class="text-center"><h1 class="mb-1">Halo, Pejuang!</h1><p style="color:#3b82f6;font-weight:700">${greeting} Streak ${streak} hari</p></div>`;
  html += `<div class="grid-1 mt-10">`;
  
  WORLDS.forEach((w,i) => {
    const locked = i > 0;
    html += `<button class="world-card" onclick="${locked ? '' : `selectWorld('${w.id}')`}">
      <div style="flex:1;text-align:left">
        <div class="label mb-2">Chapter ${i+1}</div>
        <div style="font-size:1.5rem" class="font-bold text-zinc-900 mb-2">${w.name}</div>
        <div class="text-sm text-zinc-500">${w.sub}</div>
      </div>
      <span class="emoji">${w.emoji}</span>
      ${locked ? `<div class="lock-overlay">${SVG.lock}</div>` : ''}
    </button>`;
  });
  html += `</div></div>`;
  app.innerHTML = html;
}

/* Quiz dengan HEARTS */
let qIdx = 0, qSelected = null, qFeedback = false, qScore = 0, currentHearts = 3;

function resetQuiz(){ qIdx=0; qSelected=null; qFeedback=false; qScore=0; currentHearts=3; }

function renderQuiz(){
  const app = document.getElementById('app');
  const questions = CONTENT[currentLevel][profile.persona];
  const q = questions[qIdx];

  let html = `<div class="screen card" style="padding:2rem;min-height:600px;display:flex;flex-direction:column">`;
  html += `<div class="flex" style="justify-content:space-between;margin-bottom:1.5rem"><div class="label">Pertanyaan ${qIdx+1}/${questions.length}</div>`;
  html += `<div class="hearts">${'❤️'.repeat(currentHearts)}</div></div>`;

  html += `<div style="flex:1">${mascot(qFeedback ? (q.options.find(o=>o.id===qSelected)?.isCorrect ? 'excited' : 'sad') : 'thinking', 130, 'mb-6')}</div>`;
  
  html += `<h2 class="text-center mb-8">${q.text}</h2><div class="grid-1">`;
  
  q.options.forEach(o => {
    let cls = 'quiz-option';
    if(qFeedback){
      if(o.isCorrect) cls += ' quiz-correct';
      else if(qSelected===o.id && !o.isCorrect) cls += ' quiz-wrong';
      else cls += ' quiz-dim';
    }
    html += `<button class="${cls}" onclick="quizSelect('${o.id}')" ${qFeedback?'disabled':''}>${o.text}</button>`;
  });
  
  if(qFeedback){
    const fb = q.options.find(o=>o.id===qSelected)?.feedback;
    html += `<div class="feedback-box">"${fb}"</div>`;
  }
  
  html += `</div><button class="btn mt-8" onclick="quizNext()" ${qFeedback?'':'disabled'}>${qIdx<questions.length-1?'Lanjut':'Selesai'} →</button></div>`;
  app.innerHTML = html;
}

function quizSelect(id){
  if(qFeedback) return;
  qSelected = id; qFeedback = true;
  const q = CONTENT[currentLevel][profile.persona][qIdx];
  if(q.options.find(o=>o.id===id)?.isCorrect){
    qScore++;
    addXP(20); // XP tiap jawaban benar
  } else {
    currentHearts--;
  }
  renderQuiz();
}

function quizNext(){
  if(currentHearts <= 0){
    alert("💔 Nyawa habis! Coba lagi besok atau ulangi lesson ini.");
    resetQuiz();
    currentLevel = null;
    render();
    return;
  }
  const questions = CONTENT[currentLevel][profile.persona];
  if(qIdx < questions.length-1){
    qIdx++; qSelected=null; qFeedback=false;
    renderQuiz();
  } else {
    addXP(100); // bonus selesai lesson
    resetQuiz();
    completeLevel();
  }
}

/* Complete level */
function completeLevel(){
  if(currentLevel && !progress.includes(currentLevel)){
    progress.push(currentLevel);
    localStorage.setItem('fin_progress', JSON.stringify(progress));
  }
  currentLevel = null;
  render();
}

{ONBOARDING}
{LEVELPATH}
{LEVELROUTER}
{PLACEHOLDER}
{BARTER}
{LIFECLOCK}

render(); // START
</script>
</body>
</html>
"""

final_html = new_html.replace('{CONTENT}', content_match.group(1)) \
    .replace('{LESSONS}', lessons_match.group(1)) \
    .replace('{WORLDS}', worlds_match.group(1)) \
    .replace('{SVG}', svg_match.group(1)) \
    .replace('{ONBOARDING}', onboarding_match.group(1)) \
    .replace('{LEVELPATH}', levelpath_match.group(1)) \
    .replace('{LEVELROUTER}', levelrouter_match.group(1)) \
    .replace('{PLACEHOLDER}', placeholder_match.group(1)) \
    .replace('{BARTER}', barter_match.group(1)) \
    .replace('{LIFECLOCK}', lifeclock_match.group(1))

with open(r'c:\Users\Windows\Desktop\application\index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
