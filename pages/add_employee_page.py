from orange_hrm_playwright_framework import config
from orange_hrm_playwright_framework.constants import routes
class AddEmployee:
    def __init__(self,page):
        self.page = page
        self.header = page.locator(".orangehrm-card-container h6")
        self.emp_id_txt_fld = page.get_by_role("textbox").nth(4)
        self.first_name_field = page.get_by_placeholder("First Name")
        self.last_name_field = page.get_by_placeholder("Last Name")
        self.save_button = page.get_by_role("button",name=" Save ")

    def open(self):
        self.page.goto(config.BASE_URL+routes.ADD_EMPLOYEE_ROUTE)

    def enter_first_name(self,firstname):
        self.first_name_field.fill(firstname)

    def enter_last_name(self,lastname):
        self.last_name_field.fill(lastname)

    def create_new_employee(self,firstname,lastname):
        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.save_button.click()
