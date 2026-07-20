import re
from playwright.sync_api import expect
from orange_hrm_playwright_framework.pages import add_employee_page
from orange_hrm_playwright_framework.pages.add_employee_page import AddEmployee
from orange_hrm_playwright_framework.test_data import users_data

def test_navigation_to_addEmployee_page(login_page,dashboard_page,pim_page):
    login_page.open()
    login_page.login(users_data.ADMIN["username"],users_data.ADMIN["password"])
    dashboard_page.click_pim()
    pim_page.click_add_employee_button()

    #creating object of AddEmployee class.
    add_employee_page = AddEmployee(pim_page.page)
    #notice we are using add_employee_page.page not pim_page.page here becoz url of the page, locator,action should belong to that page only
    #assert we have arrived at add employee pages
    expect(add_employee_page.page).to_have_url(re.compile(r"/addEmployee"))

    #assert the heading is Add Employee
    expect(add_employee_page.header).to_contain_text("Add Employee")