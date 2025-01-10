from db import connection

cursor = connection.cursor()

class TaskModel:
    @staticmethod
    def create(task_name, task_description, project_id):
        sql = """
            INSERT INTO task (task_name, task_description, task_datecreation, task_state, project_id)
            VALUES (?, ?, date('now'), FALSE, ?);
        """
        cursor.execute(sql, (task_name, task_description, project_id,))
        connection.commit()

    @staticmethod
    def get_by_project_id(project_id):
        sql = """
            SELECT *
            FROM task
            WHERE project_id = ?;
        """
        cursor.execute(sql, (project_id,))
        return cursor.fetchall()
    
    @staticmethod
    def update_state_by_task_id(task_id):
        sql = """
            UPDATE task
            SET task_state = TRUE
            WHERE task_id = ?;
        """
        cursor.execute(sql, (task_id,))
        connection.commit()

    @staticmethod
    def delete_by_task_id(task_id):
        sql = """
            DELETE FROM task
            WHERE task_id = ?;
        """
        cursor.execute(sql, (task_id,))
        connection.commit()
