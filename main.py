 
from router.router import user
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user)
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="https://localhost.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
