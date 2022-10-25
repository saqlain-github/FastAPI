from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Fruit(BaseModel):
    name : str
    weight : Optional[int] = None
    count : int

app =FastAPI()

# @app.get("/")
# def typeHinte(name:str, height:int):
#     print("You name is :"+name+"Your height is : "+height)


@app.get("/")
def hello():
    return {"Hello" : "world"}

#HTTP request Body can use Get or post
@app.post("/fruit")
def fruit(f:Fruit):
    return {"name" : f.name, "weight" : f.weight, "count" : f.count}