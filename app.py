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
tamu_undangan = """KELUARGA BANI HUZAINI	1
ARSITEKTUR UB 2013	2
ALL MEMBER BJ 28	3
DINDA PUTRI & GURUH	4
FEBY VALENTINA	5
VINA ALFI M & SUAMI	6
MELINA PANDAN S	7
FIDIAH AULIA & SUAMI	8
KURNIA CAHYA P	9
REVYANA NAWANG & REZA	10
ANDREA TYA	11
DIASTIKA R & SUAMI	12
SULIS AGUSTIA & SUAMI	13
IRA YULIA ASTUTIK & SUAMI	14
SYAFIRA SALASABILA	15
FAJAR FURQON	16
PUSPA NILA CEMPAKA & SUAMI	17
GABRIELLA S. & SUAMI	18
YUNISA ROSIYANTO	19
TRI YUNI & SUAMI	20
PRATIWI OKTAVIANA & SUAMI	21
FAHMIA TSANIE & SUAMI	22
NUR AZLINA	23
RESTICA	24
UMAMAH AL BATUL	25
ALMAS NUGRAHANINGSIH	26
FARADINA HASAN	27
ARIDA F YASMIN	28
SHOFY AFINA	29
UMI HAJAR KH	30
MARTHA ANGELIA	31
DEWI WIDYA	32
ROHADATUL AISY	33
Anggit Teguh Iman	34
Aji Prisma Arista	35
Aditya Alfian Noor	36
Ainul Fahmi	37
Andreas Bayu Saputra	38
Ari Sulistyo	39
Ageng Gesit Putro Panuntun	40
Bayu Ikhsan Saputra	41
Bentar Randy	42
M. Aden Al Barrie	43
Enggar Tyasto	44
Habib Syarif Dalimunte	45
Joko Purnomo	46
Jundi Izzuddin Alqosam	47
Leo Saputra	48
Sandy Janilandra Irawan	49
Ramadhona Kurniawan	50
Nurul Efendi	51
Wicaksono Sambu Wihikan	52
Wahyu Purba Aji	53
M. Thorig Algomar	54
Dian Ardia Rini	55
Dwika Putra Anugrah	56
Ardiansyah Selian	57
M. Chotibul Umam	58
Ervanda Putra	59
Faisal Wahyu Hidayat	60
R. Alvino Putra Yodi Prasetyo	61
Hadi Susanto	62
Fajar Nurhadi	63
Edi Hartono	64
Muhammad Zakaria	65
Muhammad Zulkarnain	66
Aron Dio Sabatino Akimas	67
Candra Agung Prabowo	68
Vikri Ari Susanto	69
Rifki Setiawan	70
Bass RIFQI Halvyan	71
Bass Eka Putra adhy Suryanto	72
M.Eko Pujo Sakti & Istri	73
Febrian Nuzulul Arsya & Istri	74
Rifaldi Wahyu Putra	75
Eka Retno Ardianti	76
M Fahmi Suyuti	77
Dinas PU Banyuwangi	78
Badan Pendapatan Daerah Banyuwangi	79
Inspektorat Banyuwangi	80
Keluarga Aseph (9F)	81
Vanadia Anisa	82
Angelia Septa	83
Rizka Ilmawati	84
Teknika 02	85
Keluarga Polimarin Jawa Timur	86
Keluarga Polimarin Banyuwangi	87
Alumni Polimarin 02	88"""

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
        # for komen in daftar_komentar:
        #     komen.author = " ".join(komen.author.split("%20"))
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