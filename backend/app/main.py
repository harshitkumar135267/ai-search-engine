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
    search_data = {
        "python": [
            {
                "title": "Python Offical Website",
                "Url": "https://www.python.org"
            },
            {
                "title": "W3Schools Python",
                "url": "https://www.w3schools.com/python"
            }
        ],
        "java":[
            {
                "title": "Oracle Java",
                "url": "https://www.oracle.com/java/"
            }
        ]
    }
    results = search_data.get(query.lower(),["result not found"])
    return{
        "search":query,
        "limit":limit,
        "results":results
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