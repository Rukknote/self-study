from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: Optional[ShopInfo]
app = FastAPI()

@app.post("/item/")
async def create_item(item: Item):
    #return item
    return {
        "message": f"{item.name}は、税込価格{int(item.price*item.tax)}円です"
    }