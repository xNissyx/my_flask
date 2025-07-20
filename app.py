"""
仮想環境に入る用のコピペ
.\venv\Scripts\activate
"""
from flask import Flask         #   Flaskをインポート

app = Flask(__name__)

"""
デコレーター
()内のURLにアクセスしたときに、その中の関数を実行
"""
@app.route('/')
def hello_world():
    return "<h1>ルートページです</h1>"

@app.route('/about')
def about():
    return "Aboutページです"

"""
Flask側の動き
・@app.route()で指定されたデコレーターの部分を解析
・<>で囲われた部分はプレースホルダーとして認識し、変数としてビュー関数へ渡す
"""
@app.route('/user/<username>')  #   動的なURLを作成する方法
def show_user_profile(username):
    return f"{username}さんのページです"

if __name__ == '__main__':
    app.run(debug=True)         #   debug=Trueにすると開発時は色々いいらしい