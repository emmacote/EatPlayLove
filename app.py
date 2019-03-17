__author__ = 'Emma Cote'
from flask import Flask, render_template, jsonify, request, abort
from model import Food, Session, Serving

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/food", methods=["GET", "POST"])
def food():

    sess = Session()
    msg = ""

    if request.method == "POST":
        new_food = request.json["new_food"]
        food = Food(name=new_food)
        sess.add(food)
        sess.commit()
        msg = "Added new food: {}".format(new_food)
    else:
        # GET method message
        msg = "Retrieved list of all foods for this user."


    food_list = [dict(id=food.id, name=food.name) for food in sess.query(Food).all()]
    return_data = dict(msg=msg, foods=food_list)
    return jsonify(return_data)


@app.route("/serving", methods=["POST"])
def add_serving():
    from datetime import datetime

    json_data = request.json
    food_id = json_data.get("food_id")
    portions = json_data.get("portions")

    sess = Session()
    food = sess.query(Food).filter_by(id=food_id).one()
    serving = Serving(date=datetime.now(), qty=portions, food=food)
    sess.add(serving)
    sess.commit()

    msg = "{} serving of {} recorded.".format(portions, food.name)
    return jsonify(dict(msg=msg))


if __name__ == '__main__':
    app.run()
