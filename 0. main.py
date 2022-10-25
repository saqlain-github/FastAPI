from fastapi import FastAPI
from pydantic import BaseModel


''''''
class Fruit(BaseModel):
    name : str
    price : int
    
app = FastAPI()
#uvicorn main:app --reload -> run the main.py


@app.get("/")
def root():
    return {"hello": "weorld"} 


# @app.get("/")
# def root_2(items:int):
#     return  {"hello": items}
# @app.put("/hello")
# def root():
#     return {"1":"2"} 


@app.put("/fruit_count/{count}")
def get_fruit_count(count:int, fruit_name:Fruit):
    return { "Total Fruit Count " : count, 
            "fruit_name " : fruit_name.name,
            "price ": fruit_name.price
            } 

