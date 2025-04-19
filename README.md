# Student Admission System

This project implements a simple student admission system that validates user input (name, date of birth, email) and processes applications.

## Core Features:

- **Name validation**: Ensures name is a non-empty string.
- **DOB validation**: Ensures DOB follows the YYYY-MM-DD format.
- **Email validation**: Ensures email is in a valid format.
- **Application processing**: If all validations pass, the application is processed; otherwise, an error message is returned.

## Running the Tests:

To run the unit tests, ensure you have Python and the `unittest` framework installed.

1. Clone or download the repository.
2. Run the tests by executing the following command:

```bash
python -m unittest test_student_admission_system.py
```

### Test Cases:

- Valid application with correct data.
- Empty name field.
- Incorrect DOB format.
- Invalid email format.
- Missing fields.

### TDD Implementation:

The feature of email validation was implemented using Test-Driven Development (TDD). The test was written first, followed by the implementation of the feature, and refactored to ensure the test passed. Student Admission System
