from flask import Blueprint, abort, jsonify, render_template, request
from jinja2 import TemplateNotFound

router = Blueprint("simple_page", __name__)


@router.route("/", defaults={"page": "index"})
@router.route("/<page>")
def show(page):
    try:
        return render_template(f"{page}.html")
    except TemplateNotFound:
        abort(404)

@router.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict(flat=False)  # Permet de récupérer toutes les valeurs cochées
    print(data)
    return jsonify(data)
