from flask import Flask, request
from controllers.user_controller import UserController
from controllers.project_controller import ProjectController

app = Flask(__name__)
app.secret_key = 'BASIC_SECRET_KEY'

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return UserController.render_login()
    return UserController.process_login()

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
def update_project_state(project_id):
    return ProjectController.process_delete_project(project_id)

if __name__ == "__main__":
    app.run(debug=True)