import pytest
from playwright.sync_api import expect
import re
from orange_hrm_playwright_framework.test_data import users_data
from orange_hrm_playwright_framework.tests.conftest import pim_page
from orange_hrm_playwright_framework.pages.view_personal_details_page import ViewPersonalDetails
from orange_hrm_playwright_framework.test_data import temp_test_data

def test_emp_id_auto_generation(login_page,dashboard_page,pim_page,add_emp_page):
    login_page.open()
    login_page.login(users_data.ADMIN["username"],users_data.ADMIN["password"])
    dashboard_page.click_pim()
    pim_page.click_add_employee_button()


    #assert the emp id input field has auto generated value
    #the value changes on each login its dynamic so we cannot assert exact value, but can assert pattern
    #cont-like there must a value of 4 digit or it must be non-empty so we have to regex validation here
    expect(add_emp_page.emp_id_txt_fld).to_have_value(re.compile(r"\d{4}"))

def test_create_new_emp_success(add_emp_page,login_page,dashboard_page,pim_page,view_personal_details_page):
    login_page.open()
    login_page.login(users_data.ADMIN["username"], users_data.ADMIN["password"])
    dashboard_page.click_pim()
    pim_page.click_add_employee_button()
    #invoking create new employee method to simply create a new employee in system
    #the firstname & lastname of user is stored in temp_test_data.py file
    add_emp_page.create_new_employee(temp_test_data.firstname,temp_test_data.lastname)

    #assert employee has been created success
    #1.assert url i.e. we have landed on view personal details page
    expect(view_personal_details_page.page).to_have_url(re.compile(r"/pim/viewPersonalDetails/"))

    #2.assert the firstname & lastname of entered user is appeared as heading
    expect(view_personal_details_page.emp_name_header).to_have_text(temp_test_data.firstname+" "+temp_test_data.lastname)

    #3. assert the firstname & lastname fields are prepopulated with exact firstname & lastname & middle name should be blank
    expect(view_personal_details_page.first_name_field).to_have_value(temp_test_data.firstname)
    expect(view_personal_details_page.last_name_field).to_have_value(temp_test_data.lastname)
    expect(view_personal_details_page.middle_name_field).to_have_value("")