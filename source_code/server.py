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
    'Red Knot', 'American_Oystercatcher', 'Semipalmated_Sandpiper', 'Ruddy_Turnstone', 
    'Sanderling', 'Whimbrel', 'Wilsons_Plover', 'Greater_Yellowlegs',
    'Lesser_Yellowlegs', 'American_Golden_Plover'
]

values = [
    47, 44, 42, 37, 37,
    35, 33, 32, 32, 32
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

str_labels = [
    'Protect Habitat (dev)', 'Protect Habitat (coast)', 'Reduce Predation', 'Reduce Human Dist.', 
    'Reduce Hunting', 'Climate Change', 'Fill Knowledge Gap'
]

str_values = [
    8, 2, 4, 10,
    6, 3, 9
]

str_colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC"]

pie_labels = [
    'Eastern Arctic and Sub Arctic', 'Canada and North Eastern US', 'Mid Atlantic and Southern US', 'Northern South America', 'Caribbean', 'Southern South America'
]

pie_values = [
    3, 12, 32, 16, 11, 6
]

pie_colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF", "#DDDDDD"
]

doughnut_labels= [
    'National Audubon Society', 'Maine Department of Inland Fisheries and Wildlife', 'Manomet, USFWS', 'U.S.F.W.S',
    'U.S. Fish and Wildlife Service, Division of Migratory Birds', 'USFWS Region 7 Migratory Birds, Manomet', 'New Jersey Audubon', 'USFWS',
    'Fundación Inalafquen / International Conservation Fund of Canada', 'Audubon Connecticut'
]

doughnut_values = [
    2600000, 600000, 522000, 500521,
    500000, 455000, 400000, 342000,
    298428, 240000
]

doughnut_colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500"]


@app.route('/')
def index():
    data = db.read(None)
    return render_template('index.html', data = data)

@app.route('/dashboard/')
def dashboard():
    data = db.dashboard(None)
    return render_template('dashboard.html', data = data, labels=labels, colors=colors, str_values=str_values, str_labels=str_labels, str_colors=str_colors, values=values, set=zip(pie_values, pie_labels, pie_colors), set2=zip(doughnut_values, doughnut_labels, doughnut_colors), max=50)

@app.route('/strategy/')
def strategy():
    data = db.read_strategy(None)
    return render_template('strategy.html', data = data)

@app.route('/species/')
def species():
    data = db.read_species(None)
    return render_template('species.html', data = data)

#@app.route('/organization/')
#def organization():
#    data = db.read(None)
#    return render_template('organization.html', data = data)

#@app.route('/partner/')
#def partner():
#    data = db.read(None)
#    return render_template('partner.html', data = data)

@app.route('/project/')
def project():
    data = db.read(None)
    return render_template('index.html', data = data)

@app.route('/usd/')
def usd():
    data = db.read_usd(None)
    return render_template('project.html', data = data)

@app.route('/cad/')
def cad():
    data = db.read_cad(None)
    return render_template('project.html', data = data)

@app.route('/brl/')
def brl():
    data = db.read_brl(None)
    return render_template('project.html', data = data)

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