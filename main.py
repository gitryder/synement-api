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
    return {'info': 'synement v0.1'}


@app.get('/all/today')
def get_all_due_today():
    return data.all_due_today()


@app.get('/all/tomorrow')
def get_all_due_tomorrow():
    return data.all_due_tomorrow()


@app.get('/all/after')
def get_all_due_after_tomorrow():
    return data.all_due_after_tomorrow()


@app.get('/assignments')
def get_assignments():
    return data.all_assignments()


@app.get('/experiments')
def get_experiments():
    return data.all_experiments()
