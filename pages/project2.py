import streamlit as st

st.set_page_config(page_title="Sales Dashboard", layout="centered")


st.title("ML System")
st.write("")

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "🚀 View Live App",
        "https://ads-multiplication-beeraboina-rahul-v2.streamlit.app/"
    )

with col2:
    st.link_button(
        "💻 View Source Code",
        "https://github.com/Rahul-2305/ADS-Automated-Multiplication"
    )
st.divider()
st.subheader("Tools Used")
st.text("Python, Streamlit, Excel")

st.divider()
st.subheader("Metrics")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Before Automation", value="20 - 25 Mins")
    st.caption("Manual time taken by an Analyst")

with col2:
    st.metric(label="After Automation", value="30 - 45 sec")
    st.caption("Application run-time")

with col3:
    st.metric(label="Performance Improvement", value="98%")
    st.caption("Percentage time reduced")

st.divider()

if st.button("⬅ Back"):
    st.switch_page("pages/Projects.py")

st.caption("© 2026 Beeraboina Rahul")
