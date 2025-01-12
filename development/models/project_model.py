from . import db
from datetime import datetime, timezone

class Project(db.Model):
    __tablename__ = 'project'
    
    project_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(100), nullable=False)
    project_description = db.Column(db.Text, nullable=False)
    project_datecreation = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    project_state = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    
    # Relation avec Task
    tasks = db.relationship('Task', backref='project', lazy=True, cascade="all, delete-orphan")
    
    @classmethod
    def create(cls, project_name, project_description, user_id):
        project = cls(
            project_name=project_name,
            project_description=project_description,
            user_id=user_id
        )
        db.session.add(project)
        db.session.commit()
        return project
