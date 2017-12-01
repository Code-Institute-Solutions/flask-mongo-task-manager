import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://admin:admin@ds123926.mlab.com:23926/task_manager'

mongo = PyMongo(app)


@app.route('/get_tasks')
def get_tasks():
    _tasks = mongo.db.tasks.find()
    task_list = [task for task in _tasks]
    return render_template('tasks.html', tasks = task_list)
    
@app.route('/add_task')
def add_task():
    _categories = mongo.db.categories.find()
    category_list = [category for category in _categories]
    return render_template('addtask.html', categories = category_list )
    

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

    
