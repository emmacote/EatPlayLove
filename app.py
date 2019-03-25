__author__ = 'Emma Cote'
from flask import Flask, render_template, jsonify, request, abort
from sqlalchemy import Table, Column, Integer, String, Float, create_engine, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


db_url = "sqlite:///datastore.db"
eng = create_engine(db_url)
Base = declarative_base(bind=eng)


class Food(Base):
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class Serving(Base):
    __tablename__ = "servings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    food_id = Column(ForeignKey("foods.id"))
    qty = Column(Integer)
    food = relationship("Food")


class WeighIn(Base):
    __tablename__ = "weighins"
    id = Column(Integer, primary_key=True, autoincrement=True)
    weight = Column(Float)


Session = sessionmaker(bind=eng)
Base.metadata.create_all(eng)


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


@app.route("/weight", methods=["POST"])
def add_weight():
    json_data = request.json
    new_weight = json_data.get("new_weight", "0")
    new_weight = float(new_weight)

    if new_weight:
        sess = Session()
        weigh_in = WeighIn(weight=new_weight)
        sess.add(weigh_in)
        sess.commit()
        stub_res = {"stub": "stub result... adding weight: {}".format(new_weight)}
        return jsonify(stub_res)
    else:
        abort(400)




if __name__ == '__main__':
    app.run()
