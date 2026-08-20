import streamlit as st
import lists

data = {
    "Eligible":None
}


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

load_css("style.css")


st.title("[ Internship Recommendation Engine ✨⚙️ ]")
st.divider()


with st.form(key="form"):
    Eligible = st.checkbox("Are you Eligible?")
    state = st.multiselect("Preferred States",lists.location_list)
    sector = st.multiselect("Target Sectors",lists.sector_list)
    field = st.multiselect("Target Fields",lists.field_list)
    skills = st.text_area("Key Skills & Interests",placeholder="e.g., Python, Java, C++, AI, Machine Learning, Accounting, Computer Networking...")

    submitted = st.form_submit_button("Find Internships!")

