from flask import session, redirect

class AuthUtils:
    @staticmethod
    def isAuthenticated():
        user_id = session.get("user_id")
        if not user_id:
            return redirect("/")
        return user_id