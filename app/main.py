'''
Main file for the routes and some logic of the API
'''
from typing import Optional
from enum import Enum

import numpy as np
import mlflow
import mlflow.sklearn

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel


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
    clf = mlflow.sklearn.load_model("model/")

    # json_item = jsonable_encoder(item)
    # data = pd.DataFrame(json_item, index=[0])
    sample = np.array([i for i in Item.values()]).reshape(1, -1)
    y_pred = clf.predict(sample)
    print(y_pred)
    del clf
    del sample

    print(y_pred)
    return "Exito!"
