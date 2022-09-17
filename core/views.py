from flask import Blueprint, Flask, render_template, request, redirect, url_for

bp = Blueprint('view', __name__, url_prefix='/')


@bp.route("/", methods=["GET", "POST"])
def welcome():

    if request.method == "POST":
        fullname = request.form.get('fullname')
        return redirect(url_for('view.home', username=fullname.lower().replace(' ', '')))
    else:
        return render_template("welcome.html")


@bp.route("/home/<username>")
def home(username):
    return render_template("home.html", username=username, pets=["Pet1"])

