const CACHE_KEY = "language_history";

function changeLanguage(){
    let lang = localStorage.getItem(CACHE_KEY);
    console.log(lang)
    if (lang === "IN"){
        data = document.querySelector(".arti-ayat")
        data2 = document.querySelector(".a")
        data4 = document.querySelector(".a.last")
        data5 = document.querySelector(".keluarga-pengantin-wanita")
        data6 = document.querySelector(".keluarga-pengantin-pria")
        data7 = document.querySelector(".col-head")
        data8 = document.querySelector(".tambah-jadwal")
        data9 = document.querySelector(".e")
        data10 = document.querySelector(".h")
        data11 = document.querySelector(".i")
        data12 = document.querySelector(".bisa > a")
        data13 = document.querySelector(".tidak-bisa > a")
        data14 = document.querySelector(".konfirmasi > a")
        data15 = document.querySelector(".prokes > h1")
        data16 = document.querySelector(".wedding-wish > p")
        data17 = document.querySelector(".continue")
        data18 = document.querySelector(".pernyataan")
        data19 = document.querySelector(".data-lengkap > h3")
        data20 = document.querySelector(".tanggal")
        data21 = document.querySelector(".kirim")
        // fotoprokes = document.querySelector(".prokes > img")
        data.innerHTML = '<i>"Dan di antara tanda-tanda<br>(kebesaran)-Nya ialah Dia menciptakan<br>pasangan-pasangan untukmu dari jenismu<br>sendiri, agar kamu cenderung dan merasa<br>tenteram kepadanya, dan Dia menjadikan di<br>antaramu rasa kasih dan sayang”</i>';
        data2.innerHTML = "Kepada Yth."
        data4.innerHTML = "Kami mengundang Anda untuk berbagi dalam kegembiraan kami dan meminta kehadiran Anda di pesta pernikahan"
        data5.innerHTML = "Putri dari<br>Bapak Akhmad Saeho, S.E.<br>dan<br>Luluk Khomsiyah, S.E., M.Si"
        data6.innerHTML = "Putra dari<br>Bapak Sudarminto, S.Pd., M.Pd.<br>dan<br>Ibu Endang Suliyanti"
        data7.innerHTML = "<td>Hari</td><td>Jam</td><td>Menit</td><td>Detik</td>"
        data8.innerHTML = "Tambah Jadwal"
        data9.innerHTML = "Akad Nikah"
        data10.innerHTML = "Lokasi :"
        data11.innerHTML = "Apakah anda bersedia hadir?"
        data12.innerHTML = "Bisa"
        data13.innerHTML = "Tidak Bisa"
        data14.innerHTML = "Konfirmasi"
        data15.innerHTML = "Protokol Kesehatan"
        data16.innerHTML = "Berikan harapanmu untuk membuat hari ini semakin meriah"
        data17.innerHTML = "Lihat ucapan lainnya"
        data18.innerHTML = "Atas kehadiran dan do’a restu dari bapak/ibu/saudara/I sekalian, kami ucapkan terima kasih<br><br>Dari kami yang berbahagia"
        data19.innerHTML = "Kamis,<br>23 September 2021"
        data20.innerHTML = "23 September 2021"
        data21.innerHTML = "Kirim"
        // fotoprokes.setAttribute("src", "")
    } else if (lang === "EN"){
        data = document.querySelector(".arti-ayat")
        data2 = document.querySelector(".a")
        data4 = document.querySelector(".a.last")
        data5 = document.querySelector(".keluarga-pengantin-wanita")
        data6 = document.querySelector(".keluarga-pengantin-pria")
        data7 = document.querySelector(".col-head")
        data8 = document.querySelector(".tambah-jadwal")
        data9 = document.querySelector(".e")
        data10 = document.querySelector(".h")
        data11 = document.querySelector(".i")
        data12 = document.querySelector(".bisa > a")
        data13 = document.querySelector(".tidak-bisa > a")
        data14 = document.querySelector(".konfirmasi > a")
        data15 = document.querySelector(".prokes > h1")
        data16 = document.querySelector(".wedding-wish > p")
        data17 = document.querySelector(".continue")
        data18 = document.querySelector(".pernyataan")
        data19 = document.querySelector(".data-lengkap > h3")
        data20 = document.querySelector(".tanggal")
        data21 = document.querySelector(".kirim")
        data.innerHTML = '<i>"And of His signs is that He created for you from yourselves mates that you may find tranquility in them; and He placed between you affection and mercy. Indeed in that are signs for a people who give thought."</i>';
        data2.innerHTML = "For"
        data4.innerHTML = "We invite you to share in our joy and request your presence at the wedding of"
        data5.innerHTML = "The Daugther of<br>Mr. Akhmad Saeho, S.E.<br>and<br>Mrs. Luluk Khomsiyah, S.E., M.Si"
        data6.innerHTML = "The Son of<br>Mr. Sudarminto, S.Pd., M.Pd.<br>and<br>Mrs. Endang Suliyanti"
        data7.innerHTML = "<td>Days</td><td>Hours</td><td>Minute</td><td>Seconds</td>"
        data8.innerHTML = "Add to Calendar"
        data9.innerHTML = "Wedding Day"
        data10.innerHTML = "Location :"
        data11.innerHTML = "Would you like to attend?"
        data12.innerHTML = "Yes"
        data13.innerHTML = "No"
        data14.innerHTML = "Confirm"
        data15.innerHTML = "Health Protocol"
        data16.innerHTML = "Give your wish to make this day even more festive"
        data17.innerHTML = "Load more wishes"
        data18.innerHTML = "For your presence and blessings from all of you, we thank you<br><br>From us who are happy"
        data19.innerHTML = "Thursday,<br>23rd September 2021"
        data20.innerHTML = "23rd September 2021"
        data21.innerHTML = "Send"
    }
}

function checkForStorage() {
    return typeof(Storage) !== "undefined"
   }


function putHistory() {
    if (checkForStorage()) {
        if (localStorage.getItem(CACHE_KEY) === null) {
            localStorage.setItem(CACHE_KEY, "IN");
        } else {
            let lang = localStorage.getItem(CACHE_KEY)
            if (lang === "EN"){
                localStorage.setItem(CACHE_KEY, "IN");
            }
        }
        changeLanguage()
    }
 }

function setLanguage(){
    let lang = localStorage.getItem(CACHE_KEY)
    if (lang === "EN"){
        localStorage.setItem(CACHE_KEY, "IN");
    } else {
        localStorage.setItem(CACHE_KEY, "EN");
    }
    changeLanguage()
}
putHistory();