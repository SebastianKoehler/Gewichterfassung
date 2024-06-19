from datetime import datetime
from app.database import db


class WeightEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    def __init__(self, weight_entry_id, weight_entry_weight, weight_entry_date=datetime.now().strftime("%d.%m.%Y")):
        self.id = weight_entry_id
        self.date = weight_entry_date
        self.weight = weight_entry_weight
