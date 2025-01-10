from flask import Flask, request
from controllers.user_controller import UserController
from controllers.project_controller import ProjectController
from controllers.task_controller import TaskController

app = Flask(__name__)
app.secret_key = 'BASIC_SECRET_KEY'

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return UserController.render_login()
    return UserController.process_login()

@app.route("/logout", methods=["GET"])
def logout():
    if request.method == "GET":
        return UserController.process_logout()

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return UserController.render_signup()
    return UserController.process_signup()

@app.route("/projects", methods=["GET"])
def render_projects():
    return ProjectController.render_projects_list()

@app.route("/projects/create", methods=["GET", "POST"])
def create_project():
    if request.method == "GET":
        return ProjectController.render_create_project_form()
    return ProjectController.process_create_project()

@app.route("/projects/finish/<int:project_id>", methods=["POST"])
def process_project_state_update(project_id):
    return ProjectController.process_update_state(project_id)

@app.route("/projects/delete/<int:project_id>", methods=["POST"])
def process_project_delete(project_id):
    return ProjectController.process_delete_project(project_id)

@app.route("/tasks/<int:project_id>", methods=["GET"])
def render_tasks(project_id):
    return TaskController.render_tasks_list(project_id)

@app.route("/tasks/create/<int:project_id>", methods=["GET", "POST"])
def create_task(project_id):
    if request.method == "GET":
        return TaskController.render_create_task(project_id)
    return TaskController.process_create_task(project_id)

@app.route("/tasks/<int:project_id>/finish/<int:task_id>", methods=["POST"])
def process_task_state_update(project_id, task_id):
    return TaskController.process_update_state(project_id, task_id)

@app.route("/tasks/<int:project_id>/delete/<int:task_id>", methods=["POST"])
def process_task_delete(project_id, task_id):
    return TaskController.process_delete_task(project_id, task_id)

if __name__ == "__main__":
    app.run(debug=True)