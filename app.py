from flask import Flask, render_template, request 
from config import Config
from models.user import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Secure Login System is Running!"
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return "submitted!"
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)