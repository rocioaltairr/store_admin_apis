from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import AccountModel
from schemas import AccountSchema


blp = Blueprint("Accounts", "accounts", description="Operations on accounts")


@blp.route("/account/<string:account>")
class Account(MethodView):
    @blp.response(200, AccountSchema)
    def get(self, account_id):
        account = AccountModel.query.get_or_404(account_id)
        return account

    def delete(self, account_id):
        account = AccountModel.query.get_or_404(account_id)
        db.session.delete(account)
        db.session.commit()
        return {"message": "account deleted"}, 200


@blp.route("/account")
class AccountList(MethodView):
    @blp.response(200, AccountSchema(many=True))
    def get(self):
        return AccountModel.query.all()

    @blp.arguments(AccountSchema)
    @blp.response(201, AccountSchema)
    def post(self, account_data):
        account = AccountModel(**account_data)
        try:
            db.session.add(account)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A account with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the account.")

        return account
