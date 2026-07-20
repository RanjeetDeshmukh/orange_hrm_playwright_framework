from orange_hrm_playwright_framework.constants import routes
from orange_hrm_playwright_framework import config

class PimPage:
    def __init__(self,page):
        self.page = page
        self.header = page.locator(".oxd-topbar h6")
        self.add_employee_button = page.get_by_role("button",name=" Add ")

    def open(self):
        self.page.goto(config.BASE_URL + routes.PIM_ROUTE)

    def click_add_employee_button(self):
        self.add_employee_button.click()

