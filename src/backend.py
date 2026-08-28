from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class user_input(BaseModel):
    location : List[str]
    sector : List[str]
    field : List[str]
    skills : str
    top_k : int

app = FastAPI()


@app.get("/")
def home(): 
    return {"message":"Home route of FastApi Backend"}



@app.post("/get_internship")
def get_internship(user_input : user_input):
    return user_input