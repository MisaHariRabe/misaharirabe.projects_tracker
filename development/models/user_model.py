from . import db
import bcrypt

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    user_dateofbirth = db.Column(db.Date, nullable=False)
    user_password = db.Column(db.LargeBinary, nullable=False)

    projects = db.relationship('Project', backref='user', lazy=True, cascade="all, delete-orphan")

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    
    def verify_password(self, password):
        if isinstance(self.user_password, bytes):
            return bcrypt.checkpw(password.encode("utf-8"), self.user_password)
        raise ValueError("Invalid hashed password format")
    
    @classmethod
    def create(cls, user_name, user_email, user_dateofbirth, user_password):
        user = cls(
            user_name=user_name,
            user_email=user_email,
            user_dateofbirth=user_dateofbirth,
            user_password=cls.hash_password(user_password)
        )
        db.session.add(user)
        db.session.commit()
        return user