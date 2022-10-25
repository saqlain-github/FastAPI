# to return an http response with error to clien you use HTTPException

from fastapi import FastAPI, HTTPException

app = FastAPI()

fruit = {"orange":"This fruit is sour"}

@app.get("/fruit/{fruit_name}")
def read_fruit(fruit_name :str):
    if fruit_name not in fruit:
        raise HTTPException(status_code=404, detail = "Item not found")
    return {"fruit property": fruit[fruit_name]}