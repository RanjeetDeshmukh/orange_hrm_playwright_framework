from playwright.sync_api import Page
from orange_hrm_playwright_framework import config
from orange_hrm_playwright_framework.constants import routes

class ViewPersonalDetails:
    def __init__(self,page:Page):
        self.page = page
        self.emp_name_header = page.locator(".orangehrm-edit-employee-name h6")
        self.first_name_field = page.get_by_placeholder("First Name")
        self.last_name_field = page.get_by_placeholder("Last Name")
        self.middle_name_field = page.get_by_placeholder("Middle Name")
        self.employee_list_link = page.get_by_role("link",name="Employee List")

    def open(self):
        self.page.goto(config.BASE_URL+routes.VIEW_PERSONAL_DETAILS_ROUTE)

    def click_employee_list_link(self):
        self.employee_list_link.click()

    def get_employee_id(self):
        # TODO: Replace nth(4) with a stable locator when available.
        self.page.wait_for_load_state("networkidle")
        employee_id = self.page.get_by_role("textbox").nth(4).input_value()
        return employee_id