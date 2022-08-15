from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException

from marketview.model.company import Company
from marketview.service.company_service import CompanyService

router = APIRouter()
company_service: CompanyService = CompanyService()


@router.get("/companies", tags=["companies"])
async def get_companies() -> List[Dict[str, Any]]:
    return []


@router.get("/companies/{id}", tags=["companies"])
async def get_company(id: int) -> Dict[str, Any]:
    company: Optional[Company] = company_service.find_by_id(id=id)

    if not company:
        raise HTTPException(status_code=404, detail=f"Company with id '{id}' not found!")

    return company.__dict__


@router.post("/companies", tags=["companies"])
async def post_company() -> Dict[str, Any]:
    return {}
