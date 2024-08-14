from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

class RecipeTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<RecipeTable {self.name}>'

# Existing models from other projects
class BitcoinPriceData(db.Model):
    __tablename__ = 'bitcoin_prices'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    price = db.Column(db.Float)

class EthereumPriceData(db.Model):
    __tablename__ = 'ethereum_prices'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    price = db.Column(db.Float)

class TetherPriceData(db.Model):
    __tablename__ = 'tether_prices'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    price = db.Column(db.Float)
