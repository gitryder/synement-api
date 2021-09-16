from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import data as data

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {'info': 'synement v0.36'}


@app.get('/{year}/today')
def get_all_due_today(year):
    return data.all_due_today(year)


@app.get('/{year}/tomorrow')
def get_all_due_tomorrow(year):
    return data.all_due_tomorrow(year)


@app.get('/{year}/after')
def get_all_due_after_tomorrow(year):
    return data.all_due_after_tomorrow(year)
