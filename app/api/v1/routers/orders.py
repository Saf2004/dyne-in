from fastapi import APIRouter, HTTPException
from infrastructure.database.client import supabase
from infrastructure.database.models.models import Order

from typing import List

router = APIRouter()

@router.post("/orders")
async def create_order(order: Order):
    try:
        response = supabase.table('orders').insert(order.dict()).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/orders", response_model=List[Order])
async def get_orders():
    try:
        response = supabase.table('orders').select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
