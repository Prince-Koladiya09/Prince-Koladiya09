<style>
/* General Styling /
.profile-container {
font-family: 'Inter', sans-serif;
color: #f0f2f5; / Light grey text /
background: linear-gradient(135deg, #1a202c, #2d3748); / Dark gradient background /
padding: 20px;
border-radius: 15px;
box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
text-align: center;
overflow: hidden; / Ensures animations don't spill */
}

/* Header Section /
.header-section {
padding: 30px 0;
margin-bottom: 30px;
background: linear-gradient(45deg, #667eea, #764ba2); / Purple-blue gradient */
border-radius: 10px;
position: relative;
overflow: hidden;
animation: fadeIn 1.5s ease-out;
}

.header-section h1 {
font-size: 3.5em; /* Larger font for impact */
font-weight: 900;
color: #ffffff;
margin-bottom: 10px;
text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
animation: slideInLeft 1s ease-out;
}

.header-section p {
font-size: 1.2em;
color: #e2e8f0;
animation: slideInRight 1s ease-out 0.3s; /* Delayed animation */
}

/* Animated Text Effect */
@keyframes slideInLeft {
from { transform: translateX(-100%); opacity: 0; }
to { transform: translateX(0); opacity: 1; }
}

@keyframes slideInRight {
from { transform: translateX(100%); opacity: 0; }
to { transform: translateX(0); opacity: 1; }
}

@keyframes fadeIn {
from { opacity: 0; }
to { opacity: 1; }
}

/* Skills Section */
.skills-section {
margin-bottom: 30px;
}

.skills-section h2 {
font-size: 2em;
color: #a0aec0; /* Lighter grey */
margin-bottom: 20px;
position: relative;
display: inline-block;
}

.skills-section h2::after {
content: '';
display: block;
width: 60%;
height: 3px;
background: #4299e1; /* Blue accent */
margin: 10px auto 0;
border-radius: 5px;
}

.skill-badges {
display: flex;
flex-wrap: wrap;
justify-content: center;
gap: 15px;
}

.skill-badge {
transition: transform 0.3s ease, box-shadow 0.3s ease;
border-radius: 8px;
overflow: hidden;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.skill-badge:hover {
transform: translateY(-5px) scale(1.05);
box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
}

/* Project Section */
.projects-section {
margin-bottom: 30px;
}

.projects-section h2 {
font-size: 2em;
color: #a0aec0;
margin-bottom: 20px;
position: relative;
display: inline-block;
}

.projects-section h2::after {
content: '';
display: block;
width: 60%;
height: 3px;
background: #ed8936; /* Orange accent */
margin: 10px auto 0;
border-radius: 5px;
}

.project-item {
background-color: #2d3748; /* Slightly lighter dark background */
border-radius: 10px;
padding: 20px;
margin-bottom: 15px;
text-align: left;
transition: transform 0.3s ease, background-color 0.3s ease;
border: 1px solid #4a5568;
}

.project-item:hover {
transform: translateY(-5px);
background-color: #4a5568; /* Darker on hover */
}

.project-item h3 {
font-size: 1.5em;
color: #4299e1; /* Blue for project titles */
margin-bottom: 5px;
}

.project-item p {
font-size: 1em;
color: #cbd5e0; /* Light grey for description */
}

.project-item a {
color: #9f7aea; /* Purple for links */
text-decoration: none;
font-weight: bold;
transition: color 0.2s ease;
}

.project-item a:hover {
color: #b794f4;
text-decoration: underline;
}

/* Stats Section (Optional - requires GitHub Actions) */
.stats-section {
margin-bottom: 30px;
}

.stats-section h2 {
font-size: 2em;
color: #a0aec0;
margin-bottom: 20px;
position: relative;
display: inline-block;
}

.stats-section h2::after {
content: '';
display: block;
width: 60%;
height: 3px;
background: #ecc94b; /* Yellow accent */
margin: 10px auto 0;
border-radius: 5px;
}

.stats-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
gap: 20px;
justify-content: center;
}

.stat-card {
background-color: #2d3748;
border-radius: 10px;
padding: 20px;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
transition: transform 0.3s ease, box-shadow 0.3s ease;
border: 1px solid #4a5568;
}

.stat-card:hover {
transform: translateY(-5px);
box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
}

/* Footer */
.footer-section {
margin-top: 40px;
padding-top: 20px;
border-top: 1px solid #4a5568;
font-size: 0.9em;
color: #a0aec0;
}

.footer-section a {
color: #9f7aea;
text-decoration: none;
font-weight: bold;
}

.footer-section a:hover {
text-decoration: underline;
}
</style>

<div class="profile-container">
<div class="header-section">
<h1>Hi there, I'm Prince Koladiya! 👋</h1>
<p>Highly motivated Computer Science student passionate about AI/ML & Software Engineering.</p>
</div>

<div class="skills-section">
<h2>Skills & Technologies</h2>
<div class="skill-badges">
<!-- You can use popular badge services or custom SVGs -->
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3776AB%3Fstyle%3Dfor-the-badge%26logo%3Dpython%26logoColor%3Dwhite" class="skill-badge" alt="Python">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/JavaScript-F7DF1E%3Fstyle%3Dfor-the-badge%26logo%3Djavascript%26logoColor%3Dblack" class="skill-badge" alt="JavaScript">
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" class="skill-badge" alt="TensorFlow">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Keras-D00000%3Fstyle%3Dfor-the-badge%26logo%3Dkeras%26logoColor%3Dwhite" class="skill-badge" alt="Keras">
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" class="skill-badge" alt="PyTorch">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Flask-000000%3Fstyle%3Dfor-the-badge%26logo%3Dflask%26logoColor%3Dwhite" class="skill-badge" alt="Flask">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/HTML5-E34F26%3Fstyle%3Dfor-the-badge%26logo%3Dhtml5%26logoColor%3Dwhite" class="skill-badge" alt="HTML5">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/CSS3-1572B6%3Fstyle%3Dfor-the-badge%26logo%3Dcss3%26logoColor%3Dwhite" class="skill-badge" alt="CSS3">
<img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" class="skill-badge" alt="Supabase">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Git-F05032%3Fstyle%3Dfor-the-badge%26logo%3Dgit%26logoColor%3Dwhite" class="skill-badge" alt="Git">
</div>
</div>

<div class="projects-section">
<h2>Featured Projects</h2>
<div class="project-item">
<h3>IMDB Sentiment Analysis: Baseline to Transformers</h3>
<p>Engineered a comprehensive 10-step ML pipeline for sentiment analysis on IMDB reviews. Benchmarked traditional models against advanced RNN (LSTM) and state-of-the-art Transformer (DistilBERT) architectures, achieving superior accuracy. Utilized LIME for model interpretability and performed qualitative error analysis.</p>
<a href="https://www.google.com/search?q=https://github.com/Prince-Koladiya09/YOUR_IMDB_REPO" target="_blank">View Project on GitHub</a>
</div>
<div class="project-item">
<h3>Sorting Algorithm Visualizer</h3>
<p>A web-based interactive visualizer for sorting algorithms (Merge, Quick, Selection Sort). Dynamically generates arrays, animates the sorting process with visual cues and sound effects, and provides a performance graph comparing complexities.</p>
<a href="https://sortexplorer.netlify.app/" target="_blank">Explore Live Demo</a>
</div>
<!-- Add more projects here -->
</div>

<div class="stats-section">
<h2>My GitHub Stats</h2>
<div class="stats-grid">
<!-- GitHub Stats Card (requires external service like GitHub Readme Stats) -->
<div class="stat-card">
<img src="https://www.google.com/search?q=https://github-readme-stats.vercel.app/api%3Fusername%3DPrince-Koladiya09%26show_icons%3Dtrue%26theme%3Ddark%26hide_border%3Dtrue%26count_private%3Dtrue" alt="Prince's GitHub Stats"/>
</div>
<!-- Top Languages Card -->
<div class="stat-card">
<img src="https://www.google.com/search?q=https://github-readme-stats.vercel.app/api/top-langs/%3Fusername%3DPrince-Koladiya09%26layout%3Dcompact%26theme%3Ddark%26hide_border%3Dtrue" alt="Top Languages"/>
</div>
</div>
</div>

<div class="footer-section">
<p>Connect with me on <a href="https://www.google.com/search?q=https://linkedin.com/in/prince-koladiya-47782727a" target="_blank">LinkedIn</a> or explore more on my <a href="https://github.com/Prince-Koladiya09" target="_blank">GitHub profile</a>.</p>
</div>
</div>
