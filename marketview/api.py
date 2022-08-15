from fastapi import FastAPI
from typing import Any, Dict
import uvicorn

from marketview.router.company_router import router as company_router

app = FastAPI()

app.include_router(company_router)


@app.get("/")
async def root() -> Dict[str, Any]:
    return {"message": "Hello world!"}


def start():
    uvicorn.run("marketview.api:app", host="0.0.0.0", port=8000, reload=True, workers=2)
