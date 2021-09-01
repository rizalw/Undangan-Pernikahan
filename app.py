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
tamu_undangan = """KELUARGA BANI HUZAINI	80
ARSITEKTUR UB 2013	14
ALL MEMBER BJ 28	168
DINDA PUTRI & GURUH	40
FEBY VALENTINA	150
VINA ALFI M & SUAMI	166
MELINA PANDAN S	161
FIDIAH AULIA & SUAMI	83
KURNIA CAHYA P	197
REVYANA NAWANG & REZA	166
ANDREA TYA 	10
DIASTIKA R & SUAMI	162
SULIS AGUSTIA & SUAMI	78
IRA YULIA ASTUTIK & SUAMI	46
SYAFIRA SALASABILA	4
FAJAR FURQON	94
PUSPA NILA CEMPAKA & SUAMI	15
GABRIELLA S. & SUAMI	66
YUNISA ROSIYANTO	20
TRI YUNI & SUAMI	156
PRATIWI OKTAVIANA & SUAMI	118
FAHMIA TSANIE & SUAMI	106
NUR AZLINA	173
RESTICA	26
UMAMAH AL BATUL	174
ALMAS NUGRAHANINGSIH	82
FARADINA HASAN	80
ARIDA F YASMIN	10
SHOFY AFINA	136
UMI HAJAR KH	175
MARTHA ANGELIA	121
DEWI WIDYA 	151
ROHADATUL AISY	185
Anggit Teguh Iman	30
Aji Prisma Arista	172
Aditya Alfian Noor	150
Ainul Fahmi	150
Andreas Bayu Saputra	110
Ari Sulistyo	85
Ageng Gesit Putro Panuntun	18
Bayu Ikhsan Saputra	122
Bentar Randy	112
M. Aden Al Barrie	77
Enggar Tyasto	122
Habib Syarif Dalimunte	83
Joko Purnomo	8
Jundi Izzuddin Alqosam	46
Leo Saputra	182
Sandy Janilandra Irawan	82
Ramadhona Kurniawan	180
Nurul Efendi	64
Wicaksono Sambu Wihikan	125
Wahyu Purba Aji	23
M. Thorig Algomar	36
Dian Ardia Rini	97
Dwika Putra Anugrah	1
Ardiansyah Selian	23
M. Chotibul Umam	130
Ervanda Putra	121
Faisal Wahyu Hidayat	155
R. Alvino Putra Yodi Prasetyo	87
Hadi Susanto	132
Fajar Nurhadi	53
Edi Hartono	193
Muhammad Zakaria	85
Muhammad Zulkarnain	48
Aron Dio Sabatino Akimas	61
Candra Agung Prabowo	129
Vikri Ari Susanto	107
Rifki Setiawan	31
Bass RIFQI Halvyan	200
Bass Eka Putra adhy Suryanto	39
M.Eko Pujo Sakti & Istri	67
Febrian Nuzulul Arsya & Istri	142
Rifaldi Wahyu Putra	152
Eka Retno Ardianti	40
M Fahmi Suyuti	39
Dinas PU Banyuwangi	125
Badan Pendapatan Daerah Banyuwangi	112
Inspektorat Banyuwangi	41
Keluarga Aseph (9F) 	158
Vanadia Anisa	156
Angelia Septa	69
Rizka Ilmawati	21"""

def get_keys(tamu_undangan, id):
    data = tamu_undangan.split("\n")
    for datum in data:
        atom = datum.split("\t")
        if id == int(atom[-1]):
            return atom[0]
        

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
        global tamu_undangan
        global overlay
        daftar_komentar = komentar.query.order_by(komentar.date_created).all()
        return render_template("index.html", data = get_keys(tamu_undangan, id), id = id, overlay = overlay, daftar_komentar = daftar_komentar)
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