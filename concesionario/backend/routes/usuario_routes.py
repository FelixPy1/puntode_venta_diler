from fastapi import APIRouter, HTTPException, status, Form, Request, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from backend.services.usuario_service import login_usuario
from backend.schemas.usuario_schemas import UsuarioLogin
from fastapi.staticfiles import StaticFiles

app = FastAPI()
router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)



templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@router.post("/login")
async def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    data = UsuarioLogin(email=email, password=password)

    try:
        usuario = login_usuario(data)

        # 🔥 Redirección según rol
        if usuario["rol"] == "admin":
            return RedirectResponse(url="/admin/dashboard", status_code=302)
        else:
            return RedirectResponse(url="/usuario/dashboard", status_code=302)

    except HTTPException as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": e.detail
            }
        )