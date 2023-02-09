from utils import *

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="./templates")


@app.get("/")
def main_page(request: Request):
    result = "The inputed area:"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


@app.post("/")
def main_page(request: Request, area_id: str = Form(...)):
    make_map(area_id)
    return templates.TemplateResponse('index.html', context={'request': request, 'result': area_id})


@app.get("/map")
def map_page(request: Request):
    return templates.TemplateResponse('geo.html', context={'request': request})


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
