from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{
        "message":"Welcome to my AI Search Engine!"
    }
@app.get("/search")
def search(query:str):
    if query=="":
        return{
            "error":"Please enter a search term"
        }
    return{
        "search":query
    }