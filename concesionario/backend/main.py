from fastapi import FastAPI
from routes.usuario_routes import router as usuario_router

app = FastAPI()
app.include_router(usuario_router)
