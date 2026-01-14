from flask import Flask

from src.blueprint import router

app = Flask(__name__, template_folder="src/templates", static_folder="src/static")
app.secret_key = "dev-secret"
app.register_blueprint(router)
