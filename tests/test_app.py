from app import app

def test_home():

    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200