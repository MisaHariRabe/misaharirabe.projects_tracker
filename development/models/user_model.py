from db import connection

class UserModel:
    @staticmethod
    def create(user_name, user_dateofbirth, user_email, user_password):
        cursor = connection.cursor()
        sql = "INSERT INTO user (user_name, user_dateofbirth, user_email, user_password) VALUES (?,?,?,?);"
        cursor.execute(sql, (user_name, user_dateofbirth, user_email, user_password))
        connection.commit()
