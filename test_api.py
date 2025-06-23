from fastapi.testclient import TestClient 
from main import app 
from main import Fruit, Fruits, memory_db

import pytest

from test_integration import fruit 

client = TestClient(app) 

def test_get_fruits():
    response = client.get("/fruits")
    assert response.status_code == 200
    assert response.json() == {"fruits": []}

def test_add_fruits():
    response = client.post("/fruits")
    assert response.status_code == 200 
    assert response.json() == {"fruits": fruit}
    
    
    
    
    
    