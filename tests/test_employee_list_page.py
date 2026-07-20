from orange_hrm_playwright_framework.test_data import users_data,temp_test_data
from playwright.sync_api import expect
import time
from playwright.sync_api import Page

from orange_hrm_playwright_framework.tests.conftest import view_employee_list, view_personal_details_page


def test_emp_search_by_name(login_page,dashboard_page,pim_page,add_emp_page,view_personal_details_page,view_employee_list):
    login_page.open()
    login_page.login(users_data.ADMIN["username"],users_data.ADMIN["password"])
    dashboard_page.click_pim()
    pim_page.click_add_employee_button()
    add_emp_page.create_new_employee(temp_test_data.firstname,temp_test_data.lastname)
    view_personal_details_page.emp_name_header.wait_for(state="visible")
    view_personal_details_page.click_employee_list_link()

    view_employee_list.search_by_employee_name(temp_test_data.firstname,temp_test_data.lastname)

    #assert that it is the same user that we added newly
    emp_id,first_name_cell,last_name_cell = view_employee_list.return_records_row_data()

    expect(first_name_cell).to_contain_text(temp_test_data.firstname)
    expect(last_name_cell).to_contain_text(temp_test_data.lastname)

def test_emp_search_by_id(login_page,dashboard_page,pim_page,add_emp_page,view_personal_details_page,view_employee_list,page:Page):
    login_page.open()
    login_page.login(users_data.ADMIN["username"],users_data.ADMIN["password"])
    dashboard_page.click_pim()
    pim_page.click_add_employee_button()
    add_emp_page.create_new_employee(temp_test_data.firstname, temp_test_data.lastname)
    view_personal_details_page.emp_name_header.wait_for(state="visible")

    employee_id = view_personal_details_page.get_employee_id()
    view_personal_details_page.click_employee_list_link()
    view_employee_list.search_by_employee_id(employee_id)

    #assert that the id is found & firstname lastname os correct
    emp_id, first_name_cell, last_name_cell = view_employee_list.return_records_row_data()
    expect(emp_id).to_contain_text(employee_id)
    expect(first_name_cell).to_contain_text(temp_test_data.firstname)
    expect(last_name_cell).to_contain_text(temp_test_data.lastname)

def test_employee_deletion(login_page,dashboard_page,pim_page,add_emp_page,view_personal_details_page,view_employee_list,page):
    login_page.open()
    login_page.login(users_data.ADMIN["username"],users_data.ADMIN["password"])
    dashboard_page.click_pim()
    pim_page.click_add_employee_button()
    #create a new employee
    add_emp_page.create_new_employee(temp_test_data.firstname,temp_test_data.lastname)
    view_personal_details_page.emp_name_header.wait_for(state="visible")
    #get the employee id from personal details page & store it inside employee_id variable
    employee_id = view_personal_details_page.get_employee_id()
    #click on employee list link & go to employee_list page
    view_personal_details_page.click_employee_list_link()
    #search the employee id we created
    view_employee_list.search_by_employee_id(employee_id)
    #delete the record from the table employee records
    view_employee_list.click_delete_record_button()
    #click Yes Delete on confirmation popup
    view_employee_list.confirm_delete_record_btn.click()
    #search the employee by employee id
    view_employee_list.search_by_employee_id(employee_id)

    #assert after deletion there are no records in that records table
    expect(view_employee_list.records_table_body_row).to_have_count(0)










