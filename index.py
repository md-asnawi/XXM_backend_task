from fastapi import FastAPI
from route import pallet

app = FastAPI()
app.include_router(pallet)