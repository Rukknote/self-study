from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field

class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12) #文字数を制限できる
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]

app = FastAPI()

@app.post("/")
async def index(data: Data):
    return {
        "message": data
    }

"""
penと3文字にした場合、422 Error: Unprocessable Entityが出る
{
  "shop_info": {
    "name": "ABC store",
    "location": "Tokyo"
  },
  "items": [
    {
      "name": "pen",
      "description": "this is cheap",
      "price": 100,
      "tax": 1.1
    }
  ]
}

{
  "detail": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "items",
        0,
        "name"
      ],
      "msg": "String should have at least 4 characters",
      "input": "pen",
      "ctx": {
        "min_length": 4
      }
    }
  ]
}
"""