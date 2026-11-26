from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! I'm using Flask."

@app.route("/higashi")
def higashi():
    return "東のページです！自治会の会計をLINEで楽にするサービスを作っています。"

@app.route("/Kimura")
def Kimura():
    return "Kimuraのページです！自治会をらくにするよ！！"

@app.route("/akiyama")
def akiyama():
    return "こんにちは＾＾"

@app.route("/Chu")
def Chu():
    return "yahho"

@app.route("/a”-１")
def a”-１():
    return "一人目できたかも"
