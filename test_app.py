import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client: #Cliente de prueba para hacer get y POST
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

def test_estado_contiene_tipos(client):
    response = client.get("/estado")
    assert response.status_code == 200
    data = response.get_json()
    for tipo in ["CAJ", "PERS", "REC", "JOP"]:     # Solo aseguramos que estén todas las claves
        assert tipo in data

