from flask import Flask, render_template
from database import initialize_database, get_all_books

app = Flask(__name__)

@app.route('/')
def home():
    books = get_all_books()
    return render_template('home.html', books=books)

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)