from typing import Optional

import uvicorn
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


#uvicorn main:app --reload   -- use this to start the app

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/form", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/basic", response_class=HTMLResponse)
async def getting_form_data(request: Request, first_no: str = Form(...), second_no: str = Form(...), file: UploadFile = File(...)):
    sum = int(first_no) + int(second_no)
    content = await file.read()
    print(content)
    return templates.TemplateResponse("result.html", {"request": request, "sum": sum, "file_data": content})

if __name__ == '__main__':
    uvicorn.run(app)

