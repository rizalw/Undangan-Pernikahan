from flask import *
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
# db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/download')
def download():
    return send_file("./static/images/Tiket-Souvenir.png", as_attachment=True)
if __name__ == "__main__":
    app.run(debug=True)