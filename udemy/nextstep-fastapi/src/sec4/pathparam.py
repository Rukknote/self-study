from fastapi import FastAPI

app = FastAPI()

@app.get("/countries/{country_name}")
async def country(country_name: str): # 型を指定することで受け取るデータを制御できる
    return {"country_name": country_name}