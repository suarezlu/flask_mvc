from project import app
from flask import render_template,request
from flask.ext.wtf import Form
from wtforms import TextField,validators

class CreateForm(Form):
    text=TextField(u'Text:',[validators.Length(min=1,max=20)])
    

@app.route('/')
def start():
    #load model
    from project.models.Printer import Printer
    print_model=Printer()
    msg=print_model.get_str()
    return render_template('printer/index.html',msg=msg)