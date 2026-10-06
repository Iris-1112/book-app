from flask import Flask, render_template, request, redirect
from database import get_all_mood_tags, initialize_database, get_all_books, add_book, tag_book

app = Flask(__name__)

@app.route('/')
def home():
    books = get_all_books()
    return render_template('home.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        status = request.form['status']
        new_book_id = add_book(title, author, status)
        selected_tags = request.form.getlist('moods')
        for tag_id in selected_tags:
            tag_book(new_book_id, tag_id)
        return redirect('/')
    moods = get_all_mood_tags()
    return render_template('add.html', moods=moods)

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)