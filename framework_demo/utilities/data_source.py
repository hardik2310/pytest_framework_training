from framework_demo.utilities.read_utils import get_excel_as_list

test_invalid_login_data = [
    ("Admin1", "admin1", "Invalid credentials"),
    ("Admin2", "admin2", "Invalid credentials")
]

test_valid_login_data = [
    ("Admin", "admin123")
]

test_add_employee_data = [
    ("Admin", "admin123", "John", "J", "Wick", "John Wick", "John"),
    ("Admin", "admin123", "Peter", "J", "Wick", "Peter Wick", "Peter")
]

test_invalid_file_data = get_excel_as_list(io='../test_data/orange_test_data.xlsx',
                                           sheet_name='invalid_file')
