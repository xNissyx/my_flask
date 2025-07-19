# app.py

from flask import Flask

# Flaskアプリケーションのインスタンスを作成します。
# __name__ はPythonがモジュールをどのようにロードしているかを示し、
# Flaskがリソースを見つけるのに役立ちます。
app = Flask(__name__)

# ルートURL (/) にアクセスしたときに実行される関数を定義します。
@app.route('/')
def hello_world():
    # ブラウザに表示される文字列を返します。
    return '<h1>Hello, World! from Flask App!</h1>'

# このスクリプトが直接実行された場合に、開発サーバーを起動します。
if __name__ == '__main__':
    # debug=True にすると、コードの変更が自動的にリロードされ、
    # エラーが発生したときに詳細なデバッグ情報が表示されます。
    app.run(debug=True)