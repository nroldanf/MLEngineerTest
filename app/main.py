'''
Main file for the routes and some logic of the API
'''
from typing import Optional
from enum import Enum

import pandas as pd
import mlflow
import mlflow.sklearn

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel

clf = mlflow.pyfunc.load_model("model/")

feats = ['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
       'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity',
       'speechiness', 'tempo', 'valence', 'year']

app = FastAPI()

class Item(BaseModel):
    acousticness: float
    danceability: float
    duration_ms: int
    energy: float
    explicit: int
    instrumentalness: float
    key: int
    liveness: float
    loudness: float
    mode: int
    popularity: int
    speechiness: float
    tempo: float
    valence: float
    year: int


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/guess_artist", status_code=200)
async def guess_artist(item: Item):
    '''
    '''
    print("Inicio")
    json_item = jsonable_encoder(item)
    print(json_item)
    data = pd.DataFrame(json_item, index=[0])
    print(data)
    y_pred = clf.predict(data)
    print(y_pred)
    return "Exito"
