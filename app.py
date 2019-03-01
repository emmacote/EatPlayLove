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


    food_list = [food.name for food in sess.query(Food).all()]
    return_data = dict(msg=msg, foods=food_list)
    return jsonify(return_data)



if __name__ == '__main__':
    app.run()
