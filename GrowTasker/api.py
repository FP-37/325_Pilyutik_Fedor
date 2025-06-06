import requests
import json
from pathlib import Path

API_URL = "http://127.0.0.1:5000"
LOCAL_FILE = "local_fallback.json"
local_file_path = Path(LOCAL_FILE)


def save_local_data(task_id, task_data):
    data = {}
    if local_file_path.exists():
        with local_file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    data[task_id] = task_data
    with local_file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f)


def load_local_data():
    if local_file_path.exists():
        with local_file_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def delete_local_task(task_id):
    if local_file_path.exists():
        with local_file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if task_id in data:
            del data[task_id]
            with local_file_path.open("w", encoding="utf-8") as f:
                json.dump(data, f)


def get_tasks():
    try:
        response = requests.get(f"{API_URL}/tasks")
        if response.status_code == 200:
            raw = response.json()
            return {k: json.loads(v) for k, v in raw.items() if isinstance(v, str)}
    except:
        return load_local_data()
    return {}


def add_task(task_data):
    task_id = task_data.get("id")
    try:
        response = requests.post(f"{API_URL}/tasks", json=task_data)
        return response.status_code == 200
    except:
        save_local_data(task_id, task_data)
        return False


def update_task(task_id, completed):
    try:
        response = requests.post(f"{API_URL}/tasks/update", json={
            "id": task_id,
            "completed": completed
        })
        return response.status_code == 200
    except:
        tasks = load_local_data()
        if task_id in tasks:
            tasks[task_id]["completed"] = completed
            save_local_data(task_id, tasks[task_id])
        return False


def delete_task(task_id):
    try:
        response = requests.post(f"{API_URL}/tasks/delete", json={"id": task_id})
        return response.status_code == 200
    except:
        delete_local_task(task_id)
        return False


def get_fruit_count():
    try:
        response = requests.get(f"{API_URL}/fruits")
        if response.status_code == 200:
            return response.json().get("count", 0)
    except:
        return 0
    return 0
