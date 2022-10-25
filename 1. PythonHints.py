from fastapi import FastAPI




app =FastAPI()

@app.get("/")
def typeHinte(name:str, height:int):
    print("You name is :"+name+"Your height is : "+height)

