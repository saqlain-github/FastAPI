from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "world"}

@app.post("/signup")
def signup(user_name : str = Form(...), phone_no : int = Form(...)):
    return {"user_name": user_name}