from db import connection

cursor = connection.cursor()
class ProjectModel:
    @staticmethod
    def create(project_name, project_description, user_id):
        sql = """
            INSERT INTO project (project_name, project_description, project_datecreation, project_state, user_id)
            VALUES (?, ?, date('now'), FALSE, ?);
        """
        cursor.execute(sql, (project_name, project_description, user_id,))
        connection.commit()

    @staticmethod
    def get_by_user_id(user_id):
        sql = """
            SELECT *
            FROM project
            WHERE user_id = ?;
        """
        cursor.execute(sql, (user_id,))
        return cursor.fetchall()
    
    @staticmethod
    def get_by_project_id(project_id):
        sql = """
            SELECT *
            FROM project
            WHERE project_id = ?;
        """
        cursor.execute(sql, (project_id,))
        return cursor.fetchone()

    @staticmethod
    def get_by_project_name(project_name, user_id):
        sql = """
            SELECT *
            FROM project
            WHERE project_name LIKE "%?%"
            AND user_id = ?;
        """
        cursor.execute(sql, (project_name, user_id,))
        return cursor.fetchall()
    
    @staticmethod
    def get_by_project_date_creation(project_datecreation, user_id):
        sql = """
            SELECT *
            FROM project
            WHERE project_datecreation = ?
            AND user_id = ?;
        """
        cursor.execute(sql, (project_datecreation, user_id,))
        return cursor.fetchall()

    @staticmethod
    def get_by_project_state(project_state, user_id):
        sql = """
            SELECT *
            FROM project
            WHERE project_state = ?
            AND user_id = ?;
        """
        cursor.execute(sql, (project_state, user_id,))
        return cursor.fetchall()
    
    @staticmethod
    def update_by_project_id(project_name, project_description, project_id):
        sql = """
            UPDATE project
            SET
                project_name = ?,
                project_description = ?
            WHERE
                project_id = ?;
        """
        cursor.execute(sql, (project_name, project_description, project_id,))
        connection.commit()

    @staticmethod
    def update_state_by_project_id(project_id):
        sql = """
            UPDATE project
            SET
                project_state = TRUE
            WHERE
                project_id = ?;
        """
        cursor.execute(sql, (project_id,))
        connection.commit()

    @staticmethod
    def delete_by_project_id(project_id):
        sql = """
            DELETE FROM project
            WHERE
                project_id = ?;
        """
        cursor.execute(sql, (project_id,))
        connection.commit()