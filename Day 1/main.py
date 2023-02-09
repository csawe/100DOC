from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(80))
    
    def __repr__(self):
        return f"{self.name} - {self.description}"
    
@app.route("/drinks", methods=["GET"])
def get_drinks():
    drinks = Drink.query.all()
    drinks_list = [{"id":drink.id, "name":drink.name, "description": drink.description} for drink in drinks]
    return jsonify(drinks_list)

@app.route("/drinks/<int:id>", methods=["GET"])
def get_drink(id):
    print("-----------------------------------here")
    drink = Drink.query.get(id)
    if drink:
        return jsonify({"id":drink.id, "name":drink.name, "description": drink.description})
    else:
        return jsonify({"message": "Drink not found"}), 404

@app.route("/drinks", methods=["POST"])
def add_drink():
    data = request.get_json()
    name = data['name']
    description = data['description']
    drink = Drink(name=name, description=description)
    db.session.add(drink)
    db.session.commit()
    return jsonify({"name":drink.name, "description": drink.description})

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)