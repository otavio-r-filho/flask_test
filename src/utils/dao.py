import os
import uuid
import pickle
import logging

def create_user_db(user_db_path):
    """
    Creates a user database, whichi is a dictionary in the format:
    user_id | files_lst

    Parameters
    ----------
    project_path : str
        Root path of the application

    Returns
    -------
    None
    """
    logging.info("Creating user database")
    # Creating parent directory
    os.makedirs(os.path.dirname(user_db_path), exist_ok=True)
    # Creating dictionary with user 0
    user_db = {"0":[]}
    # Saving user_db
    with open(user_db_path, "wb") as f:
        pickle.dump(user_db, f)
    
    return user_db

def check_user_db(project_path):
    """
    Checks if a user database exists. If not, a new one is created

    Parameters
    ----------
    project_path : str
        Root path of the application
    
    Returns
    -------
    dict
        Dictionary with the user database
    """
    logging.info("Checking user database")
    # Creating user path
    user_db_path = os.path.join(project_path, "data/auxiliary/user_db.pkl").replace("\\", "/")
    
    if os.path.exists(user_db_path):
        logging.info("User database found!")
        with open(user_db_path, "rb") as f:
            user_db = pickle.load(f)
        return user_db
    else:
        logging.warning("User database not found!")
        return create_user_db(user_db_path)

def create_new_user(user_db, max_tries=500):
    """
    Creates a new user in the database

    Parameters
    ----------
    None

    Returns
    -------
    str
        32-bit token user id
    """
    logging.info("Creating new user")
    new_user_id = uuid.uuid4().hex

    tries = 0
    while new_user_id in user_db.keys() and tries < max_tries:
        new_user_id = uuid.uuid4().hex()
        tries += 1

    if new_user_id in user_db.keys():
        logging.warning("Impossible the create a new user my lord! VALHALA IS FULL!")
        return None
    return new_user_id