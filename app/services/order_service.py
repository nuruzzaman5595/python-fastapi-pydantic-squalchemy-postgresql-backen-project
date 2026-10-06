from sqlalchemy.orm import Session
from app.models.order import Order

def get_orders(db: Session):
    return db.query(Order).all()