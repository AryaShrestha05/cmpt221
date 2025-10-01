"""orm.py: sqlalchemy orm used to manage the Professors table"""
from db.server import get_session
from db.schema import Professor

"""Lab 4 - Part 2:
- Insert 3 records into the Professors table
- Update 1 record in the Professors table
- Delete 1 record in the Professors table
"""

def get_all_professors():
    """Select all records from the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # get all entries in the Professors table
        professors = session.query(Professor).all()
        return professors
    
    finally:
        session.close()

def insert_professors():
    """Insert 3 records into the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        prof1 = Professor(P_FirstName="Alice", P_LastName="Johnson", P_Email="alice.johnson@university.edu")
        prof2 = Professor(P_FirstName="Bob", P_LastName="Smith", P_Email="bob.smith@university.edu")
        prof3 = Professor(P_FirstName="Carol", P_LastName="Lee", P_Email="carol.lee@university.edu")
        session.add_all([prof1,prof2,prof3])
        session.commit()

    except Exception as e:
        session.rollback()
        print("Error inserting professors:", e)

    finally:
        session.close()

def update_professor():
    """Update one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        professor = session.query(Professor).filter_by(ProfessorID=2).first()
        if professor:
            professor.P_Email = "bob.smith.statistics@university.edu"  # update field
        session.commit()
    
    except Exception as e:
        session.rollback()
        print("Error updating professor:", e)
        
    finally:
        session.close()

def delete_professor():
    """Delete one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        professor = session.query(Professor).filter_by(ProfessorID=3).first()
        if professor:
            session.delete(professor)
        session.commit()

    except Exception as e:
        session.rollback()
        print("Error updating professor:", e)

    finally:
        session.close()

