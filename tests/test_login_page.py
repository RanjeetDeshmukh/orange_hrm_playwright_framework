import re
from math import lgamma

from orange_hrm_playwright_framework.pages.dashboard_page import DashboardPage
from orange_hrm_playwright_framework.test_data import users_data
from playwright.sync_api import expect

#To create the obj of LoginPage class we created a fixture in conftest & that fixture we are using here
def test_valid_login(login_page):
    #using the LoginPage obj accessing methods of class LoginPage
    #opening the URL
    login_page.open()

    #invoking login function by passing username & password stored inside the users_data file
    login_page.login(users_data.ADMIN["username"], users_data.ADMIN["password"])

    #asserting login was success & we are landing on Dashboard page by checking url
    expect(login_page.page).to_have_url(re.compile(r"/dashboard/index"))

    #asserting login was success & we are landing on Dashboard page by checking the heading
    #invoking dashboard pages obj to access the locator of header element
    dashboard_page_obj = DashboardPage(login_page.page)
    expect(dashboard_page_obj.dashboard_header).to_contain_text("Dashboard")

def test_invalid_password_login(login_page):
    #opening the login_page
    login_page.open()

    #invoking login method
    login_page.login(users_data.ADMIN["username"], users_data.INVALID_CREDS["password"])

    #asserting if the error message is displayed on login page when passed invalid credetials
    expect(login_page.invalid_login_alert).to_contain_text("Invalid credentials")

def test_invalid_user_pass_login(login_page):
    login_page.open()

    #invoking login method
    login_page.login(users_data.INVALID_CREDS["username"], users_data.INVALID_CREDS["password"])

    #asserting if the error message is displayed on login page when passed invalid credetials
    expect(login_page.invalid_login_alert).to_contain_text("Invalid credentials")

