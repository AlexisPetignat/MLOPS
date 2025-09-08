from fastapi import FastAPI
from model_app import prediction
from pydantic import BaseModel

app = FastAPI()


@app.get("/predict")
async def predictGet():
    return {"y_predict": 2}


class houseFeatures(BaseModel):
    size: float
    rooms: int
    hasGarden: bool


@app.post("/predict")
async def predictPost(house: houseFeatures):
    return prediction(house.size, house.rooms, house.hasGarden)
