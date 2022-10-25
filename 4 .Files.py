from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
def hello():
    return {"File": "FileUpload"}

@app.post("/file")
def create_f(file : bytes = File(...)): # works for short files
    return {"file size" : len(file)}

@app.post("/uploaded_f") # works for bigger file
def uploaded_f(file:UploadFile):
    return {"Filename " : file.filename}