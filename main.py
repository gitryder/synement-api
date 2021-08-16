from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import data as data

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:1234",
]

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


@app.get('/all')
def get_all_course_work():
    return data.all_course_work()


@app.get('/assignments')
def get_assignments():
    return data.all_assignments()


@app.get('/experiments')
def get_experiments():
    return data.all_experiments()
