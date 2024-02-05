from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)

    account_id = db.Column(
        db.Integer, db.ForeignKey("accounts.id"), unique=False, nullable=False
    )
    account = db.relationship("AccountModel", back_populates="items")

    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")
