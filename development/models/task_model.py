from . import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = 'task'
    
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(100), nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    task_datecreation = db.Column(db.DateTime, default=datetime.utcnow)
    task_state = db.Column(db.Boolean, default=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id', ondelete='CASCADE'), nullable=False)
    
    @classmethod
    def create(cls, task_name, task_description, project_id):
        task = cls(
            task_name=task_name,
            task_description=task_description,
            project_id=project_id
        )
        db.session.add(task)
        db.session.commit()
        return task
