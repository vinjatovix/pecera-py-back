from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/health/http")
def get_health():
    return {"status": "OK"}
