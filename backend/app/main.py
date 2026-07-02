from fastapi import FastAPI
from .services import search_results
app=FastAPI()
@app.get("/")
def home():
    return{
        "message":"Welcome to my AI Search Engine!"
    }
@app.get("/search")

def search(query:str,limit:int=5):  
    if query=="":
        return{
            "error":"Please enter a search term"
        }
    if limit<=0:
        return{
            "error":"Limit must be greater than 0"
        }
    results = search_results(query,limit)
    if len(results)==0:
        return{
            "search":query,
            "limit":limit,
            "results":[],
            "message":"No results found"
        }
@app.get("/user/{name}")
def get_user(name:str):
    return{
        "user":name
    }
@app.get("/user/{name}/post/{post_id}")
def get_post(name:str,post_id:int):
    return{
        "user":name,
        "post_id":post_id  
    }