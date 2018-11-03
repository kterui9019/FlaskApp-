#Flask本体
from flask import Flask
#リクエストメソッドを扱う
from flask import request
#テンプレートエンジンを使う
from flask import render_template
#ファイル名を安全にする
from werkzeug.utils import secure_filename

from random import random

# Flaskをインスタンス化　引数はアプリ名
#__name__にファイル名（app.py）が入る
app = Flask(__name__)

#ルーティングを記述
#@app.route('/')なら~/（ルート）、('/hoge')なら~/hogeにアクセスしたときの処理

#同じURLでもGET/POSTで処理が変わる様子
@app.route('/hoge', methods=['GET'])
def hoge():
    return 'hoge!'

@app.route('/hoge', methods=['POST'])
def Hoge():
    return 'Hoge'

@app.route('/foo/')
def foo():
    return 'foo!'

@app.route('/fuga')
def fuga():
    return 'fuga!'

#テンプレートエンジン
#@app.route引数の<>内に書いたものがメソッドに渡される
#titleメソッドは<title>をtitleとして受け取る
#returnでrender_templateを返す　tmplates内のindex.htmlにtitleに入ってる文字列をtitleとして渡す
@app.route('/title/<title>')
def title(title):
    return render_template('index.html', title=title)


#URLのパラメータ値を取得する
#/search?=以下の文字を取得してくる
@app.route('/search')
def search():
    q = request.args.get('q', '')
    return q

#ログインフォームへのGETリクエスト
#login.htmlのテンプレートエンジンを使う
@app.route('/login',methods=['GET'])
def render_form():
    return render_template('login.html')

#login.htmlでのPOSTリクエストに対するルーティング
#emailとusernameをcheck.htmlにわたす
@app.route('/login',methods=['POST'])
def login():
    if request.form['username'] and request.form['email']:
        return render_template('check.html', email=request.form['email'], username=request.form['username'])
    else:
        return render_template('error.html')

#/uploadのGETリクエストに対するルーティング
#upload.htmlのテンプレートエンジンを使う
@app.route('/upload', methods=['GET'])
def render_upload_form():
    return render_template('upload.html')

#/uploadのPOSTリクエストに対するルーティング
#変数ｆに画像ファイルを格納したあと、安全なファイル名として保存する
#保存した画像ファイルをresult.htmlにわたす
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.form['name'] and request.files['image']:
        f = request.files['image']
        filepath = 'static/' + secure_filename(f.filename)
        f.save(filepath)
        return render_template('result.html', name=request.form['name'], image_url=filepath)

@app.route('/')
def index():
    return render_template('index.html', random=random())

@app.route('/list/')
def listing():
    return render_template('index2.html', l=["Hoge","Fuga","Foo"])

@app.route('/dict')
def dictionary():
    return render_template('index3.html', d=[{"name":"Hoge", "value":"1"}, {"name":"Fuga", "value":"2"}, {"name":"foo", "value":"3"}])

@app.route('/usetheme')
def usetheme():
    return render_template('index4.html', title="Hoge", message="Fuga")