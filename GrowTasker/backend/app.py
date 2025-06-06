from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)


@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = {}
    for key in r.keys():
        value = r.get(key)
        if value:
            tasks[key] = value
    return jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_id = data.get('id')
    text = data.get('text')
    completed = data.get('completed', False)
    date = data.get('date')
    time = data.get('time', '')

    if not all([task_id, text, date]):
        return jsonify({"error": "Missing required fields"}), 400

    task_data = {
        "text": text,
        "completed": completed,
        "date": date,
        "time": time
    }

    r.set(task_id, json.dumps(task_data))
    return jsonify({"status": "success"}), 200


@app.route('/tasks/update', methods=['POST'])
def update_task():
    data = request.get_json()
    task_id = data.get("id")
    completed = data.get("completed")

    task_data = r.get(task_id)
    if not task_data:
        return jsonify({"error": "Task not found"}), 404

    task = json.loads(task_data)
    task["completed"] = completed
    r.set(task_id, json.dumps(task))

    return jsonify({"status": "updated"}), 200


@app.route('/tasks/delete', methods=['POST'])
def delete_task():
    data = request.get_json()
    task_id = data.get("id")
    r.delete(task_id)
    return jsonify({"status": "deleted"}), 200


@app.route('/fruits', methods=['GET'])
def get_fruits():
    count = 0
    for key in r.keys():
        value = r.get(key)
        if value:
            try:
                task = json.loads(value)
                if task.get("completed"):
                    count += 1
            except:
                continue
    return jsonify({"count": count})


if __name__ == "__main__":
    app.run(debug=True)
