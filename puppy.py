import sys
from flask import Flask, jsonify, abort
from models import db, Puppy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///puppy.db"
db.init_app(app)

# PUPPIES = {
#     "rover": {
#         "name": "Rover",
#         "image_url": "http://example.com/rover.jpg"
#     },
#     "spot": {
#         "name": "Spot",
#         "image_url": "http://example.com/spot.jpg"
#     }
# }


@app.route('/<slug>')
def get_puppy(slug):
    puppy = Puppy.query.filter(Puppy.slug==slug).first_or_404()
    output = {
        "name": puppy.name,
        "image_url": puppy.image_url
    }
    return jsonify(puppy)

if __name__ == "__main__":
    if "createdb" in sys.argv:
        with app.app_context():
            db.create_all()
        print("Database created!")
    else:
        app.run()
