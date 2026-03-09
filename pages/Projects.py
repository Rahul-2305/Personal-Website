import streamlit as st

st.set_page_config(page_title="Projects", layout="centered")

# ---------------- THEME ----------------
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}

div.stButton > button {
    background-color: black;
    color: #00ff88;
    border: 1px solid #00ff88;
    border-radius: 8px;
    padding: 6px 14px;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #00ff88;
    color: black;
}
</style>
""", unsafe_allow_html=True)

st.title("Projects")

# ---------------- PROJECT LIST ----------------
projects = [
    {
        "title": "Automated Excel Multiplier System",
        "desc": "An automation tool that reduces manual time by 95%",
        "page": "pages/project1.py"
    },
    {
        "title": "ML Prediction Model",
        "desc": "Machine learning model for business forecasting.",
        "page": "pages/project2.py"
    },
    # Add more here freely
]

# ---------------- AUTO STACKING ----------------
for project in projects:
    with st.container(border=True):
        st.subheader(project["title"])
        st.write(project["desc"])

        if st.button("View Project", key=project["title"]):
            st.switch_page(project["page"])

        st.markdown("<br>", unsafe_allow_html=True)

if st.button("⬅ Back"):
    st.switch_page("app.py")


st.caption("© 2026 Beeraboina Rahul")
