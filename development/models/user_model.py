from db import connection

class UserModel:
    @staticmethod
    def create(user_name, user_dateofbirth, user_email, user_password):
        with connection.cursor() as cursor:
            sql = "INSERT INTO user (user_name, user_dateofbirth, user_email, user_password) VALUES (?,?,?,?);"
            cursor.execute(sql, (user_name, user_dateofbirth, user_email, user_password))
            connection.commit()

    @staticmethod
    def get_by_id(user_id):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user WHERE user_id = ?;"
            cursor.execute(sql, (user_id,))
            user = cursor.fetchone()
            return user