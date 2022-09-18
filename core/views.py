from flask import Blueprint, render_template, request, redirect, url_for
from .controller import OwnerController, PetController
from .config import ADMIN_NAME

bp = Blueprint('view', __name__, url_prefix='/')


@bp.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        fullname = request.form.get('fullname')

        if fullname == ADMIN_NAME:
            return redirect(url_for('view.admin'))

        fullname_stripped = fullname.strip()
        owner_controller = OwnerController()
        owner_o = owner_controller.get_owner(fullname_stripped)
        if not owner_o:
            owner_o = owner_controller.insert_owner(fullname_stripped)
        return redirect(url_for('view.home', username=owner_o.username))

    return render_template("welcome.html")


@bp.route("/admin")
def admin():
    pet_controller = PetController()
    pets = pet_controller.get_all()
    return render_template("admin.html", pets=[pet.serialize for pet in pets])


@bp.route("/home/<username>")
def home(username):
    controller = OwnerController()
    pets = controller.get_pets(username)
    return render_template("home.html", username=username, pets=[pet.serialize for pet in pets])


@bp.route("/buy", methods=["POST"])
def buy_pet():
    pet_type = request.form.get('pet')
    owner_username = request.form.get('username')
    owner_controller = OwnerController()
    owner_o = owner_controller.get_owner(identifier=owner_username)

    if owner_o:
        pet_controller = PetController()
        pet_controller.insert(pet_type, owner_o.fullname)

    return redirect(url_for('view.home', username=owner_username))



