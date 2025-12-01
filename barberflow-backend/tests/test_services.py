def test_create_service(client):
    """
    Teste: Admin deve conseguir cadastrar um novo serviço.
    """
    payload = {
        "name": "Corte Degrade",
        "price": 35.00,
        "duration": 30
    }
    
    # Tenta criar via POST
    response = client.post('/api/services/', json=payload)
    
    # Verifica se criou (201 Created)
    assert response.status_code == 201
    assert response.json['name'] == "Corte Degrade"

def test_get_services(client):
    """
    Teste: Cliente deve conseguir listar os serviços.
    """
    # Cria um serviço primeiro
    client.post('/api/services/', json={"name": "Barba", "price": 20, "duration": 15})
    
    # Tenta buscar via GET
    response = client.get('/api/services/')
    
    assert response.status_code == 200
    assert len(response.json) > 0
    assert response.json[0]['name'] == "Barba"