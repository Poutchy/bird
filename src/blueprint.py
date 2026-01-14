from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

router = Blueprint("simple_page", __name__)


@router.route("/", defaults={"page": "index"})
@router.route("/<page>")
def show(page):
    try:
        return render_template(f"{page}.html")
    except TemplateNotFound:
        abort(404)
