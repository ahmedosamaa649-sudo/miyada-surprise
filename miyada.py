# -*- coding: utf-8 -*-

import os
import threading
import webbrowser
import mimetypes
from tkinter import Tk, filedialog
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


PORT = 8000
PASSWORD = "112007"


# ==================================================
# اختيار الصورة والأغنية
# ==================================================

root = Tk()
root.withdraw()

print("اختار الصورة ❤️")

IMAGE_PATH = filedialog.askopenfilename(
    title="اختار صورة ميادة ❤️",
    filetypes=[
        ("Images", "*.jpg *.jpeg *.png *.webp"),
        ("All files", "*.*")
    ]
)

if not IMAGE_PATH:
    print("لم يتم اختيار صورة ❌")
    input("اضغط Enter للخروج...")
    raise SystemExit


print("اختار الأغنية 🎵")

SONG_PATH = filedialog.askopenfilename(
    title="اختار الأغنية 🎵",
    filetypes=[
        ("Audio", "*.mp3 *.wav *.m4a *.ogg"),
        ("All files", "*.*")
    ]
)

if not SONG_PATH:
    print("لم يتم اختيار الأغنية ❌")
    input("اضغط Enter للخروج...")
    raise SystemExit


root.destroy()


# ==================================================
# قراءة الملفات داخل البرنامج
# ==================================================

with open(IMAGE_PATH, "rb") as f:
    IMAGE_DATA = f.read()

with open(SONG_PATH, "rb") as f:
    SONG_DATA = f.read()


IMAGE_TYPE = mimetypes.guess_type(IMAGE_PATH)[0]

if IMAGE_TYPE is None:
    IMAGE_TYPE = "image/jpeg"


SONG_TYPE = mimetypes.guess_type(SONG_PATH)[0]

if SONG_TYPE is None:
    SONG_TYPE = "audio/mpeg"


# ==================================================
# السيرفر
# ==================================================

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        path = self.path.split("?")[0]


        # =========================
        # الصورة
        # =========================

        if path == "/miyada-image":

            self.send_response(200)

            self.send_header(
                "Content-Type",
                IMAGE_TYPE
            )

            self.send_header(
                "Content-Length",
                str(len(IMAGE_DATA))
            )

            self.send_header(
                "Cache-Control",
                "no-cache"
            )

            self.end_headers()

            self.wfile.write(IMAGE_DATA)

            return


        # =========================
        # الأغنية
        # =========================

        if path == "/miyada-song":

            self.send_response(200)

            self.send_header(
                "Content-Type",
                SONG_TYPE
            )

            self.send_header(
                "Content-Length",
                str(len(SONG_DATA))
            )

            self.send_header(
                "Accept-Ranges",
                "bytes"
            )

            self.send_header(
                "Cache-Control",
                "no-cache"
            )

            self.end_headers()

            self.wfile.write(SONG_DATA)

            return


        # =========================
        # الصفحة
        # =========================

        if path == "/":

            html = f"""
<!DOCTYPE html>

<html lang="ar" dir="rtl">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Miyada Surprise ❤️</title>


<style>

body {{
    margin: 0;
    padding: 20px;

    min-height: 100vh;

    background:
    linear-gradient(135deg,#120009,#55002d);

    color: white;

    font-family: Arial, sans-serif;

    display: flex;
    justify-content: center;
    align-items: center;
}}


.box {{
    width: 100%;
    max-width: 550px;

    padding: 30px;

    text-align: center;

    background: rgba(255,255,255,.08);

    border-radius: 25px;

    box-shadow: 0 0 40px rgba(255,0,100,.35);
}}


h1 {{
    font-size: 32px;
}}


input {{
    width: 85%;

    padding: 15px;

    border: 0;

    border-radius: 12px;

    text-align: center;

    font-size: 18px;

    margin: 15px 0;
}}


button {{
    padding: 14px 28px;

    border: 0;

    border-radius: 12px;

    background: #ff2875;

    color: white;

    font-size: 18px;

    cursor: pointer;
}}


#surprise {{
    display: none;
}}


.photo {{
    display: block;

    width: 100%;

    max-width: 430px;

    margin: 20px auto;

    border-radius: 20px;

    box-shadow: 0 0 25px rgba(255,255,255,.2);
}}


.message {{
    text-align: right;

    font-size: 19px;

    line-height: 2;

    background: rgba(0,0,0,.2);

    padding: 20px;

    border-radius: 20px;

    margin: 20px 0;
}}


audio {{
    width: 100%;

    margin: 20px 0;
}}


.error {{
    color: #ff8aad;
}}

</style>

</head>


<body>


<div class="box">


<!-- ================= تسجيل الدخول ================= -->

<div id="login">

<h1>عندي حاجة ليكي ❤️</h1>

<p>

في مفاجأة صغيرة مستنياكي...

<br>

اكتبي الباسورد ❤️

</p>


<input
id="password"
type="password"
placeholder="الباسورد">


<br>


<button onclick="openSurprise()">

افتحي المفاجأة ❤️

</button>


<p id="error" class="error"></p>


</div>



<!-- ================= المفاجأة ================= -->

<div id="surprise">


<h1>ميادة ❤️✨</h1>


<img
class="photo"
src="/miyada-image"
alt="Miyada">


<div class="message">


<div style="text-align:center;font-size:28px;">

ميادة ❤️✨

</div>


عارف إني ساعات كتير بزعلك،
ويمكن أوقات مش بعرف أوصّلك اللي جوايا بالطريقة الصح،
بس ربنا وحده يعلم أنا بحبك قد إيه،
وقد إيه وجودك في حياتي فارق معايا. ❤️

<br><br>


أنا مش عايز منك حاجة كبيرة،
كل اللي نفسي فيه إنك تكوني مرتاحة ومطمنة وإنتِ معايا،
وإنك تعرفي إن مشاعري ناحيتك حقيقية ومن قلبي.

<br><br>


يمكن أغلط، ويمكن أقصر،
بس عمري ما هبطل أحاول أكون أحسن،
وأصلّح أي حاجة تضايقك مني.

<br><br>


لأنك بالنسبة لي مش مجرد شخص بحبه،
إنتِ حد غالي على قلبي
ووجودك بيفرق في يومي. ❤️

<br><br>


نفسي أفضل جنبك في كل لحظة حلوة،
وأكون أول حد تلاقيه وقت ما تحتاجي حد يسمعك أو يطمنك.

<br><br>


ونفسي الأيام اللي جاية تبقى أحلى من كل اللي فات. ✨

<br><br>


أنا مش بوعدك إني هكون كامل،
بس أوعدك إني هفضل أحاول،
وهفضل أقدّر وجودك،
وأحافظ على مكانتك عندي. ❤️

<br><br>


بحبك يا ميادة،
وربنا يعلم قد إيه الكلمة دي صغيرة
قدام كل اللي جوايا ليكي.

<br><br>


❤️❤️❤️✨


</div>


<audio id="song" controls loop>

<source
src="/miyada-song"
type="{SONG_TYPE}">

المتصفح لا يدعم تشغيل الصوت.

</audio>


</div>


</div>



<script>


function openSurprise() {{

    let password =
    document.getElementById("password").value;


    if (password === "{PASSWORD}") {{

        document.getElementById("login").style.display =
        "none";


        document.getElementById("surprise").style.display =
        "block";


        let song =
        document.getElementById("song");


        song.play().catch(function() {{

            console.log("اضغط تشغيل الأغنية");

        }});

    }}


    else {{

        document.getElementById("error").innerText =
        "الباسورد غلط ❤️ حاولي تاني";

    }}

}}


</script>


</body>

</html>
"""


            data = html.encode("utf-8")


            self.send_response(200)


            self.send_header(
                "Content-Type",
                "text/html; charset=utf-8"
            )


            self.send_header(
                "Content-Length",
                str(len(data))
            )


            self.end_headers()


            self.wfile.write(data)

            return


        self.send_response(404)

        self.end_headers()


    def log_message(self, format, *args):

        pass



# ==================================================
# تشغيل الموقع
# ==================================================

server = ThreadingHTTPServer(
    ("127.0.0.1", PORT),
    Handler
)


print("")
print("================================")
print("الموقع اشتغل ❤️")
print("================================")
print("")
print("http://127.0.0.1:8000")
print("")


threading.Thread(
    target=server.serve_forever,
    daemon=True
).start()


webbrowser.open(
    "http://127.0.0.1:8000"
)


input("اضغط Enter للخروج...")
