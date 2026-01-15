from flask import Blueprint, abort, jsonify, render_template, request
from jinja2 import TemplateNotFound

from src import all_birds
from src.data import normalize_form_data
from src.distance import find_closer

router = Blueprint("simple_page", __name__)


@router.route("/", defaults={"page": "index"})
@router.route("/<page>")
def show(page):
    try:
        return render_template(f"{page}.html")
    except TemplateNotFound:
        abort(404)


@router.route("/submit", methods=["POST"])
def submit():
    data = normalize_form_data(request.form.to_dict(flat=False))
    print(f"{data=}")
    res = find_closer(data, all_birds)
    print(f"{res=}")

    return jsonify({"success": True, "result": res})


@router.route("/all-birds", methods=["GET"])
def get_all_birds():
    for bird in all_birds:
        bird["score"] = 0.0
    return jsonify({"success": True, "result": all_birds})
