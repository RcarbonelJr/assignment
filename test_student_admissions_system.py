import unittest
from student_admissions_system import process_application

class TestStudentAdmissionSystem(unittest.TestCase):

    def test_valid_application(self):
        """
        Tests that valid input is processed successfully.
        """
        data = {"name": "Alice Johnson", "dob": "2002-09-15", "email": "alice.johnson@example.com"}
        result = process_application(data)
        self.assertEqual(result, "Application processed successfully.")

    def test_invalid_name_empty(self):
        """
        Verifies that an empty name triggers an appropriate error.
        """
        data = {"name": "", "dob": "2002-09-15", "email": "alice.johnson@example.com"}
        result = process_application(data)
        self.assertIn("Error", result)

    def test_invalid_dob_format(self):
        """
        Ensures that a wrongly formatted DOB is rejected.
        """
        data = {"name": "Alice Johnson", "dob": "15/09/2002", "email": "alice.johnson@example.com"}
        result = process_application(data)
        self.assertIn("Error", result)

    def test_invalid_email_format(self):
        """
        Ensures that an invalid email format triggers an error.
        """
        data = {"name": "Alice Johnson", "dob": "2002-09-15", "email": "alicejohnson.com"}
        result = process_application(data)
        self.assertIn("Error", result)

    def test_missing_fields(self):
        """
        Tests the system's behavior when expected fields are missing.
        """
        data = {}
        result = process_application(data)
        self.assertIn("Error", result)

if __name__ == "__main__":
    unittest.main()