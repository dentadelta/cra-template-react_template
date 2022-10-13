from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import microservice1
from backend import dashboard

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(microservice1.router)
app.include_router(dashboard.router)
