from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
 

app = FastAPI() 

@app.get("/fruits")
async def get_fruits(Fruits: str):
    return {"Fruits": Fruits, "name": f"Fruit {Fruits}" }



client = TestClient(app)

def test_get_fruits():
    response = client.get("/fruits")
    assert response.status_code == 200 
    assert response.json() == {'fruit': 'Fruit'}




