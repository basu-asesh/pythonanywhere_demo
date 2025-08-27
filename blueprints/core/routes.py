from flask import render_template
from . import core_bp

@core_bp.route("/")
def index():
    return render_template("core/index.html")
