from flask import Flask, render_template, request, redirect, url_for
from app.models import db, Book
from dotenv import load_dotenv
import os
from uuid import UUID

# .envファイルを読み込む
load_dotenv()

# 環境変数からデータベース接続情報を取得
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

app = Flask(__name__)

# SQLAlchemy設定
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

# 本の一覧を表示
@app.route('/')
def index():
    books = Book.query.order_by(Book.created_at.desc()).all()
    return render_template('index.html', books=books)

# 本の詳細を表示
@app.route('/book/<uuid:book_id>')
def view_book(book_id):
    book = Book.query.get_or_404(str(book_id))
    return render_template('view_book.html', book=book)

# 新しい本の作成フォームを表示
@app.route('/create', methods=['GET'])
def show_create_book():
    return render_template('create_book.html')

# 新しい本を作成
@app.route('/create', methods=['POST'])
def create_book():
    title = request.form['title']
    author = request.form['author']
    impression = request.form['impression']
    favorite_flag = bool(request.form.get('favorite_flag'))
    reading_time_minutes = int(request.form['reading_time_minutes'])
    reading_status = request.form['reading_status']
    new_book = Book(
        title=title,
        author=author,
        impression=impression,
        favorite_flag=favorite_flag,
        reading_time_minutes=reading_time_minutes,
        reading_status=reading_status
    )
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('index'))

# 本を削除
@app.route('/book/<uuid:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(str(book_id))
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))
# 本の変更フォームを表示
@app.route('/book/<uuid:book_id>/edit', methods=['GET'])
def show_edit_book(book_id):
    book = Book.query.get_or_404(str(book_id))
    return render_template('edit_book.html', book=book)

# 本の情報を変更
@app.route('/book/<uuid:book_id>/edit', methods=['POST'])
def edit_book(book_id):
    book = Book.query.get_or_404(str(book_id))
    book.title = request.form['title']
    book.author = request.form['author']
    book.impression = request.form['impression']
    book.favorite_flag = bool(request.form.get('favorite_flag'))
    book.reading_time_minutes = int(request.form['reading_time_minutes'])
    book.reading_status = request.form['reading_status']
    db.session.commit()
    return redirect(url_for('index'))

#お気に入りのみを表示する
@app.route('/favorites')
def show_favorites():
    favorite_books = Book.query.filter_by(favorite_flag=True).order_by(Book.created_at.desc()).all()
    return render_template('favorites.html', books=favorite_books)

#任意の文字列でのタイトル検索
@app.route('/search_results')
def show_search_results():
    query = request.args.get('query')
    search_results = Book.query.filter(Book.title.ilike(f'%{query}%')).order_by(Book.created_at.desc()).all()
    return render_template('search_results.html', books=search_results, query=query)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
