from re import A
from flask import *
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(app)

#models
class komentar(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(50), nullable = False)
    comment = db.Column(db.String(255), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, author, comment):
        self.author = author
        self.comment = comment


#Guest Data
tamu_undangan = {
    "KELUARGA BANI HUZAINI" : 67,
    "ARSITEKTUR UB 2013" : 48,
    "ALL MEMBER BJ 28" : 134,
    "DINDA PUTRI & GURUH" : 33,
    "FEBY VALENTINA" : 195,
    "VINA ALFI M & SUAMI" : 64,
    "MELINA PANDAN S"	: 69,
    "FIDIAH AULIA & SUAMI" : 83,
    "KURNIA CAHYA P" : 92,
    "REVYANA NAWANG & REZA" : 80,
    "ANDREA TYA" : 112,
    "DIASTIKA R & SUAMI" : 136,
    "SULIS AGUSTIA & SUAMI" : 157,
    "IRA YULIA ASTUTIK & SUAMI" : 139,
    "SYAFIRA SALASABILA" : 143,
    "PUSPA NILA CEMPAKA & SUAMI" : 70,
    "M.Eko Pujo Sakti & Istri" : 21,
    "Febrian Nuzulul Arsya & Istri" : 94,
    "Rifaldi Wahyu Putra" : 194,
    "Eka Retno Ardianti" : 162,
    "M Fahmi Suyuti" : 166
}

#routing

@app.route("/admin214")
def admin():
    return render_template("admin.html")

@app.route("/")
def index():
    return render_template("index.html", data = "Nama Pengunjung")

def get_keys(value):
    for x, y in tamu_undangan.items():
        if y == value:
            return x

@app.route("/<int:id>")
def personalized_index(id):
    return render_template("index.html", data = get_keys(id))

@app.route('/download')
def download():
    return send_file("./static/images/Tiket-Souvenir.png", as_attachment=True)
if __name__ == "__main__":
    app.run(debug=True)