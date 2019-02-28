__author__ = 'Emma Cote'
from flask import Flask, render_template, jsonify


app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/food", methods=["GET"])
def food():
    stub_result = dict(foods="milk oatmeal water pickles".split())
    return jsonify(stub_result)


if __name__ == '__main__':
    app.run()
