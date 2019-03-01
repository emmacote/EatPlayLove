__author__ = 'Emma Cote'
from flask import Flask, render_template, jsonify, request, abort
from model import Food, Session

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/food", methods=["GET", "POST"])
def food():
    sess = Session()
    if request.method == "GET":
        food_obs = sess.query(Food).all()
        foods = []
        for food in food_obs:
            foods.append(food.name)


        res = dict(foods=foods)
        return jsonify(res)

    elif request.method == "POST":
        new_food = request.json["new_food"]
        food = Food(name=new_food)
        sess.add(food)
        sess.commit()

        food_list = [food.name for food in sess.query(Food).all()]

        msg = "Added new food: {}".format(new_food)
        return_data = dict(msg=msg, foods = food_list)
        return jsonify(return_data)

    else:
        abort(400)


if __name__ == '__main__':
    app.run()
