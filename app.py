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
tamu_undangan = """KELUARGA BANI HUZAINI	24
ARSITEKTUR UB 2013	149
ALL MEMBER BJ 28	57
DINDA PUTRI & GURUH	65
FEBY VALENTINA	52
VINA ALFI M & SUAMI	81
MELINA PANDAN S	145
FIDIAH AULIA & SUAMI	28
KURNIA CAHYA P	143
REVYANA NAWANG & REZA	163
ANDREA TYA 	84
DIASTIKA R & SUAMI	31
SULIS AGUSTIA & SUAMI	76
IRA YULIA ASTUTIK & SUAMI	188
SYAFIRA SALASABILA	166
FAJAR FURQON	106
PUSPA NILA CEMPAKA & SUAMI	101
GABRIELLA S. & SUAMI	165
YUNISA ROSIYANTO	192
TRI YUNI & SUAMI	183
PRATIWI OKTAVIANA & SUAMI	155
FAHMIA TSANIE & SUAMI	171
NUR AZLINA	156
RESTICA	48
UMAMAH AL BATUL	14
ALMAS NUGRAHANINGSIH	29
FARADINA HASAN	5
ARIDA F YASMIN	32
SHOFY AFINA	93
UMI HAJAR KH	44
MARTHA ANGELIA	107
DEWI WIDYA 	9
ROHADATUL AISY	143
Anggit Teguh Iman	145
Aji Prisma Arista	40
Aditya Alfian Noor	177
Ainul Fahmi	10
Andreas Bayu Saputra	48
Ari Sulistyo	55
Ageng Gesit Putro Panuntun	76
Bayu Ikhsan Saputra	39
Bentar Randy	123
M. Aden Al Barrie	99
Enggar Tyasto	41
Habib Syarif Dalimunte	57
Joko Purnomo	165
Jundi Izzuddin Alqosam	183
Leo Saputra	45
Sandy Janilandra Irawan	27
Ramadhona Kurniawan	23
Nurul Efendi	115
Wicaksono Sambu Wihikan	197
Wahyu Purba Aji	38
M. Thorig Algomar	178
Dian Ardia Rini	88
Dwika Putra Anugrah	194
Ardiansyah Selian	152
M. Chotibul Umam	17
Ervanda Putra	41
Faisal Wahyu Hidayat	26
R. Alvino Putra Yodi Prasetyo	56
Hadi Susanto	20
Fajar Nurhadi	12
Edi Hartono	67
Muhammad Zakaria	145
Muhammad Zulkarnain	25
Aron Dio Sabatino Akimas	79
Candra Agung Prabowo	82
Vikri Ari Susanto	96
Rifki Setiawan	144
Bass RIFQI Halvyan	154
Bass Eka Putra adhy Suryanto	27
M.Eko Pujo Sakti & Istri	126
Febrian Nuzulul Arsya & Istri	106
Rifaldi Wahyu Putra	29
Eka Retno Ardianti	88
M Fahmi Suyuti	6
Dinas PU Banyuwangi	118
Badan Pendapatan Daerah Banyuwangi	36
Inspektorat Banyuwangi	31
Keluarga Aseph (9F) 	90
Vanadia Anisa	49
Angelia Septa	195
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