from fastapi import APIRouter, HTTPException
from infrastructure.database.client import supabase
from infrastructure.database.models.models import MenuItem
from typing import List

router = APIRouter()

@router.get("/menu-items", response_model=List[MenuItem])
async def get_menu_items():
    try:
        response = supabase.table('menu_items').select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/menu-items/{item_id}")
async def get_menu_item(item_id: str):
    try:
        response = supabase.table('menu_items').select("*").eq('id', item_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Item not found")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
