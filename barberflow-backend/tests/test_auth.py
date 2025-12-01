def test_register_user(client):
    """Teste: Cliente deve conseguir se cadastrar."""
    payload = {
        "name": "Cliente Teste",
        "email": "cliente@email.com",
        "password": "123"
    }
    response = client.post('/api/auth/register', json=payload)
    assert response.status_code == 201
    assert response.json['email'] == "cliente@email.com"

def test_login_user(client):
    """Teste: Cliente deve conseguir logar e receber sucesso."""
    # 1. Cria usuário
    client.post('/api/auth/register', json={"name": "User", "email": "login@test.com", "password": "123"})
    
    # 2. Tenta logar
    payload = {"email": "login@test.com", "password": "123"}
    response = client.post('/api/auth/login', json=payload)
    
    assert response.status_code == 200
    assert "Login realizado" in response.json['message']