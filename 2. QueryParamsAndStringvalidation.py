from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()


@app.get("/")
def hello():
    return {"hello": "world"}
            

@app.get("/fruit")
def fruit(fruit_name : Optional[str] = Query("Orange",min_length=2,max_length=5)):
    return {"THis is query parameter":fruit_name}

#http://127.0.0.1:8000/fruit?fruit_name=orange
# def fruit(fruit_name : str = Query("Orange",min_length=2,max_length=5)):
# def fruit(fruit_name : Optional[str] = Query(...,min_length=2,max_length=5)): # pass compulsory