from flask import render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from apli import app,db
from apli.models import Task        #ver porque el importar 'from models import Task' no funciona ->Error: ModuleNotFoundError: No module named 'models'

@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks = tasks)


@app.route('/create-task', methods=['POST'])
def create():
    task = Task(content=request.form['entryTask'], done=False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete/<id>')
def delete(id):
    task = Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/done/<id>')
def done(id):
    task = Task.query.filter_by(id=int(id)).first()
    task.done = not(task.done)
    db.session.commit()
    return redirect(url_for('home'))

    
