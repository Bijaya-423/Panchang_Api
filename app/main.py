from fastapi import FastAPI
from .api.routes import router

app = FastAPI()

# Include the router for Panchang API
app.include_router(router)
