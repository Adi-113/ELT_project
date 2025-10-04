import pandas as pd
from fastapi import FastAPI

app = FastAPI()

df = pd.read_csv("spotify_churn_dataset.csv")
@app.get("/")
def read_root():
    return {"message": "API is running 🚀"}

@app.get("/data")
def get_data():
    """Return rows from the CSV as JSON"""
    return df.to_dict(orient="records")

