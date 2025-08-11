"""
仮想環境に入る用のコピペ
.\venv\Scripts\activate
"""
from flask import Flask, render_template         #   Flask, rendertemplatesをインポート
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# 'sqlite:///site.db' は、プロジェクトのルートに 'site.db' というファイル名でDBを作成するという意味
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# ③ SQLAlchemyのインスタンスを作成
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # プライマリキー
    username = db.Column(db.String(80), unique=True, nullable=False) # ユニークな文字列
    email = db.Column(db.String(120), unique=True, nullable=False) # ユニークな文字列

    def __repr__(self):
        # オブジェクトを文字列で表現する方法を定義
        return f'<User {self.username}>'

"""
デコレーター
()内のURLにアクセスしたときに、その中の関数を実行
"""
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

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