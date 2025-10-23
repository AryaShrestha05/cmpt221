"""query.py: leverages SQLAlchemy to create generic queries for interacting with the postgres DB"""
from db.server import get_session

def get_all(table) -> list:
    """Select all records from a DB table using SQLAlchemy ORM.

        args: 
            table (object): db table

        returns:
            records (list[obj]): list of records from db table
    """
    session = get_session()
    try:
        # get all records in the table
        records = session.query(table).all()
        return records
    
    finally:
        session.close()

def insert(record) -> None:
    session = get_session()
    try:
        session.add(record)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error inserting record: {e}")
        raise e
    finally:
        session.close()

def get_user_by_email(table, email) -> object:
    """Find a user by email address using SQLAlchemy ORM.

        args: 
            table (object): db table
            email (str): email address to search for

        returns:
            user (object): user record from db table, or None if not found
    """
    session = get_session()
    try:
        # find user by email
        user = session.query(table).filter(table.Email == email).first()
        return user
    
    finally:
        session.close()