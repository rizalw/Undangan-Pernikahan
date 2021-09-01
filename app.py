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
tamu_undangan = """KELUARGA BANI HUZAINI	199
ARSITEKTUR UB 2013	24
ALL MEMBER BJ 28	190
DINDA PUTRI & GURUH	149
FEBY VALENTINA	81
VINA ALFI M & SUAMI	9
MELINA PANDAN S	21
FIDIAH AULIA & SUAMI	156
KURNIA CAHYA P	119
REVYANA NAWANG & REZA	94
ANDREA TYA 	101
DIASTIKA R & SUAMI	45
SULIS AGUSTIA & SUAMI	164
IRA YULIA ASTUTIK & SUAMI	141
SYAFIRA SALASABILA	115
FAJAR FURQON	159
PUSPA NILA CEMPAKA & SUAMI	67
GABRIELLA S. & SUAMI	195
YUNISA ROSIYANTO	178
TRI YUNI & SUAMI	131
PRATIWI OKTAVIANA & SUAMI	159
FAHMIA TSANIE & SUAMI	101
NUR AZLINA	163
RESTICA	62
UMAMAH AL BATUL	186
ALMAS NUGRAHANINGSIH	72
FARADINA HASAN	197
ARIDA F YASMIN	192
SHOFY AFINA	19
UMI HAJAR KH	1
MARTHA ANGELIA	29
DEWI WIDYA 	29
ROHADATUL AISY	195
Anggit Teguh Iman	39
Aji Prisma Arista	188
Aditya Alfian Noor	77
Ainul Fahmi	187
Andreas Bayu Saputra	91
Ari Sulistyo	143
Ageng Gesit Putro Panuntun	173
Bayu Ikhsan Saputra	39
Bentar Randy	32
M. Aden Al Barrie	141
Enggar Tyasto	45
Habib Syarif Dalimunte	10
Joko Purnomo	172
Jundi Izzuddin Alqosam	39
Leo Saputra	23
Sandy Janilandra Irawan	87
Ramadhona Kurniawan	32
Nurul Efendi	155
Wicaksono Sambu Wihikan	152
Wahyu Purba Aji	5
M. Thorig Algomar	132
Dian Ardia Rini	14
Dwika Putra Anugrah	81
Ardiansyah Selian	57
M. Chotibul Umam	156
Ervanda Putra	15
Faisal Wahyu Hidayat	3
R. Alvino Putra Yodi Prasetyo	184
Hadi Susanto	120
Fajar Nurhadi	58
Edi Hartono	151
Muhammad Zakaria	125
Muhammad Zulkarnain	98
Aron Dio Sabatino Akimas	168
Candra Agung Prabowo	129
Vikri Ari Susanto	103
Rifki Setiawan	55
Bass RIFQI Halvyan	136
Bass Eka Putra adhy Suryanto	181
M.Eko Pujo Sakti & Istri	175
Febrian Nuzulul Arsya & Istri	107
Rifaldi Wahyu Putra	102
Eka Retno Ardianti	55
M Fahmi Suyuti	19
Dinas PU Banyuwangi	180
Badan Pendapatan Daerah Banyuwangi	142
Inspektorat Banyuwangi	76
Keluarga Aseph (9F) 	38
Vanadia Anisa	56
Angelia Septa	42
Rizka Ilmawati	126"""

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