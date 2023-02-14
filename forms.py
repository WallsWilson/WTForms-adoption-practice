from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField 
from wtforms.validators import InputRequired, Optional, EqualTo, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators = [InputRequired()])
    species = StringField("Species", validators = [InputRequired(), EqualTo('cat', 'dog', 'porcupine')])
    photo_URL = StringField("Photo URL", validators = [Optional(), URL()]) 
    age = IntegerField("Age", validators = [NumberRange(min=0, max=30)])
    notes = StringField("Notes")