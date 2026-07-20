from datetime import datetime
from orange_hrm_playwright_framework.test_data import temp_test_data

current = datetime.now()
formatted_time = current.strftime("%Y%m%d_%H%M%S")
def generate_fname():
    return f"TestFname_{formatted_time}"
def generate_lname():
    return f"TestLname_{formatted_time}"


