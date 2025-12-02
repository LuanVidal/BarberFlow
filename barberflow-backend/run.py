from app import create_app, db
from app.models import Barber, Service, Appointment

app = create_app()

def setup_inicial():
    with app.app_context():
        # 1. Cria Barbeiro Padrão
        if not Barber.query.filter_by(email="barbeiro@teste.com").first():
            print("--- Criando Barbeiro ---")
            b = Barber(name="Barbeiro Chefe", email="barbeiro@teste.com")
            b.set_password("123")
            db.session.add(b)

        # 2. Cria/Atualiza Serviços (Preços que você pediu)
        servicos_padrao = [
            {"name": "Corte", "price": 35.0, "duration": 30},
            {"name": "Corte e Sobrancelha", "price": 40.0, "duration": 30},
            {"name": "Luzes", "price": 100.0, "duration": 90},
            {"name": "Barba", "price": 30.0, "duration": 20},
            {"name": "Corte e Barba", "price": 60.0, "duration": 50}
        ]

        print("--- Atualizando Serviços ---")
        for s_data in servicos_padrao:
            servico = Service.query.filter_by(name=s_data['name']).first()
            if not servico:
                servico = Service(name=s_data['name'], price=s_data['price'], duration=s_data['duration'])
                db.session.add(servico)
            else:
                servico.price = s_data['price'] # Atualiza preço se mudou
        
        db.session.commit()
        print("Banco de dados pronto!")

if __name__ == "__main__":
    setup_inicial()
    app.run(debug=True)