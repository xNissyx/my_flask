"""
仮想環境に入る用のコピペ
.\venv\Scripts\activate
"""
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# db_path = os.path.join(app.instance_path, 'site.db')
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
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

@app.route('/new', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        new_user = User(username=username, email=email)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e: # エラーハンドリングを再度追加しました
            db.session.rollback()
            print(f"ユーザーの作成中にエラーが発生しました: {e}")
            error_message = "そのユーザー名またはメールアドレスは既に登録されています。"
            return render_template("create.html", error_message=error_message)
    
    return  render_template("create.html")

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    user_to_delete = User.query.get(id) # ユーザーが見つからない場合は404エラーを返す

    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect(url_for('index'))


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
    with app.app_context(): db.create_all()
    app.run(debug=True)         #   debug=Trueにすると開発時は色々いいらしい