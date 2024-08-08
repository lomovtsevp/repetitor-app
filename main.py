from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Create the FastAPI app
app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')


templates = Jinja2Templates(directory="templates")

@app.get("/welcome")
async def root(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})