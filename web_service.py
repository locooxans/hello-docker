fromflask import Flask, render_template, request, redirect

app = Flask(__name__)

# Mesajları geçici bir listede tutuyoruz (veritabanı yerine)
mesajlar = []

@app.route("/", methods=["GET", "POST"])
defindex():
ifrequest.method == "POST":
isim = request.form.get("isim")
mesaj = request.form.get("mesaj")
if isim and mesaj:
mesajlar.append({"isim": isim, "mesaj": mesaj})
returnredirect("/")

returnrender_template("index.html", mesajlar=mesajlar)

if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000)

