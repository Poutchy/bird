from flask import Blueprint, abort, redirect, render_template, request, session, url_for
from jinja2 import TemplateNotFound

from src import all_birds
from src.distance import find_closer

router = Blueprint("simple_page", __name__)


@router.route("/", defaults={"page": "index"})
@router.route("/<page>")
def show(page):
    try:
        result = session.pop("result", None)
        return render_template(f"{page}.html", result=result)
    except TemplateNotFound:
        abort(404)


@router.route("/submit", methods=["POST"])
def submit():
    data = request.form.to_dict(flat=False)
    print(f"{data=}")
    res = find_closer(data, all_birds)
    print(f"{res=}")

    session["result"] = res

    return redirect(url_for("simple_page.show"))
