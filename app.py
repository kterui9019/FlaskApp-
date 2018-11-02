from flask import Flask
from flask import request

# Flaskをインスタンス化　引数はアプリ名
#__name__にファイル名（app.py）が入る
app = Flask(__name__)

#ルーティングを記述
#@app.route('/')なら~/（ルート）、('/hoge')なら~/hogeにアクセスしたときの処理
@app.route('/')
def hello_world():
    return """
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <link rel="stylesheet" href="/static/style.css"/>
            </head>
            <body>
                <h1>Hello World</h1>
            </body>
        </html>
    """

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
