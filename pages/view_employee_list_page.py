from playwright.sync_api import Page
from orange_hrm_playwright_framework import config
from orange_hrm_playwright_framework.constants import routes
class ViewEmployeeList:
    def __init__(self,page:Page):
        self.page = page
        self.enter_employee_name = page.get_by_role("textbox", name="Type for hints...").nth(0) #used codegen here.
        self.search_button = page.get_by_role("button",name=" Search ")
        self.enter_employee_id = page.locator(".oxd-input-group.oxd-input-field-bottom-space input").nth(1)
        self.confirm_delete_record_btn = page.get_by_role("button",name = " Yes, Delete ")
        self.records_table_body_row = page.locator(".oxd-table-body").get_by_role("row")

    def open(self):
        self.page.goto(config.BASE_URL+routes.VIEW_EMPLOYEE_LIST_ROUTE)

    def search_by_employee_name(self,firstname,lastname):
        self.enter_employee_name.fill(firstname+" "+lastname)
        self.search_button.click()

    def return_records_row_data(self):
        emp_id = self.records_table_body_row.get_by_role("cell").nth(1)
        records_table_firstname = self.records_table_body_row.get_by_role("cell").nth(2)
        records_table_lastname = self.records_table_body_row.get_by_role("cell").nth(3)
        return emp_id, records_table_firstname, records_table_lastname

    def click_delete_record_button(self):
        delete_icon = self.records_table_body_row.get_by_role("cell").nth(8).locator(".oxd-icon.bi-trash")
        delete_icon.click()

    def search_by_employee_id(self,employee_id):
        self.enter_employee_id.fill(employee_id)
        self.search_button.click()