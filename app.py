import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://admin:admin@ds123926.mlab.com:23926/task_manager'

mongo = PyMongo(app)


#---------------------Tasks------------------------- 

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
    
@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks =  mongo.db.tasks
    
    checked_urgent = request.form.get("is_urgent", None)
    if checked_urgent:
        checked_urgent = True
    else:
         checked_urgent = False
    
    task_description = request.form.get("task_description", None)
    due_date = request.form.get("due_date", None)
    
    task_doc = {
        'task_name': request.form['task_name'],
        'category_name': request.form['category_name'],
        'task_description': task_description,
        'due_date': due_date,
        'is_urgent': checked_urgent
    }
    
    tasks.insert_one(task_doc)
    return redirect(url_for('get_tasks'))
    

@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    _task =  mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    _categories = mongo.db.categories.find()
    category_list = [category for category in _categories]
    return render_template('edittask.html', task =_task, categories = category_list)
    
 
@app.route('/update_task/<task_id>', methods=['POST'])
def update_task(task_id):
    tasks =  mongo.db.tasks
    
    checked_urgent = request.form.get("is_urgent", None)
    if checked_urgent:
        checked_urgent = True
    else:
         checked_urgent = False
    
    task_description = request.form.get("task_description", None)
    due_date = request.form.get("due_date", None)
    
    tasks.update(
        { "_id":ObjectId(task_id)},
        {'task_name': request.form['task_name'],
        'category_name': request.form['task_name'],
        'task_description':task_description,
        'due_date': due_date,
        'is_urgent' : checked_urgent
    })
    return redirect(url_for('get_tasks'))
    
@app.route('/delete_task/<task_id>')    
def delete_task(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('get_tasks'))
    
#---------------------Categories------------------------- 

@app.route('/get_categories')  
def get_categories():
    _categories = mongo.db.categories.find()
    category_list = [category for category in _categories]
    return render_template('categories.html', categories = category_list)
    
@app.route('/edit_category/<category_id>')    
def edit_category(category_id):
    _category = mongo.db.categories.find_one({'_id': ObjectId(category_id)})
    return render_template('editcategory.html', category = _category)
    
@app.route('/update_category/<category_id>', methods=['POST']) 
def update_category(category_id):
    _categories = mongo.db.categories
    _categories.update(
        {"_id": ObjectId(category_id)},{ "category_name": request.form["category_name"]})
    return redirect(url_for("get_categories"))
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

    
