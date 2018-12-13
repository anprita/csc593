'''
Created on Nov 26, 2018

@author: prita
'''

from flask import Flask, Markup, flash, render_template, redirect, url_for, request, session
from module.database import Database
from pprint import pprint

pprint(globals())
pprint(locals())


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


@app.route('/')
def index():
    data = db.read(None)
    return render_template('index.html', data = data)

@app.route('/dashboard/')
def dashboard():
    data = db.dashboard(None)
    return render_template('dashboard.html', data = data, labels=labels, colors=colors, values=values, set=zip(values, labels, colors), max=170000)

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addproject', methods = ['POST', 'GET'])
def addproject():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new project has been added")
        else:
            flash("A new project can not be added")
            
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);
    print(data)
    
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updateproject', methods = ['POST'])
def updateproject():
    if request.method == 'POST' and request.form['update']:
        
        if db.update(session['update'], request.form):
            flash('A project has been updated')
           
        else:
            flash('A project can not be updated')
        
        session.pop('update', None)
        
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    
@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);
    
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deleteproject', methods = ['POST'])
def deleteproject():
    if request.method == 'POST' and request.form['delete']:
        
        if db.delete(session['delete']):
            flash('A project has been deleted')
           
        else:
            flash('A project can not be deleted')
        
        session.pop('delete', None)
        
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug = True, port=8181, host="127.0.0.1")