import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pkg.barcode.parser import parse
from pkg.barcode.encoder import encode

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/barcode", response_class=HTMLResponse)
async def render_barcode(request: Request):
    with open("test.json", "r") as f:
        data = f.read()
        obj = json.loads(data)
    return templates.TemplateResponse(
        request=request,
        name="barcode.html",
        context={"data": obj["packages"][0]},
    )


@app.get("/barcode/{code}", response_class=HTMLResponse)
async def parse_barcode(request: Request, code: str):
    path = parse(code)
    base64_image = encode(path)
    return templates.TemplateResponse(
        request=request, name="barcode_parser.html", context={"base64_image": base64_image}
    )
