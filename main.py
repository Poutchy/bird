from flask import Flask

from src.blueprint import router

app = Flask(__name__, template_folder="src/templates")
app.register_blueprint(router)
