from . import db

class Service(db.Model):
    __tablename__ = 'services'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False) # Em minutos

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'duration': self.duration
        }