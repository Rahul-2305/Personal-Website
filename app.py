import streamlit.components.v1 as components
import streamlit as st
import base64

st.set_page_config(page_title="Beeraboina Rahul", layout="wide")

# ---------- GLOBAL CSS (RESPONSIVE DESIGN) ----------
st.markdown("""
<style>

/* Remove Streamlit default padding */
.block-container {
    padding-top: 2rem;
}

/* Background */
.stApp {
    background-color: black;
    color: white;
}

/* Headings */
h1, h2, h3 {
    color: #00ff88;
}

/* ---------------- NAVBAR ---------------- */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background-color: black;
    display: flex;
    justify-content: center;
    gap: 40px;
    padding: 15px;
    border-bottom: 1px solid #00ff88;
}

.navbar a {
    text-decoration: none;
    color: white;
    font-weight: bold;
    transition: 0.3s;
}

.navbar a:hover {
    color: #00ff88;
}

/* -------------- HERO SECTION -------------- */
.hero {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 40px;
    padding: 40px 20px;
}

.hero img {
    width: 250px;
    border-radius: 15px;
}

/* -------------- TIMELINE -------------- */
.timeline {
    position: relative;
    margin-left: 20px;
    padding-left: 20px;
}

.timeline::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    border-left: 2px dashed #00ff88;
}

.timeline-item {
    margin-bottom: 30px;
}

/* -------------- RESPONSIVE BREAKPOINT -------------- */
@media (max-width: 768px) {
    .navbar {
        flex-wrap: wrap;
        gap: 15px;
    }

    .hero {
        flex-direction: column;
        text-align: center;
    }

    .hero img {
        width: 200px;
    }
}

</style>
""", unsafe_allow_html=True)

# ------------- NAVBAR -------------
st.markdown("""
<div class="navbar">
    <a href="#home">Home</a>
    <a href="#education">Education</a>
    <a href="#skills">Skills</a>
    <a href="#employment">Employment</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# ------------- HOME -------------


# Convert image to base64
with open("assets/profile.jpg", "rb") as img_file:
    encoded = base64.b64encode(img_file.read()).decode()

st.markdown("<a name='home'></a>", unsafe_allow_html=True)

st.markdown(f"""
<div class="hero">
    <img src="data:image/jpg;base64,{encoded}" />
    <div>
        <h1>Beeraboina Rahul</h1>
        <h3>Market Mix Modelling Analyst | Aspiring Data Scientist</h3>
        <p>
       A Data Science professional with 1.4 years of experience in Market Mix Modelling, specializing in multi-linear regression and performance analytics. 
       Complex marketing data is converted into clear, revenue-driving decisions, with a growing focus on advanced machine learning and scalable solutions.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<style>
div[data-testid="stPageLink"] a {
    background-color: black !important;
    color: #00ff88 !important;
    font-weight: 600;
    padding: 14px 24px;
    border-radius: 8px;
    text-align: center;
    display: block;
    border: 1px solid #00ff88;
    transition: all 0.3s ease;
}

div[data-testid="stPageLink"] a:hover {
    background-color: #00ff88 !important;
    color: black !important;
    transform: translateY(-3px);
}
</style>
""", unsafe_allow_html=True)

# --- Centered Button ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.page_link(
        "pages/Projects.py",
        label="🚀 View My Projects",
        use_container_width=True
    )


st.divider()

# ------------- EDUCATION -------------
st.markdown("<a name='education'></a>", unsafe_allow_html=True)
st.header("Education")

st.markdown("""
<div class="timeline">
    <div class="timeline-item">
        <h3>National Institute of Technology, Tiruchirappalli</h3>
        <p>B.Tech in Civil Engineering - 8.58</p> 
        <p>2020 - 2024</p>
    </div>
    <div class="timeline-item">
        <h3>12th - Chennai Public School</h3>
        <p>91.20%</p>
        <p>2020</p>
    </div>
    <div class="timeline-item">
        <h3>10th - Chinmaya Vidyalaya Anna Nagar West</h3>
        <p>89.00%</p>
        <p>2018</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()


# ------------- SKILLS -------------
st.markdown("<a name='skills'></a>", unsafe_allow_html=True)
st.header("Skills")

st.dataframe({
    "Category": ["Programming/Analytics", "Business Reporting", "AI & Machine Learning", "Other Tools"],
    "Skills/Tools": [
        "Python, SQL, Data Visualization, Multi-Linear Regression, EDA",
        "Power BI, Excel, Client Deck Creation, ROI & KPI Tracking",
        "Prompt Engineering, RAG-Based Systems, LLMs, Deep Learning, Model Evaluation",
        "Power Point, GitHub, VS Code, Jupyter Notebook"
    ]
}, use_container_width=True)

st.divider()


# ------------- EMPLOYMENT -------------
st.markdown("<a name='employment'></a>", unsafe_allow_html=True)
st.header("Employment")

st.markdown("""
<div class="timeline">
    <div class="timeline-item">
        <h3>Analyst @ Ipsos MMA</h3>
        <p><i>Bangalore, Karnatka</i></p>
        <p>Nov 2025 - Present</p>
        <li>Promoted to Analyst within a year for demonstrating strong analytical capability and taking full ownership of US and EMEA brand portfolios.</li>
        <li>Designed and deployed a Streamlit-based automation system that reduced multi-file Excel processing time by 95% (25 minutes → 45 seconds), improving reporting efficiency and scalability.</li>
    </div>
    <div class="timeline-item">
         <h3>Associate Analyst @ Ipsos MMA</h3>
        <p><i>Bangalore, Karnatka</i></p>
        <p>Oct 2024 - Oct 2025 (1 Yr 1 mos)</p>
       <li>Created client decks presenting key business KPIs such as ROI, Effectiveness, CPP, and Support to drive strategic decisions.</li>
       <li>Conducted Exploratory Data Analysis (EDA) on Own Brand & Competitor Data to analyze market share, sales units, revenue, and promotions.</li>
       <li>Ran multi-linear regression models to predict unit sales and forecast market trends.</li>
       <li>Worked on time-series data to analyze sales patterns and market fluctuations.</li>
       <li>Assisted in the optimization of marketing spend across various tactics to improve efficiency.</li>
       <li>Contributed to Market Mix Modeling (MMM) by evaluating the impact of marketing activities on business performance.</li>
       <li>Collaborated with clients, including Hanes (Retail) and McCormick (CPG), providing data-driven insights for better decision-making.</li>     
        <li> Utilized Python, Excel, PowerPoint for data analysis and business reporting.</li>
    </div>
     <div class="timeline-item">
     <h3>Machine Learning Intern @ National Institute of Technology, Tiruchirappalli</h3>
        <p><i>Tiruchirappalli, Tamil Nadu</i></p>
        <p>Jun 2023 - July 2023 (2 mos)</p>
       <li>Applied clustering and PCA to large datasets to uncover high-incidence patterns and improve trend visibility. </li>
       <li>Built interactive Excel dashboards and visualizations, reducing manual analysis time by 40%.</li>
       <li>Presented insights to non-technical stakeholders using clear data storytelling and business context.</li>         
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()


# ------------- CONTACT -------------
st.markdown("<a name='contact'></a>", unsafe_allow_html=True)
st.header("Contact")


components.html("""
<style>
body {
    margin: 0;
    padding: 0;
}

.social-container {
    display: flex;
    justify-content: center;
    gap: 25px;
    margin-top: 20px;
}

.social-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 12px 24px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    color: white;
    background-color: #111;
    border: 1px solid #333;
    transition: all 0.3s ease;
    font-family: Arial, sans-serif;
}

.social-btn:hover {
    background-color: #00ff88;
    color: black;
    transform: translateY(-3px);
}
</style>

<div class="social-container">

    <a href="mailto:rahulbeeraboina@example.com" class="social-btn">
        📧 Email
    </a>

    <a href="https://www.linkedin.com/in/beeraboina-rahul" target="_blank" class="social-btn">
        💼 LinkedIn
    </a>

    <a href="https://github.com/Rahul-2305/" target="_blank" class="social-btn">
        💻 GitHub
    </a>

</div>
""", height=120)

with open("assets/resume.pdf", "rb") as f:
    st.download_button(
        "Download Resume",
        f,
        file_name="Resume.pdf",
        use_container_width=True
    )

st.caption("© 2026 Beeraboina Rahul")
# st.write("📧 rahulbeeraboina@example.com")
