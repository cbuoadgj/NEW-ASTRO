from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get('/')
def index_root():
    return {"message":"HEALTH IS COOL"}

