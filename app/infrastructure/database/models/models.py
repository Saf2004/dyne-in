from pydantic import BaseModel, UUID4
from typing import Optional, List
from datetime import datetime
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    PREPARING = 'preparing'
    READY = 'ready'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'

class OrderType(str, Enum):
    DINE_IN = 'dine_in'
    PICKUP = 'pickup'
    DELIVERY = 'delivery'

class MenuItem(BaseModel):
    id: Optional[UUID4]
    name: str
    description: Optional[str]
    price: float
    category_id: UUID4
    image_url: Optional[str]
    is_available: bool = True

class Order(BaseModel):
    id: Optional[UUID4]
    user_id: UUID4
    order_type: OrderType
    status: OrderStatus = OrderStatus.PENDING
    total_amount: float
    special_instructions: Optional[str]
    table_number: Optional[int]
