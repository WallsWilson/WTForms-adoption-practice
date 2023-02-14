from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_intro'
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def root():
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pets():
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_URL = form.photo_URL.data
        age = form.age.data
        notes = form.notes.data
        flash(f"Added new pet: {name}, {species}, {photo_URL}, {age}, {notes}")
        return redirect("/")
    else:
        return render_template("pet_add_form.html", form=form)