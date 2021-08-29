from re import A
from flask import *
from flask.scaffold import F
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

def get_keys(value):
    for x, y in tamu_undangan.items():
        if y == value:
            return x

overlay = True

#routing

@app.route("/admin214")
def admin():
    daftar_komentar = komentar.query.order_by(komentar.date_created).all()
    return render_template("admin.html", daftar_komentar = daftar_komentar)


@app.route("/")
def index():
    try:
        global overlay
        daftar_komentar = komentar.query.order_by(komentar.date_created).all()
        return render_template("index.html", data = "Anonim", id = 0, overlay = overlay, daftar_komentar = daftar_komentar)
    finally:
        if overlay is False:
            overlay = True


@app.route("/<int:id>")
def personalized_index(id):
    try:
        global overlay
        daftar_komentar = komentar.query.order_by(komentar.date_created).all()
        return render_template("index.html", data = get_keys(id), id = id, overlay = overlay, daftar_komentar = daftar_komentar)
    finally:
        if overlay is False:
            overlay = True

@app.route("/delete/<int:id>")
def delete(id):
    delete_data = komentar.query.get_or_404(id)
    try:
        db.session.delete(delete_data)
        db.session.commit()
        return redirect("/admin214")
    except:
        return "Terjadi masalah dalam penghapusan data"

@app.route("/submit/<author>/<int:id>", methods = ["POST"])
def submit(id, author):
    author = author
    comment = request.form["comment"]
    # print(author, comment)
    global overlay
    overlay = False
    input_baru = komentar(author, comment)
    try:
        db.session.add(input_baru)
        db.session.commit()
    except:
        return "Upload Gagal"
    else:
        if id == 0:
            return redirect("/")
        return redirect("/{}".format(id))

@app.route('/download')
def download():
    return send_file("./static/images/Tiket-Souvenir.png", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)