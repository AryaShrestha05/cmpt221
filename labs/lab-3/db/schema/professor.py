"""professor.py: create a table named professors in the marist database"""
from db.server import db

class Professor(db.Model):
    __tablename__ = 'Professors'
    ProfessorID = db.Column(db.Integer,primary_key=True, autoincrement=True)
    P_FirstName = db.Column(db.String(100))
    P_LastName = db.Column(db.String(100))
    P_Email = db.Column(db.String(100))
    # create relationship with courses table. assoc table name = ProfessorCourse
    Courses = db.relationship('Course', secondary = 'ProfessorCourse', back_populates = 'Professors')
    def __init__(self):
        # remove pass and then initialize attributes
        self.P_FirstName = self.P_FirstName
        self.P_LastName = self.P_LastName
        self.P_Email = self.P_Email

    def __repr__(self):
        # add text to the f-string
        return f"""
            "PROFESSOR FIRST NAME: {self.P_FirstName}
             PROFESSOR LAST NAME: {self.P_LastName}
             PROFESSOR EMAIL: {self.P_Email}
        """
    
    def __repr__(self):
        return self.__repr__()