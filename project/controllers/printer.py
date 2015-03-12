import os,time,hashlib
from project import app
from flask import render_template,request,Flask,redirect,url_for
from flask.ext.wtf import Form
from wtforms import TextField,validators
from werkzeug import secure_filename

from project.models.Images import Images
images_model = Images()

class CreateForm(Form):
    text=TextField(u'Text:',[validators.Length(min=1,max=20)])
    

@app.route('/')
def start():
    #load model
    images = images_model.find()

    return render_template('printer/index.html',images = images)

@app.route('/upload',methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            save_name = u'/home/vagrant/www/suarez/python/pyproject/websites/flask_mvc/project/static/upload/image/'+filename
            m = hashlib.md5()
            bytes = f.read(1024)  
            while(bytes != b''):  
                m.update(bytes)  
                bytes = f.read(1024) 
                #m.update('123456')
            psw = m.hexdigest()
            # f.save(save_name)
            return psw + u''
        #123
    else:
        data = {'name':'suarez','dateline':int(time.time())}
        images_model.insert(data)
    return '{success:"ok"}'


def allowed_file(filename):
    allowed_extensions = set(['png','jpg'])
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions