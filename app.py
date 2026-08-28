import streamlit as st
import numpy as np
import pandas as pd 
import lists
from fastembed import TextEmbedding

MATCH_THRESHOLD = 60

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

load_css("style.css")

@st.cache_resource
def load_search_engine():
    df = pd.read_csv("internships.csv")
    doc_embeddings = np.load("documents_embedding.npy")

    model = TextEmbedding()
    return df , doc_embeddings , model

df , doc_embeddings , model = load_search_engine()

def get_top_matches(query_text:str , top_k:int =5):
    query_vector = np.array(list(model.embed([query_text]))[0])
    similarity_scores =np.dot(doc_embeddings , query_vector)

    top_indices = np.argsort(similarity_scores)[::-1][:top_k]

    results = df.iloc[top_indices].copy()
    results['similarity_score'] = similarity_scores[top_indices]

    return results






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
    query_parts = [location , sector , field , skills]
    combined_query = " ".join([str(part).strip() for part in query_parts if part and str(part).strip()])

    if not combined_query:
        st.warning("Please fill at least one field before searching.")
    else:
        with st.spinner("Finding Internships"):
            results = get_top_matches(combined_query , top_k=top_k)
        st.success(f"Found top {top_k} matches!")
        st.balloons()
        #st.dataframe(results,width='stretch')
        #print(type(results))

        for index, row in results.iterrows():
    
            with st.container(border=True):
        
                # --- Header Section ---
                title_col, score_col = st.columns([3, 1])
                with title_col:
                    st.subheader(f"✨ {row['internship_title']}")
                    st.markdown(f"**🏢 {row['company_name']}** &nbsp; | &nbsp; 📍 {row['location']}")
                                
                with score_col:
                    score = row['similarity_score']
                    if pd.notna(score) and score*100 >= MATCH_THRESHOLD:
                                 # Using HTML to right-align and color the text green
                        st.markdown(f"<h4 style='text-align: right; color: #2e7d32;'>🔥 {score*100:.1f}% Match</h4>", 
                                        unsafe_allow_html=True
                                    )



                # --- Quick Stats Columns ---
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.caption("📅 Start Date")
                    st.write(row['start_date'])
                with col2:
                    st.caption("⏳ Duration")
                    st.write(row['duration'])
                with col3:
                    st.caption("💰 Stipend")
                    st.write(row['stipend'])
                    
                # --- Tags / Skills Section ---
                st.markdown(f"**Sector:** {row['sector_name']} &nbsp; | &nbsp; **Field:** {row['field_name']}")
                st.markdown(f"**🛠️ Skills Required:** `{row['skills_set']}`")
                
                # --- Expandable Description ---
                with st.expander("Read Detailed Description"):
                    st.write(row['detailed_description'])
                    # You can also add an "Apply Now" button here
                    if st.button("Apply Now", key=f"apply_{index}"):
                        st.success(f"Application started for {row['company_name']}!")





