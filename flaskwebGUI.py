from flask import Flask
from flaskwebgui import FlaskUI

app = Flask(__name__)
ui = FlaskUI(app)

@app.route("/")
def index():
    return "It works"

ui.run()