"""
Contains definition and business logic for each route handled by the package
"""

from flask import Blueprint, render_template, request, redirect, url_for

from .config import ADMIN_NAME
from .controller import OwnerController, PetController

# Blueprints in flask are used to de-couple application into smaller
# re-usable components. Blueprints are registered with the flask
# application
bp = Blueprint('view', __name__, url_prefix='/')


@bp.route("/", methods=["GET", "POST"])
def welcome():
    """
    GET: Returns welcome.html template
    POST: Inserts owner with the given fullname in the database
    if it does not exist. Then, redirects the owner to the home page
    (home.html). If given fullname belongs to the admin then redirects to
    admin page (admin.html)
    """
    if request.method == "POST":
        fullname = request.form.get('fullname')

        if fullname == ADMIN_NAME:
            return redirect(url_for('view.admin'))

        fullname_stripped = fullname.strip()
        owner_o = OwnerController.get_owner(fullname_stripped)
        if not owner_o:
            owner_o = OwnerController.insert_owner(fullname_stripped)
        return redirect(url_for('view.home', username=owner_o.username))

    return render_template("welcome.html")


@bp.route("/admin", methods=["GET"])
def admin():
    """
    Returns admin page, with the list of all the pets
    with their owners.
    """

    pets = PetController.get_all()
    return render_template("admin.html", pets=[pet.serialize for pet in pets])


@bp.route("/home/<username>", methods=["GET"])
def home(username):
    """
    Returns home page, with list of all the pets belonging to the
    owner identified by given username.
    """
    pets = OwnerController.get_pets(username)
    return render_template("home.html", username=username, pets=[pet.serialize for pet in pets])


@bp.route("/buy", methods=["POST"])
def buy_pet():
    """
    Inserts pets recorded with the owner who bought the pet in the database
    """

    pet_type = request.form.get('pet')
    owner_username = request.form.get('username')
    owner_o = OwnerController.get_owner(identifier=owner_username)
    PetController.insert_pet(pet_type, owner_o.fullname)

    return redirect(url_for('view.home', username=owner_username))
