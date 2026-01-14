from flask import Flask

from src.blueprint import router

app = Flask(__name__, template_folder="src/templates", static_folder="src/static")
app.register_blueprint(router)
