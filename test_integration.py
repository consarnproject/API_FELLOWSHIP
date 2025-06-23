from fastapi.testclient import TestClient
from main  import app 
from main import Fruit, Fruits, memory_db
import pytest

client = TestClient(app)
 

@pytest.fixture
def fruit(fruit: Fruit):
    return memory_db["fruits"].append(fruit)


def test_get_fruits():
    response = client.get("/fruits")
    assert response.status_code == 200 
    assert response.json() == { "fruits": [] }


def test_add_fruits():
    response = client.post("/fruits")

    assert response.status_code == 200
    assert response.json() == {'fruits': fruit}

