from typing import Optional
from fastapi import FastAPI

app = FastAPI()

"""
必須ではない変数にOptional[型] = Noneとする
"""
@app.get("/countries/")
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "city_name": country_no
    }