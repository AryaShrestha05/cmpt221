"""app.py: render and route to webpages"""

import os
import re
import logging
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
import bcrypt
from db.query import get_all, insert, get_user_by_email
from db.server import init_database
from db.schema import Users

# load environment variables from .env
load_dotenv()

# database connection - values set in .env
db_name = os.getenv('db_name')
db_owner = os.getenv('db_owner')
db_pass = os.getenv('db_pass')
db_url = f"postgresql://{db_owner}:{db_pass}@localhost/{db_name}"

# ===============================================================
# logging configuration
# ===============================================================
# Create logs directory if it doesn't exist
log_dir = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(log_dir, exist_ok=True)

# Configure logger
log_file = os.path.join(log_dir, 'log.txt')
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# ===============================================================
# validation functions
# ===============================================================
def validate_firstname(firstname):
    """Validate first name contains only letters"""
    if not firstname:
        return False, "First name cannot be empty"
    if not firstname.isalpha():
        return False, "First name must contain only letters"
    return True, None

def validate_lastname(lastname):
    """Validate last name contains only letters"""
    if not lastname:
        return False, "Last name cannot be empty"
    if not lastname.isalpha():
        return False, "Last name must contain only letters"
    return True, None

def validate_phone(phone):
    """Validate phone number is exactly 10 digits"""
    if not phone:
        return False, "Phone number cannot be empty"
    if not phone.isdigit():
        return False, "Phone number must contain only digits"
    if len(phone) != 10:
        return False, "Phone number must be exactly 10 digits"
    return True, None

def validate_email(email):
    """Validate email format using allowlist approach"""
    if not email:
        return False, "Email cannot be empty"
    # Basic email validation - check for @ and . with valid characters
    # Allowlist: letters, numbers, dots, underscores, hyphens, @ symbol
    # Simple email pattern check
    email_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        return False, "Email format is invalid"
    return True, None

def validate_password(password):
    """Validate password meets minimum requirements"""
    if not password:
        return False, "Password cannot be empty"
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    return True, None

# ===============================================================
# sanitization functions
# ===============================================================
def sanitize_input(input_value):
    """Remove leading and trailing whitespaces from input"""
    if input_value is None:
        return None
    return input_value.strip()

# ===============================================================
# password hashing functions
# ===============================================================
def hash_password(password):
    """Hash and salt a password using bcrypt"""
    # Generate salt and hash password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password, hashed_password):
    """Verify a password against a hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_app():
    """Create Flask application and connect to your DB"""
    # create flask app
    app = Flask(__name__, 
                template_folder=os.path.join(os.getcwd(), 'templates'), 
                static_folder=os.path.join(os.getcwd(), 'static'))
    
    
    # connect to db
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    
    # Initialize database
    with app.app_context():
        if not init_database():
            logger.error("Failed to initialize database. Exiting.")
            print("Failed to initialize database. Exiting.")
            exit(1)
        logger.info("Database initialized successfully")

    # ===============================================================
    # routes
    # ===============================================================

    # create a webpage based off of the html in templates/index.html
    @app.route('/')
    def index():
        """Home page"""
        return render_template('index.html')
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        """Sign up page: enables users to sign up"""
        if request.method == 'POST':
            try:
                # Sanitize input - remove leading/trailing whitespaces
                firstname = sanitize_input(request.form.get('firstname'))
                lastname = sanitize_input(request.form.get('lastname'))
                email = sanitize_input(request.form.get('email'))
                phone = sanitize_input(request.form.get('phone'))
                password = request.form.get('password')  # Don't strip password
                confirm_password = request.form.get('confirm_password')  # Don't strip password
                
                # Initialize validation flag - assume invalid until proven otherwise (allowlist approach)
                is_valid = False
                error_message = None
                
                # Server-side validation (using allowlist approach - assume invalid until proven valid)
                # Validate first name
                if not firstname:  # Check after sanitization
                    error_message = "First name cannot be empty"
                    logger.warning(f"Signup validation failed - First name: empty after sanitization")
                    return render_template('error.html', error_message=error_message)
                
                valid, msg = validate_firstname(firstname)
                if not valid:
                    error_message = msg
                    logger.warning(f"Signup validation failed - First name: {msg}")
                    return render_template('error.html', error_message=error_message)
                
                # Validate last name
                if not lastname:  # Check after sanitization
                    error_message = "Last name cannot be empty"
                    logger.warning(f"Signup validation failed - Last name: empty after sanitization")
                    return render_template('error.html', error_message=error_message)
                
                valid, msg = validate_lastname(lastname)
                if not valid:
                    error_message = msg
                    logger.warning(f"Signup validation failed - Last name: {msg}")
                    return render_template('error.html', error_message=error_message)
                
                # Validate phone number
                if not phone:  # Check after sanitization
                    error_message = "Phone number cannot be empty"
                    logger.warning(f"Signup validation failed - Phone: empty after sanitization")
                    return render_template('error.html', error_message=error_message)
                
                valid, msg = validate_phone(phone)
                if not valid:
                    error_message = msg
                    logger.warning(f"Signup validation failed - Phone: {msg}")
                    return render_template('error.html', error_message=error_message)
                
                # Validate email
                if not email:  # Check after sanitization
                    error_message = "Email cannot be empty"
                    logger.warning(f"Signup validation failed - Email: empty after sanitization")
                    return render_template('error.html', error_message=error_message)
                
                valid, msg = validate_email(email)
                if not valid:
                    error_message = msg
                    logger.warning(f"Signup validation failed - Email: {msg}")
                    return render_template('error.html', error_message=error_message)
                
                # Validate password strength
                valid, msg = validate_password(password)
                if not valid:
                    error_message = msg
                    logger.warning(f"Signup validation failed - Password: {msg}")
                    return render_template('error.html', error_message=error_message)
                
                # Validate password match
                if password != confirm_password:
                    error_message = "Passwords do not match"
                    logger.warning("Signup validation failed - Passwords do not match")
                    return render_template('error.html', error_message=error_message)
                
                # Check if email already exists
                existing_user = get_user_by_email(Users, email)
                if existing_user:
                    error_message = "An account with this email already exists"
                    logger.warning(f"Signup failed - Email already exists: {email}")
                    return render_template('error.html', error_message=error_message)
                
                # If all validations pass, set is_valid to True
                is_valid = True
                
                if is_valid:
                    # Hash and salt the password
                    hashed_password = hash_password(password)
                    
                    # Create user object
                    user = Users(
                        FirstName=firstname,
                        LastName=lastname,
                        Email=email,
                        Password=hashed_password,
                        PhoneNumber=phone
                    )
                    
                    # Insert user into database
                    insert(user)
                    logger.info(f"User successfully created: {email}")
                    return redirect(url_for('success'))
                    
            except Exception as e:
                # Log the error
                logger.error(f"Error during signup: {str(e)}", exc_info=True)
                error_message = "An error occurred while processing your signup. Please try again."
                return render_template('error.html', error_message=error_message)
        
        return render_template('signup.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """Log in page: enables users to log in"""
        if request.method == 'POST':
            try:
                # Sanitize input - remove leading/trailing whitespaces
                email = sanitize_input(request.form.get('email'))
                password = request.form.get('password')  # Don't strip password
                
                # Validate inputs are not empty
                if not email or not password:
                    error_message = "Email and password are required"
                    logger.warning("Login validation failed - Empty fields")
                    return render_template('error.html', error_message=error_message)
                
                # Validate email format
                valid, msg = validate_email(email)
                if not valid:
                    error_message = msg
                    logger.warning(f"Login validation failed - Email: {msg}")
                    return render_template('error.html', error_message=error_message)
                
                # Find user by email
                user = get_user_by_email(Users, email)
                
                # Check if user exists and password matches
                if user and verify_password(password, user.Password):
                    logger.info(f"User successfully logged in: {email}")
                    return redirect(url_for('success'))
                else:
                    # Log failed login attempt (but don't reveal if user exists or not)
                    logger.warning(f"Failed login attempt for email: {email}")
                    error_message = "Invalid email or password"
                    return render_template('error.html', error_message=error_message)
                    
            except Exception as e:
                # Log the error
                logger.error(f"Error during login: {str(e)}", exc_info=True)
                error_message = "An error occurred while processing your login. Please try again."
                return render_template('error.html', error_message=error_message)

        return render_template('login.html')

    @app.route('/users')
    def users():
        """Users page: displays all users in the Users table"""
        try:
            all_users = get_all(Users)
            logger.info("Users page accessed successfully")
            return render_template('users.html', users=all_users)
        except Exception as e:
            logger.error(f"Error loading users page: {str(e)}", exc_info=True)
            error_message = "An error occurred while loading users. Please try again."
            return render_template('error.html', error_message=error_message)

    @app.route('/success')
    def success():
        """Success page: displayed upon successful login"""
        return render_template('success.html')
    
    @app.route('/error')
    def error():
        """Error page: displayed when an error occurs"""
        error_message = request.args.get('error_message', 'An unknown error occurred')
        return render_template('error.html', error_message=error_message)

    return app

if __name__ == "__main__":
    app = create_app()
   
    app.run(debug=True)