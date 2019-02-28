__author__ = 'Emma Cote'
from flask import Flask, render_template, jsonify
from model import Food, Session

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/food", methods=["GET"])
def food():
    sess = Session()
    food_obs = sess.query(Food).all()
    foods = []
    for food in food_obs:
        foods.append(food.name)


    res = dict(foods=foods)
    return jsonify(res)


if __name__ == '__main__':
    app.run()
