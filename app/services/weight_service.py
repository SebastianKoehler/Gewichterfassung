from app import WeightEntry
from sqlalchemy.orm import Session


class WeightService:
    def __init__(self, session: Session):
        self.session = session

    @classmethod
    def add_weight_entry(cls, date, weight):
        new_entry = WeightEntry(date=date, weight=weight)
        return new_entry

    def get_weights(self):
        return self.session.query(WeightEntry).order_by(WeightEntry.date).all()
