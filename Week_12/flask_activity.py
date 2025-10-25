from flask import Flask, render_template,jsonify

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
    return '<h1><a href="https://pixers.co.nz/posters/koi-fish-ying-yang-symbol-102244746">This is a link</a></h1>' \
    f'<img src="https://drive.google.com/uc?export=view&id=1HBvfqy1yO2Oop_IL9P3qnw5aOBsHJNnv" alt="Koi Fish Ying Yang Symbol" loading="lazy"/>'

@app.route("/home_page")
def home_page():
    return render_template("./index.html")

@app.route('/temperature_calculator/<int:temp_1>/<conversion_type>')
def temperature_calculator(temp_1, conversion_type):
    if conversion_type == "c_to_f":
        converted_temp = (temp_1 * 9/5) + 32
    elif conversion_type == "f_to_c":
        converted_temp = (temp_1 - 32) * 5/9
    elif conversion_type == "c_to_k":
        converted_temp = temp_1 + 273.15
    elif conversion_type == "k_to_c":
        converted_temp = temp_1 - 273.15
    elif conversion_type == "f_to_k":
        converted_temp = (temp_1 - 32) * 5/9 + 273.15
    elif conversion_type == "k_to_f":
        converted_temp = (temp_1 - 273.15) * 9/5 + 32
    else:
        return jsonify({"error": "Invalid conversion type"}), 400

    return jsonify({"converted_temp": round(converted_temp, 2)})

if __name__ == "__main__":
    app.run(debug=True)