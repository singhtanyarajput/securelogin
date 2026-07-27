from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from config import Config
from models.user import db, User
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

db.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
@app.route("/")
def home():
    return "Secure Login System is Running!"
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return "Username or email already exists. Please choose a different one."
        
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        print("=" * 20)
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {hashed_password}")
        print("=" * 20)
        return "User registered successfully!"
    return render_template("register.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if not user:
            return "Invalid Username"
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            return "Invalid username or password."
    return render_template("login.html")
@app.route("/dashboard")
@login_required
def dashboard():
    return f"Welcome {current_user.username} to your dashboard!"
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "You have been logged out."
if __name__ == "__main__":
    app.run(debug=True)