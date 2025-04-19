import re

# ---------------------------------------------
# SECURITY: Input Validation Functions
# ---------------------------------------------

def validate_name(name):
    """
    Validates that the name is a non-empty string.
    """
    if not isinstance(name, str) or len(name.strip()) < 1:
        raise ValueError("Name must be a non-empty string.")
    return name.strip()

def validate_dob(dob):
    """
    Ensures DOB follows the correct YYYY-MM-DD format using regex.
    """
    date_pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(date_pattern, dob):
        raise ValueError("DOB must be in YYYY-MM-DD format.")
    return dob

def validate_email(email):
    """
    Ensures that the email is in a valid format (e.g., user@example.com).
    """
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_pattern, email):
        raise ValueError("Email must be in a valid format.")
    return email

def validate_application_data(data):
    """
    Aggregates multiple validation checks into one clean function.
    Any invalid input will raise a ValueError.
    """
    validate_name(data.get("name"))
    validate_dob(data.get("dob"))
    validate_email(data.get("email"))
    return True

# ---------------------------------------------
# RELIABILITY & MAINTAINABILITY: Core Logic
# ---------------------------------------------

def process_application(data):
    """
    RELIABILITY:
    Wraps the validation process in a try-except block to prevent crashes
    and ensure consistent error messaging.
    
    MAINTAINABILITY:
    Keeps business logic separate from validation and I/O for easier updates.
    """
    try:
        if validate_application_data(data):
            return "Application processed successfully."
    except ValueError as e:
        return f"Error: {e}"
