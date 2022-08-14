from fastapi import FastAPI
from typing import Any, Dict
import uvicorn

app = FastAPI()


@app.get("/")
async def root() -> Dict[str, Any]:
    return {"message": "Hello world!"}


def start():
    uvicorn.run("marketview.api:app", host="0.0.0.0", port=8000, reload=True, workers=2)
