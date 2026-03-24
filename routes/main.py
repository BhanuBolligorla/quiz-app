from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("login.html")

@main_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@main_bp.route("/create_quiz")
@login_required
def create_quiz():
    return render_template("create_quiz.html", user=current_user)

@main_bp.route("/join_quiz")
@login_required
def join_quiz():
    return render_template("join_quiz.html", user=current_user)
