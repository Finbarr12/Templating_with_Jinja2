from flask import Blueprint

product_blueprint = Blueprint("product",__name__)

@product_blueprint.route("/")
@product_blueprint.route("/home")
def home ():
    return 