from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# DATABASE_URI=postgresql://nagul.n.pathan:123@localhost/todo_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nagul.n.pathan:123@localhost:5432/todo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todos_list = [{'id': todo.id, 'task': todo.task, 'done': todo.done} for todo in todos]
    return jsonify({"todos": todos_list})

@app.route('/todos', methods=['POST'])
def add_todo():
    if not request.json or 'task' not in request.json:
        return jsonify({"error": "Invalid request"}), 400

    new_todo = Todo(task=request.json['task'])
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({"todo": {"id": new_todo.id, "task": new_todo.task, "done": new_todo.done}}), 201

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"todo": {"id": todo.id, "task": todo.task, "done": todo.done}})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
