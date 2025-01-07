import sqlite3

connection = sqlite3.connect("projects_tracker.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS
    user (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL,
        user_email TEXT NOT NULL,
        user_dateofbirth DATE NOT NULL,
        user_password TEXT NOT NULL
    );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS
    project (
        project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT NOT NULL,
        project_description TEXT NOT NULL,
        project_datecreation DATE NOT NULL,
        project_state BOOLEAN NOT NULL,
        user_id REFERENCES user (user_id) ON DELETE CASCADE
    );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS
    task (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        task_description TEXT NOT NULL,
        task_datecreation DATE NOT NULL,
        task_state BOOLEAN NOT NULL,
        project_id REFERENCES project (project_id) ON DELETE CASCADE
    );
""")

connection.commit()