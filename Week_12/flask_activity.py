from flask import Flask

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

if __name__ == "__main__":
    app.run(debug=True)