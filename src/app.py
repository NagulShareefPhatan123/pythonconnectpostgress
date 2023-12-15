from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  # Import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nagul.n.pathan:123@localhost:5432/todo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    comments = db.Column(db.Text)

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todos_list = [{'id': todo.id, 'task': todo.task, 'done': todo.done, 'created_date': todo.created_date, 'end_date': todo.end_date, 'comments': todo.comments} for todo in todos]
    return jsonify({"todos": todos_list})

@app.route('/todos', methods=['POST'])
def add_todo():
    if not request.json or 'task' not in request.json:
        return jsonify({"error": "Invalid request"}), 400

    new_todo = Todo(
        task=request.json['task'],
        done=request.json.get('done', False),
        end_date=request.json.get('end_date'),
        comments=request.json.get('comments')
    )

    db.session.add(new_todo)
    db.session.commit()

    return jsonify({"todo": {"id": new_todo.id, "task": new_todo.task, "done": new_todo.done, 'created_date': new_todo.created_date, 'end_date': new_todo.end_date, 'comments': new_todo.comments}}), 201

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"todo": {"id": todo.id, "task": todo.task, "done": todo.done}})

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    data = request.get_json()

    if 'task' in data:
        todo.task = data['task']
    if 'done' in data:
        todo.done = data['done']
    if 'end_date' in data:
        todo.end_date = data['end_date']
    if 'comments' in data:
        todo.comments = data['comments']

    db.session.commit()

    return jsonify({
        "todo": {
            "id": todo.id,
            "task": todo.task,
            "done": todo.done,
            "created_date": todo.created_date,
            "end_date": todo.end_date,
            "comments": todo.comments
        }
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
