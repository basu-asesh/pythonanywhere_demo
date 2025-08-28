from flask import render_template
from . import core_bp

@core_bp.route("/")
def home():
    return "Hello from Flask on pythonanywhere!"


@core_bp.route("/1")
def f1():
    return render_template("1.html") # from root templates folder

@core_bp.route("/2")
def index():
    return render_template("core/index.html") # from per bluprint templates folder