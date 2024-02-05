from db import db

class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    account_id = db.Column(db.Integer(), db.ForeignKey("accounts.id"), nullable=False)

    account = db.relationship("AccountModel", back_populates="tags")
    items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")
