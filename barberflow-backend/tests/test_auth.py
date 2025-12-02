def test_register_user(client):
    """Teste: Deve registrar um novo cliente com sucesso"""
    payload = {
        "name": "Teste User",
        "email": "teste@email.com",
        "password": "123"
    }
    response = client.post('/api/auth/register', json=payload)
    assert response.status_code == 201
    assert response.json['email'] == "teste@email.com"

def test_login_client(client):
    """Teste: Deve logar como cliente"""
    # 1. Cria usuário
    client.post('/api/auth/register', json={"name": "User", "email": "login@test.com", "password": "123"})
    
    # 2. Tenta logar
    response = client.post('/api/auth/login', json={"email": "login@test.com", "password": "123"})
    assert response.status_code == 200
    assert response.json['role'] == 'client'

def test_login_fail(client):
    """Teste: Deve falhar com senha errada"""
    client.post('/api/auth/register', json={"name": "User", "email": "fail@test.com", "password": "123"})
    response = client.post('/api/auth/login', json={"email": "fail@test.com", "password": "errada"})
    assert response.status_code == 401