from sqlalchemy.orm import Session
from app.models.review import Review


def create_review(
    db: Session,
    user_id: int,
    product_id: int,
    rating: int,
    comment: str
):
    review = Review(
        user_id=user_id,
        product_id=product_id,
        rating=rating,
        comment=comment
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    return review


def get_reviews(db: Session):
    return db.query(Review).all()


def get_review_by_id(db: Session, review_id: int):
    return (
        db.query(Review)
        .filter(Review.id == review_id)
        .first()
    )


def get_product_reviews(db: Session, product_id: int):
    return (
        db.query(Review)
        .filter(Review.product_id == product_id)
        .all()
    )


def update_review(
    db: Session,
    review_id: int,
    rating: int,
    comment: str
):
    review = get_review_by_id(db, review_id)

    if not review:
        return None

    review.rating = rating
    review.comment = comment

    db.commit()
    db.refresh(review)

    return review


def delete_review(db: Session, review_id: int):
    review = get_review_by_id(db, review_id)

    if not review:
        return False

    db.delete(review)
    db.commit()

    return True