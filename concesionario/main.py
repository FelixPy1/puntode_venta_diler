from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from backend.routes.usuario_routes import router as usuario_router
app = FastAPI()
app.include_router(usuario_router)

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Ruta principal
@app.get("/")
async def mostrar_login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})