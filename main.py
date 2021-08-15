from fastapi import FastAPI
import data as data

app = FastAPI()


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
