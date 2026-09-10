from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector as mq

app = FastAPI()

@app.get("/")
def index_get():
    return {"message" : "hello"}

