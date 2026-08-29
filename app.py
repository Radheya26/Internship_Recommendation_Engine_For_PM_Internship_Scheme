import streamlit as st
import pandas as pd 
import lists
import requests

backend_url = "http://127.0.0.1:8000/get_internship"

MATCH_THRESHOLD = 60

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

load_css("style.css")





st.title("[ Internship Recommendation Engine ✨⚙️ ]")
st.divider()


with st.form(key="form"):
    #Eligible = st.checkbox("Are you Eligible?")
    location = st.multiselect("Preferred Locations",lists.location_list)
    sector = st.multiselect("Target Sectors",lists.sector_list)
    field = st.multiselect("Target Fields",lists.field_list)
    skills = st.text_area("Key Skills & Interests",placeholder="e.g., Python, Java, C++, AI, Machine Learning, Accounting, Computer Networking...")
    top_k = st.slider("Number of results to retrieve" , min_value=1 , max_value=20 , value=5)
    submitted = st.form_submit_button("Find Internships!")
    

if submitted:

        user_input = {"location":location , "sector":sector , "field":field , "skills":skills , "top_k":top_k}
        
        if not user_input["location"] and not user_input["sector"] and not user_input["field"] and not user_input["skills"]:
            st.warning("Atleast fill some input fields...")
        else:
      
            with st.spinner("Finding Internships"):


                response = requests.post(backend_url , json=user_input)
            if response.status_code == 200:
                data = response.json()

                st.success(f"Found top {top_k} matches!")
                st.balloons()
                #st.dataframe(results,width='stretch')
                #print(type(results))
                #st.write(data)
                
                for item in data:
            
                    with st.container(border=True):
                
                        # --- Header Section ---
                        title_col, score_col = st.columns([3, 1])
                        with title_col:
                            st.subheader(f"✨ {item.get('internship_title')}")
                            st.markdown(f"**🏢 {item.get('company_name')}** &nbsp; | &nbsp; 📍 {item.get('location')}")
                                        
                        with score_col:
                            score = item.get('similarity_score')
                            if pd.notna(score) and score*100 >= MATCH_THRESHOLD:
                                        # Using HTML to right-align and color the text green
                                st.markdown(f"<h4 style='text-align: right; color: #2e7d32;'>🔥 {score*100:.1f}% Match</h4>", 
                                                unsafe_allow_html=True
                                            )



                        # --- Quick Stats Columns ---
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.caption("📅 Start Date")
                            st.write(item.get('start_date'))
                        with col2:
                            st.caption("⏳ Duration")
                            st.write(item.get('duration'))
                        with col3:
                            st.caption("💰 Stipend")
                            st.write(item.get('stipend'))
                            
                        # --- Tags / Skills Section ---
                        st.markdown(f"**Sector:** {item.get('sector_name')} &nbsp; | &nbsp; **Field:** {item.get('field_name')}")
                        st.markdown(f"**🛠️ Skills Required:** `{item.get('skills_set')}`")
                        
                        # --- Expandable Description ---
                        with st.expander("Read Detailed Description"):
                            st.write(item.get('detailed_description'))

            elif response.status_code == 400:
                st.warning("Fill atleast some input")
                            





