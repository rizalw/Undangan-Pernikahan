const CACHE_KEY = "language_history";

function changeLanguage(){
    let lang = localStorage.getItem(CACHE_KEY);
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
        data22 = document.querySelector(".pesan")
        data23 = document.querySelector(".pesan.tidak")
        data24 = document.querySelector(".buka > a")
        data25 = document.querySelector(".detail-overlay")
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
        data22.innerHTML = "Terima kasih sudah melakukan konfirmasi.<br>Kami tunggu kehadirannya :)"
        data23.innerHTML = "Tidak apa-apa jika tidak bisa hadir, kami minta doa dan harapannya agar semua berjalan lancar"
        data24.innerHTML = "Buka"
        data25.innerHTML = "Tanpa mengurangi rasa hormat, doa dan support dapat diberikan dalam bentuk dana ke rekening berikut :"
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
        data22 = document.querySelector(".pesan")
        data23 = document.querySelector(".pesan.tidak")
        data24 = document.querySelector(".buka > a")
        data25 = document.querySelector(".detail-overlay")
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
        data22.innerHTML = "Thank you for confirming.<br>We look forward to welcoming you :)"
        data23.innerHTML = "It's okay if you can't attend, we ask for your prayers and hopes so that everything goes smoothly"
        data24.innerHTML = "Open"
        data25.innerHTML = "Without reducing respect, prayers and support can be given in the form of funds to the following account :"
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

function bisa(){
    let data = document.querySelector(".jumlah")
    let data2 = document.querySelector(".bisa")
    let data3 = document.querySelector(".tidak-bisa")
    let data4 = document.querySelector(".konfirmasi > a")
    data.style.display = "flex";
    data2.style.opacity = "1";
    data3.style.opacity = "0.25";
    data4.target = "_blank"
    data4.href = "/download"
}
function tidakBisa(){
    let data = document.querySelector(".bisa")
    let data2 = document.querySelector(".tidak-bisa")
    let data3 = document.querySelector(".jumlah")
    data.style.opacity = "0.25";
    data2.style.opacity = "1";
    data3.style.display = "none"
}

function kurang(){
    let data = document.querySelector(".mid > p")
    let nilai = Number(data.textContent)
    if (nilai === 2){
        nilai -= 1
    }
    data.innerHTML = String(nilai)
}

function tambah(){
    let data = document.querySelector(".mid > p")
    let nilai = Number(data.textContent)
    if (nilai === 1){
        nilai += 1
    }
    data.innerHTML = String(nilai)
}

function confirm(){
    let data3 = document.querySelector(".konfirmasi > a")
    let lang = localStorage.getItem(CACHE_KEY)
    let kiri = document.querySelector(".bisa")
    let kanan = document.querySelector(".tidak-bisa")
    let data2 = document.querySelector(".konfirmasi")
    let pesan = document.querySelector(".pesan.hadir")
    let tidakDatang = document.querySelector(".pesan.tidak")
    let jumlah = document.querySelector(".jumlah")
    // ngecek apa udah mencet tombol konfirmasi atau belum
    if (data3.textContent === "Konfirmasi" || data3.textContent === "Confirm"){
        // ngecek apa udah mencet tombol bisa (otomatis tombol belum bisa juga belum dipencet)
        if (kiri.style.opacity === ""){
            return ""
        }
        data2.style.background = "#4682B4" 
        data3.style.color = "#ffff" 
        if (lang === 'IN'){
            data3.innerHTML = "Ubah"
        } else {
            data3.innerHTML = "Change"
        }
        jumlah.style.display = "none";
        kiri.style.display = "none";
        kanan.style.display = "none";
        //ngecek yang dipencet apa bisa atau tidak bisa
        if (kiri.style.opacity === "1"){
            pesan.style.display = "block";
        } else {
            let overlay = document.querySelector(".overlay")
            let overlaybg = document.querySelector(".overlay-bg")
            tidakDatang.style.display = "block";
            // overlay.style.setProperty('display', 'flex', 'important');
            overlaybg.style.display = "block";
            overlay.style.display = "flex";
        }
    //ketika tombolnya adalah ubah
    } else {
        data2.style.background = "none" 
        data3.style.color = "#4682B4" 
        kiri.style.display = "flex";
        kiri.style.opacity = "1"
        kanan.style.opacity = "1"
        kanan.style.display = "flex";
        jumlah.style.display = "flex";

        if (lang === 'IN'){
            data3.innerHTML = "Konfirmasi"
        } else {
            data3.innerHTML = "Confirm"
        }
        console.log(tidakDatang.style.display)
        //Ngecek apakah kondisinya abis mencet bisa atau tidak bisa
        if (pesan.style.display === "block"){
            data3.target = ""
            data3.href = "javascript:void()"
            pesan.style.display = "none";
        }
        else if(tidakDatang.style.display === "block"){
            tidakDatang.style.display = "none";
        }

    }
}

function closeOverlay(){
    let overlay = document.querySelector(".overlay")
    let overlaybg = document.querySelector(".overlay-bg")
    overlay.style.display = "none";
    overlaybg.style.display = "none";
}

function closeCover(){
    let cover = document.querySelector(".cover-page")
    let music = document.querySelector("#audio")
    cover.style.display = "none"
    music.play()
}

function countdown(){
    let countDownDate = new Date("sep 23, 2021 08:00:00").getTime();

    // Run myfunc every second
    let myfunc = setInterval(function() {

    let now = new Date().getTime();
    let timeleft = countDownDate - now;
        
    // Calculating the days, hours, minutes and seconds left
    let days = Math.floor(timeleft / (1000 * 60 * 60 * 24));
    let hours = Math.floor((timeleft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((timeleft % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((timeleft % (1000 * 60)) / 1000);
        
    // Result is output to the specific element
    document.getElementById("days").innerHTML = days 
    document.getElementById("hours").innerHTML = hours 
    document.getElementById("mins").innerHTML = minutes 
    document.getElementById("secs").innerHTML = seconds 
        
    // Display the message when countdown is over
    if (timeleft < 0) {
        clearInterval(myfunc);
        document.getElementById("days").innerHTML = "0"
        document.getElementById("hours").innerHTML = "0" 
        document.getElementById("mins").innerHTML = "0"
        document.getElementById("secs").innerHTML = "0"
    }
    }, 1000);
}
putHistory();