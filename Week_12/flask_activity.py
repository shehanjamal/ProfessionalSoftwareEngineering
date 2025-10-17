from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Flask</h1>"

@app.route("/bye")
def bye():
    return "<h1>Goodbye Flask</h1>"

@app.route("/username/<name>")
def data(name):
    return f"<h1>Hello {name} is learning flask.</h1>"

@app.route('/cal/<int:number>')
def show_square(number):
    return f"The square of {number} is {number**2}"

@app.route('/link')
def link():
    image_url = url_for('static', filename='koi-fish.png')
    return '<h1><a href="https://pixers.co.nz/posters/koi-fish-ying-yang-symbol-102244746">This is a link</a></h1>' \
    f'<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTBX3F8XrenPAlRbSvx9-c07_o15gkUUB8Rw&s" alt="Koi Fish Ying Yang Symbol" loading="lazy"/>'


if __name__ == "__main__":
    app.run(debug=True)