from fastapi import FastAPI
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
    return{
        "search":query,
        "limit":limit
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