import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client: #Cliente de prueba para hacer get y post
        yield client

def test_index(client): #Se simula entrar a la página y ver si el servidor responde
    response = client.get("/")
    assert response.status_code == 200

def test_generar_turno_valido(client):
    response = client.post("/generar_turno", json={"tipo": "CAJ"})
    assert response.status_code == 200
    data = response.get_json()
    assert "turno" in data
    assert data["turno"].startswith("CAJ-")

def test_generar_turno_invalido(client):
    response = client.post("/generar_turno", json={"tipo": "X"})
    assert response.status_code == 400
    data = response.get_json()
    assert "ERROR" in data

def test_estado(client):
    client.post("/generar_turno", json={"tipo": "PERS"})
    response = client.get("/estado")
    assert response.status_code == 200
    data = response.get_json()
    assert "PERS" in data

def test_estado_inicial(client):
    response = client.get("/estado")     # Verificamos que todos los contadores estén en 0 al inicio
    assert response.status_code == 200
    data = response.get_json()
    assert data == {"CAJ": 0, "PERS": 0, "REC": 0, "JOP": 0}

