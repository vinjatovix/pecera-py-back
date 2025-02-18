from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/api/v1/health/http")
def get_health():
    return {"status": "OK"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
