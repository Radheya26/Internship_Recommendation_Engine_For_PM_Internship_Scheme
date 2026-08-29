from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd
from fastembed import TextEmbedding
import numpy as np
from fastapi.responses import JSONResponse

def load_search_engine():
    df = pd.read_csv("internships.csv")
    doc_embeddings = np.load("documents_embedding.npy")

    model = TextEmbedding()
    return df , doc_embeddings , model

df , doc_embeddings , model = load_search_engine()


def get_top_matches(query_text:List[str] , top_k:int =5):
    query_vector = np.array(list(model.embed(query_text))[0])
    similarity_scores =np.dot(doc_embeddings , query_vector)

    top_indices = np.argsort(similarity_scores)[::-1][:top_k]

    results = df.iloc[top_indices].copy()
    results['similarity_score'] = similarity_scores[top_indices]

    return results

#-----------------------------------------------------
class user_input(BaseModel):
    location : List[str]
    sector : List[str]
    field : List[str]
    skills : str
    top_k : int

app = FastAPI()

#---------------------------------------------------------

@app.get("/")
def home(): 
    return {"message":"Home route of FastApi Backend"}



@app.post("/get_internship")
def get_internship(user_input : user_input):

    location_str = " ".join(user_input.location)
    sector_str = " ".join(user_input.sector)
    field_str = " ".join(user_input.field)
    skill_str = user_input.skills
    
    
    combined_query = [f"{location_str} {sector_str} {field_str} {skill_str}"]

    if str(combined_query).strip() == "":
        return JSONResponse(status_code=400)



    
    results =  get_top_matches(combined_query , top_k=user_input.top_k)
    return results.to_dict(orient="records")

