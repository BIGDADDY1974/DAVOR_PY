from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient
import sys,os
app = Flask(__name__)
client = MongoClient('localhost',27017)
db = client.tododb
@app.route('/')
def todo():
    _items = db.tododb.find()
    items = [item for item in _items]
    return render_template('todo.html', items=items)

@app.route('/new', methods=['POST'])
def new():
    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    db.tododb.insert_one(item_doc)
    return redirect(url_for('todo'))

if __name__ == "__main__":
    app.run()
