from fastapi import FastAPI

# インスタンス化
app = FastAPI()

@app.get("/")
async def index(): #async:非同期処理
    """
    uvicorn main:app --reload
    main.pyのインスタンスappを起動、main.pyに変更があれば再起動するように--reloadを選択
    
    ~/g/self-study/u/n/src/sec4 udemy-fastapi !3 ?6 > uvicorn main:app --reload                                                                     py fastapi_beginner-Mu8gULDl
    INFO:     Will watch for changes in these directories: ['/Users/username/git/self-study/udemy/nextstep-fastapi/src/sec4']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [51150] using StatReload
    INFO:     Started server process [51152]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     127.0.0.1:60089 - "GET / HTTP/1.1" 200 OK
    http://127.0.0.1:8000を開いて、「{"message":"Hello World"}」が表示されたら成功
    """
    return {"message": "Hello World"}