from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    title = "ようこそ"
    return render_template('index.html', title=title)
if __name__ == '__main__':
    app.run()
