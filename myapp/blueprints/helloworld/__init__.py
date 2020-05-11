from flask import Blueprint
from .helloworld import index

bp = Blueprint("webui", __name__, template_folder="templates")
bp.add_url_rule("/", view_func=index)