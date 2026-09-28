from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>My Book App</h1><p>Coming soon.</p>'

if __name__ == '__main__':
    app.run(debug=True)