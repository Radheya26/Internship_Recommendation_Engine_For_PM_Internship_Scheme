import streamlit as st
import numpy as np
import pandas as pd 
import lists
from fastembed import TextEmbedding


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
        st.dataframe(results,use_container_width=True)





