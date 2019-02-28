__author__ = 'Emma Cote'
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/food", methods=["GET"])
def food():
    from model import Session, Food
    sess = Session()
    foods = sess.query(Food).all()
    food_list = [food.name for food in foods]
    return jsonify(foods=food_list)


if __name__ == '__main__':
    app.run()
