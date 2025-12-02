def test_create_service(client):
    """Teste: Criar serviço"""
    response = client.post('/api/services/', json={"name": "Platinado", "price": 100, "duration": 120})
    assert response.status_code == 201
    assert response.json['name'] == "Platinado"

def test_update_settings(client):
    """Teste: Atualizar horário de funcionamento"""
    payload = {
        "open_time": "09:00",
        "close_time": "20:00"
    }
    response = client.put('/api/services/settings', json=payload)
    assert response.status_code == 200
    assert response.json['open_time'] == "09:00"

def test_update_service_price(client):
    """Teste: Deve atualizar o preço e duração de um serviço existente."""
    # 1. Cria um serviço (o ID será 1 no banco de testes)
    client.post('/api/services/', json={"name": "Corte Simples", "price": 30, "duration": 30})
    
    # 2. Dados de atualização
    payload_update = {
        "price": 50.00,
        "duration": 45
    }
    
    # 3. Envia o PUT para o ID 1
    response = client.put('/api/services/1', json=payload_update)
    assert response.status_code == 200
    
    # 4. Verifica se os novos valores foram aplicados
    assert response.json['price'] == 50.0
    assert response.json['duration'] == 45