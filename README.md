<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Prince Koladiya · Tech profile</title>
    <!-- Font & icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700;800&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: #050510;
            font-family: 'JetBrains Mono', monospace;
            color: #c9d1d9;
            line-height: 1.6;
            padding: 2rem 1rem;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* matrix rain canvas – gentle tech backdrop */
        #matrix-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            pointer-events: none;
            opacity: 0.15;
        }

        .container {
            max-width: 1100px;
            width: 100%;
            background: rgba(5, 5, 16, 0.75);
            backdrop-filter: blur(2px);
            border-radius: 32px;
            padding: 2rem 2.5rem;
            position: relative;
            z-index: 2;
            border: 1px solid rgba(0, 217, 255, 0.08);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.8);
        }

        /* ----- header / waving capsule (gentle) ----- */
        .capsule-header {
            text-align: center;
            margin-bottom: 2rem;
            position: relative;
        }

        .capsule-header h1 {
            font-size: 4rem;
            font-weight: 800;
            background: linear-gradient(135deg, #00D9FF 0%, #3a7bd5 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.02em;
            text-shadow: 0 0 30px rgba(0, 217, 255, 0.2);
            margin-bottom: 0.3rem;
        }

        .capsule-header .sub {
            font-size: 1.1rem;
            color: #8b9bb5;
            letter-spacing: 2px;
            display: flex;
            justify-content: center;
            gap: 1.2rem;
            flex-wrap: wrap;
        }

        .capsule-header .sub span {
            background: rgba(0, 217, 255, 0.06);
            padding: 0.2rem 1.2rem;
            border-radius: 40px;
            border: 1px solid rgba(0, 217, 255, 0.1);
        }

        .typing-wrapper {
            margin: 1.2rem 0 0.8rem;
            font-size: 1.2rem;
            color: #00D9FF;
            font-weight: 600;
            min-height: 2.8rem;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 1.2rem;
            margin-top: 1.2rem;
        }

        .social-links a {
            color: #c9d1d9;
            font-size: 1.8rem;
            transition: 0.2s ease;
            border-radius: 50%;
            width: 48px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.04);
        }

        .social-links a:hover {
            color: #00D9FF;
            border-color: #00D9FF;
            background: rgba(0, 217, 255, 0.06);
            transform: translateY(-2px);
        }

        /* ----- sections ----- */
        .section-title {
            font-size: 1.6rem;
            font-weight: 700;
            margin: 2.2rem 0 1.2rem 0;
            color: #00D9FF;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            border-bottom: 1px solid rgba(0, 217, 255, 0.15);
            padding-bottom: 0.4rem;
        }

        .section-title i {
            font-size: 1.4rem;
            opacity: 0.8;
        }

        .code-block {
            background: rgba(0, 217, 255, 0.03);
            border-left: 3px solid #00D9FF;
            padding: 1.2rem 1.6rem;
            border-radius: 16px;
            font-size: 0.95rem;
            margin: 1rem 0 1.5rem 0;
            overflow-x: auto;
            white-space: pre-wrap;
            word-break: break-word;
            color: #b0c4de;
            border: 1px solid rgba(0, 217, 255, 0.08);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }

        .code-block .kw { color: #00D9FF; }
        .code-block .str { color: #ffb86b; }
        .code-block .fn { color: #8be9fd; }
        .code-block .cmt { color: #6272a4; }

        /* experience cards */
        .exp-grid {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            margin: 1rem 0;
        }

        .exp-card {
            background: rgba(255, 255, 255, 0.02);
            border-radius: 20px;
            padding: 1.5rem 1.8rem;
            border: 1px solid rgba(0, 217, 255, 0.06);
            transition: 0.2s;
        }

        .exp-card:hover {
            border-color: rgba(0, 217, 255, 0.2);
            background: rgba(0, 217, 255, 0.02);
        }

        .exp-card h3 {
            font-size: 1.3rem;
            color: #e6edf3;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }

        .exp-card h3 small {
            font-weight: 400;
            font-size: 0.9rem;
            color: #8b9bb5;
        }

        .exp-metrics {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem 2rem;
            margin: 0.8rem 0 0.6rem;
            font-size: 0.9rem;
            background: rgba(0, 0, 0, 0.2);
            padding: 0.6rem 1rem;
            border-radius: 40px;
        }

        .exp-metrics span {
            color: #8be9fd;
        }

        .exp-metrics i {
            color: #00D9FF;
            margin-right: 0.3rem;
        }

        .tech-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem 0.7rem;
            margin-top: 0.8rem;
        }

        .tech-tags span {
            background: rgba(0, 217, 255, 0.06);
            padding: 0.15rem 1rem;
            border-radius: 40px;
            font-size: 0.75rem;
            border: 1px solid rgba(0, 217, 255, 0.08);
            color: #b0c4de;
        }

        /* skill icons */
        .skill-group {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem 1rem;
            margin: 0.4rem 0 0.8rem;
            align-items: center;
        }

        .skill-group img {
            height: 32px;
            filter: drop-shadow(0 0 6px rgba(0,217,255,0.1));
        }

        .badge-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 0.5rem 0;
        }

        .badge-stack .badge {
            background: rgba(0, 217, 255, 0.06);
            padding: 0.2rem 1.2rem;
            border-radius: 30px;
            font-size: 0.8rem;
            border: 1px solid rgba(0, 217, 255, 0.1);
            color: #b0c4de;
            transition: 0.1s;
        }

        .badge-stack .badge i {
            margin-right: 0.3rem;
            color: #00D9FF;
        }

        /* project cards */
        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.5rem;
            margin: 1rem 0;
        }

        .project-card {
            background: rgba(255, 255, 255, 0.02);
            border-radius: 20px;
            padding: 1.5rem;
            border: 1px solid rgba(0, 217, 255, 0.05);
            transition: 0.2s;
        }

        .project-card:hover {
            border-color: rgba(0, 217, 255, 0.2);
            transform: translateY(-4px);
            background: rgba(0, 217, 255, 0.02);
        }

        .project-card h4 {
            color: #e6edf3;
            font-size: 1.1rem;
            display: flex;
            justify-content: space-between;
        }

        .project-card h4 i {
            color: #00D9FF;
        }

        .project-card p {
            font-size: 0.9rem;
            color: #8b9bb5;
            margin: 0.6rem 0;
        }

        .project-card .tech {
            font-size: 0.7rem;
            opacity: 0.7;
            letter-spacing: 0.5px;
        }

        .project-card .link-icon {
            color: #00D9FF;
            margin-top: 0.6rem;
            display: inline-block;
        }

        /* matrix table */
        .matrix-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
        }

        .matrix-table td {
            padding: 0.6rem 0.8rem;
            border-bottom: 1px solid rgba(255,255,255,0.02);
        }

        .matrix-table .stars {
            color: #00D9FF;
            letter-spacing: 2px;
        }

        .matrix-table tr:last-child td {
            border-bottom: none;
        }

        /* footer */
        .footer-note {
            text-align: center;
            margin-top: 2.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(0, 217, 255, 0.06);
            color: #6272a4;
            font-size: 0.9rem;
        }

        .footer-note i {
            color: #00D9FF;
        }

        @media (max-width: 640px) {
            .container { padding: 1.5rem; }
            .capsule-header h1 { font-size: 2.8rem; }
        }
    </style>
</head>
<body>

    <!-- Matrix rain background (gentle) -->
    <canvas id="matrix-bg"></canvas>

    <div class="container">

        <!-- HEADER -->
        <div class="capsule-header">
            <h1>Prince Koladiya</h1>
            <div class="sub">
                <span><i class="fas fa-brain" style="color:#00D9FF;"></i> ML Engineer</span>
                <span><i class="fas fa-chart-line" style="color:#00D9FF;"></i> Data Scientist</span>
                <span><i class="fas fa-cogs" style="color:#00D9FF;"></i> Backend Dev</span>
            </div>
            <div class="typing-wrapper">
                <i class="fas fa-terminal" style="color:#00D9FF; opacity:0.6; margin-right:6px;"></i>
                <span id="typing-text"></span>
            </div>
            <div class="social-links">
                <a href="#"><i class="fab fa-linkedin-in"></i></a>
                <a href="#"><i class="fab fa-github"></i></a>
                <a href="#"><i class="fas fa-envelope"></i></a>
            </div>
        </div>

        <!-- whoami -->
        <div class="section-title"><i class="fas fa-code"></i> whoami</div>
        <div class="code-block">
            <span class="kw">class</span> <span class="fn">PrinceKoladiya</span>:

            <span class="kw">def</span> <span class="fn">__init__</span>(<span class="kw">self</span>):
                <span class="kw">self</span>.name        = <span class="str">"Prince Koladiya"</span>
                <span class="kw">self</span>.origin      = <span class="str">"India 🇮🇳"</span>
                <span class="kw">self</span>.role        = [<span class="str">"Backend Developer"</span>, <span class="str">"AI/ML Engineer"</span>]
                <span class="kw">self</span>.superpowers = [
                    <span class="str">"Shipping production backend systems"</span>,
                    <span class="str">"LLM-powered / RAG applications"</span>,
                    <span class="str">"Scalable REST APIs & microservices"</span>,
                ]
                <span class="kw">self</span>.current_quest = {
                    <span class="str">"learning"</span>      : [<span class="str">"Agentic AI"</span>, <span class="str">"Advanced RAG"</span>],
                    <span class="str">"building"</span>      : <span class="str">"AI-first, production-grade products"</span>,
                    <span class="str">"program"</span>       : <span class="str">"Amazon ML Summer School 2026"</span>,
                }
        </div>

        <!-- experience -->
        <div class="section-title"><i class="fas fa-briefcase"></i> experience · detailed</div>
        <div class="exp-grid">
            <div class="exp-card">
                <h3>⚙️ Backend Developer @ YouthQit <small>Remote, India · 2026 – Present</small></h3>
                <div class="exp-metrics">
                    <span><i class="fas fa-coins"></i> ₹9.5L+ revenue tracked</span>
                    <span><i class="fas fa-box"></i> 560+ units sold</span>
                    <span><i class="fas fa-shopping-cart"></i> 40+ orders / 3mo</span>
                    <span><i class="fas fa-store"></i> Live client: Raghav Enterprises</span>
                </div>
                <ul style="margin-left:1.2rem; color:#b0c4de; font-size:0.9rem; list-style-type:'▸ ';">
                    <li>Architected B2B wholesale platform (Play Store + App Store)</li>
                    <li>Reports & Analytics with SKU breakdown & Excel export</li>
                    <li>Firebase Phone OTP + JWT RBAC (admin/seller/buyer)</li>
                    <li>AWS Lightsail · S3 · PDFKit · CI/CD</li>
                </ul>
                <div class="tech-tags">
                    <span>Node.js</span><span>Express</span><span>MongoDB</span><span>AWS</span><span>JWT</span><span>Firebase</span>
                </div>
            </div>
        </div>

        <!-- tech stack -->
        <div class="section-title"><i class="fas fa-microchip"></i> tech · stack</div>
        <div style="display:flex; flex-wrap:wrap; gap:1.2rem 2rem; margin:0.6rem 0 0.8rem;">
            <div><span style="color:#00D9FF;">AI · ML · NLP</span>
                <div class="skill-group">
                    <img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow&theme=dark" />
                </div>
                <div class="badge-stack">
                    <span class="badge"><i class="fas fa-code"></i> LangChain</span>
                    <span class="badge"><i class="fas fa-code"></i> LangGraph</span>
                    <span class="badge"><i class="fas fa-code"></i> Scikit-Learn</span>
                    <span class="badge"><i class="fas fa-code"></i> HuggingFace</span>
                    <span class="badge"><i class="fas fa-code"></i> FAISS</span>
                </div>
            </div>
            <div><span style="color:#00D9FF;">Backend · APIs</span>
                <div class="skill-group">
                    <img src="https://skillicons.dev/icons?i=nodejs,express,fastapi,react,ts&theme=dark" />
                </div>
                <div class="badge-stack">
                    <span class="badge"><i class="fas fa-cloud"></i> REST</span>
                    <span class="badge"><i class="fas fa-cloud"></i> GraphQL</span>
                    <span class="badge"><i class="fas fa-cloud"></i> JWT</span>
                    <span class="badge"><i class="fas fa-cloud"></i> RabbitMQ</span>
                </div>
            </div>
            <div><span style="color:#00D9FF;">DB · Cloud · DevOps</span>
                <div class="skill-group">
                    <img src="https://skillicons.dev/icons?i=mongodb,mysql,postgres,redis,aws,docker,git&theme=dark" />
                </div>
            </div>
        </div>

        <!-- projects -->
        <div class="section-title"><i class="fas fa-rocket"></i> git log --exciting-projects</div>
        <div class="project-grid">
            <div class="project-card"><h4>PairEdge <i class="fas fa-code"></i></h4><p>Real-time collaborative coding & interview prep platform with WebSocket sync.</p><div class="tech">Node.js · React · MongoDB · WebSockets</div><a href="#" class="link-icon"><i class="fab fa-github"></i> repo</a></div>
            <div class="project-card"><h4>InkSpace <i class="fas fa-microservices"></i></h4><p>11 microservices CMS with RabbitMQ, Elasticsearch, circuit breaker.</p><div class="tech">Node.js · Next.js · RabbitMQ · Docker</div><a href="#" class="link-icon"><i class="fab fa-github"></i> repo</a></div>
            <div class="project-card"><h4>Demand Forecast <i class="fas fa-chart-line"></i></h4><p>LSTM quantile regression + newsvendor inventory optimization.</p><div class="tech">PyTorch · Pandas · SciPy</div><a href="#" class="link-icon"><i class="fab fa-github"></i> repo</a></div>
            <div class="project-card"><h4>Resume Screener <i class="fas fa-file-alt"></i></h4><p>AI-powered candidate matching with RAG + LLM scoring.</p><div class="tech">FastAPI · LangChain · FAISS · OpenAI</div><a href="#" class="link-icon"><i class="fab fa-github"></i> repo</a></div>
            <div class="project-card"><h4>MF Analyst <i class="fas fa-chart-pie"></i></h4><p>Mutual fund analytics dashboard with NAV, CAGR, XIRR.</p><div class="tech">Python · Pandas · Streamlit</div><a href="#" class="link-icon"><i class="fab fa-github"></i> repo</a></div>
            <div class="project-card"><h4>B2B RFP Agent <i class="fas fa-robot"></i></h4><p>Agentic RAG system for drafting proposal responses.</p><div class="tech">LangGraph · FAISS · FastAPI · LLMs</div><a href="#" class="link-icon"><i class="fab fa-github"></i> repo</a></div>
            <div class="project-card"><h4>SnipURL <i class="fas fa-link"></i></h4><p>Full-stack URL shortener with analytics, OAuth, AWS infra.</p><div class="tech">React · Node.js · MongoDB · AWS</div><a href="#" class="link-icon"><i class="fab fa-github"></i> repo</a></div>
        </div>

        <!-- expertise matrix -->
        <div class="section-title"><i class="fas fa-th"></i> expertise · matrix</div>
        <table class="matrix-table">
            <tr><td>🔧 Backend & API Design</td><td class="stars">⭐⭐⭐⭐⭐</td><td style="color:#8b9bb5;">Node, Express, FastAPI, REST, GraphQL</td></tr>
            <tr><td>☁️ Cloud & DevOps</td><td class="stars">⭐⭐⭐⭐⭐</td><td style="color:#8b9bb5;">AWS, Docker, CI/CD</td></tr>
            <tr><td>🧠 Applied Deep Learning</td><td class="stars">⭐⭐⭐⭐</td><td style="color:#8b9bb5;">LSTM, RNN, Transformers, PyTorch</td></tr>
            <tr><td>🤖 LLMs & Agentic AI</td><td class="stars">⭐⭐⭐⭐</td><td style="color:#8b9bb5;">RAG, LangChain, LangGraph, FAISS</td></tr>
            <tr><td>🗄️ Databases</td><td class="stars">⭐⭐⭐⭐</td><td style="color:#8b9bb5;">MongoDB, MySQL, PostgreSQL, Redis</td></tr>
            <tr><td>🧱 Distributed Systems</td><td class="stars">⭐⭐⭐⭐</td><td style="color:#8b9bb5;">Microservices, event-driven, RabbitMQ</td></tr>
        </table>

        <!-- activity diagram (gentle ascii) -->
        <div class="section-title"><i class="fas fa-project-diagram"></i> github activity · diagram</div>
        <div style="background: rgba(0,217,255,0.03); border-radius: 20px; padding: 1rem 1.5rem; border: 1px solid rgba(0,217,255,0.06); font-size: 0.75rem; color:#8b9bb5; overflow-x:auto; font-family: monospace; white-space: pre-wrap; letter-spacing: 0.5px;">
            <span style="color:#00D9FF;">●</span> main ──┬─ <span style="color:#8be9fd;">feat/reports</span> ── <span style="color:#00D9FF;">●</span> merged  <span style="color:#6272a4;">#42</span>
                    ├─ <span style="color:#8be9fd;">bugfix/auth</span> ── <span style="color:#00D9FF;">●</span> merged  <span style="color:#6272a4;">#38</span>
                    ├─ <span style="color:#8be9fd;">ci/cd-pipeline</span> ── <span style="color:#00D9FF;">●</span> merged  <span style="color:#6272a4;">#55</span>
                    └─ <span style="color:#8be9fd;">experiment/llm</span> ── <span style="color:#00D9FF;">●</span> open     <span style="color:#6272a4;">#61</span>
            <span style="color:#6272a4;">[2026-08-11]  ·  active branches: 4  ·  commits: 128  ·  PRs: 7</span>
        </div>

        <!-- achievements -->
        <div class="section-title"><i class="fas fa-trophy"></i> achievements</div>
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem 1.2rem; margin-bottom:0.5rem;">
            <span style="background:rgba(0,217,255,0.05); padding:0.3rem 1.2rem; border-radius:40px; border:1px solid rgba(0,217,255,0.08);"><i class="fas fa-medal" style="color:#FFD700;"></i> Amazon ML Summer School 2026 · ~1%</span>
            <span style="background:rgba(0,217,255,0.05); padding:0.3rem 1.2rem; border-radius:40px; border:1px solid rgba(0,217,255,0.08);"><i class="fas fa-cloud" style="color:#00D9FF;"></i> AWS Certified Developer – Associate</span>
            <span style="background:rgba(0,217,255,0.05); padding:0.3rem 1.2rem; border-radius:40px; border:1px solid rgba(0,217,255,0.08);"><i class="fas fa-graduation-cap"></i> Full Tuition Waiver · PDEU</span>
        </div>

        <!-- footer -->
        <div class="footer-note">
            <i class="fas fa-terminal"></i>  Prince Koladiya · 2026  ·  <i class="fas fa-code"></i> built with ☕ &amp; focus
        </div>

    </div>

    <script>
        // Gentle matrix rain – tech background
        (function() {
            const canvas = document.getElementById('matrix-bg');
            const ctx = canvas.getContext('2d');
            let w, h, columns, drops = [];
            const chars = "0123456789ABCDEF".split("");

            function resize() {
                w = canvas.width = window.innerWidth;
                h = canvas.height = window.innerHeight;
                columns = Math.floor(w / 18);
                drops = Array(columns).fill(1);
            }
            window.addEventListener('resize', resize);
            resize();

            function draw() {
                ctx.fillStyle = 'rgba(5,5,16,0.035)';
                ctx.fillRect(0, 0, w, h);
                ctx.font = '16px monospace';
                ctx.fillStyle = '#00D9FF';
                for (let i = 0; i < drops.length; i++) {
                    const text = chars[Math.floor(Math.random() * chars.length)];
                    const x = i * 18;
                    const y = drops[i] * 18;
                    ctx.globalAlpha = 0.15 + Math.random() * 0.2;
                    ctx.fillText(text, x, y);
                    if (y > h && Math.random() > 0.975) {
                        drops[i] = 0;
                    }
                    drops[i] += 0.45 + Math.random() * 0.3;
                }
                requestAnimationFrame(draw);
            }
            draw();

            // typing effect
            const phrases = [
                "🔥 Turning raw data into intelligent systems",
                "🤖 LLMs · Agents · Transformers · RAG",
                "🌐 Node.js · FastAPI · PyTorch · AWS",
                "🎯 Shipping production backend systems",
                "🚀 CS Student → Building the Future"
            ];
            let idx = 0, charIdx = 0, isDeleting = false;
            const el = document.getElementById('typing-text');
            function type() {
                const current = phrases[idx];
                if (!isDeleting) {
                    el.textContent = current.slice(0, charIdx++);
                    if (charIdx > current.length) {
                        isDeleting = true;
                        setTimeout(type, 1800);
                        return;
                    }
                } else {
                    el.textContent = current.slice(0, charIdx--);
                    if (charIdx < 0) {
                        isDeleting = false;
                        idx = (idx + 1) % phrases.length;
                        setTimeout(type, 300);
                        return;
                    }
                }
                setTimeout(type, isDeleting ? 40 : 80);
            }
            type();
        })();
    </script>
</body>
</html>
