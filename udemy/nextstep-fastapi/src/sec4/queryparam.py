from fastapi import FastAPI

app = FastAPI()

"""
クエリパラメータとは、URLの?マーク以降の内容
パスパラメータは書かれていないけれど引数が指定されている場合、クエリパラメータに該当する
"""
@app.get("/countries/")
async def country(country_name: str = "japan", country_no: int = 1):
    return {
        "country_name": country_name,
        "city_name": country_no
    }
"""
http://127.0.0.1:8000/countries/
を叩くと
{"country_name":"japan","city_name":1}

http://127.0.0.1:8000/countries/?country_name=America&country_no=2
を叩くと
{"country_name":"America","city_name":2}
"""