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

orgs = [
    'National Audubon Society', 'Maine Department of Inland Fisheries and Wildlife', 'Manomet, USFWS', 'U.S.F.W.S',
    'U.S. Fish and Wildlife Service, Division of Migratory Birds', 'USFWS Region 7 Migratory Birds, Manomet', 'New Jersey Audubon', 'USFWS',
    'Fundación Inalafquen / International Conservation Fund of Canada', 'Audubon Connecticut'
]

costs = [
    2600000, 600000, 522000, 500521,
    500000, 455000, 400000, 342000,
    298428, 240000
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500"]

names = [ 
    'Red Knot', 'American_Oystercatcher', 'Semipalmated_Sandpiper', 'Ruddy_Turnstone', 
    'Sanderling', 'Whimbrel', 'Wilsons_Plover', 'Greater_Yellowlegs',
    'Lesser_Yellowlegs', 'American_Golden_Plover'
]

numbers = [ 
    47, 44, 42, 37, 37,
    35, 33, 32, 32, 32
]

labels = [
    'Eastern Arctic and Sub Arctic', 'Canada and North Eastern US', 'Mid Atlantic and Southern US', 'Northern South America', 'Caribbean', 'Southern South America'
]

values = [
    3, 12, 32, 16, 11, 6
]

colors_1 = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF", "#DDDDDD"
]
 




@app.route('/')
def index():
    data = db.read(None)
    return render_template('index.html', data = data)

@app.route('/dashboard/')
def dashboard():
    data = db.dashboard(None)
    return render_template('dashboard.html', data = data, colors = colors, orgs = orgs, costs = costs, names=names, numbers=numbers)

    #, orgs = orgs, costs = costs, colors = colors, species, species_number, 
    #return render_template('dashboard.html', data = data, labels=labels, colors=colors, values=values, set=zip(values, labels, colors), max=170000)

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