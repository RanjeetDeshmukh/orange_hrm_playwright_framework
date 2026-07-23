import pytest
from playwright.sync_api import Page
from orange_hrm_playwright_framework.pages.add_employee_page import AddEmployee
from orange_hrm_playwright_framework.pages.login_page import LoginPage
from orange_hrm_playwright_framework.pages.dashboard_page import DashboardPage
from orange_hrm_playwright_framework.pages.pim_page import PimPage
from orange_hrm_playwright_framework.pages.view_personal_details_page import ViewPersonalDetails
from orange_hrm_playwright_framework.pages.view_employee_list_page import ViewEmployeeList
from pathlib import Path

#creating a fixture to get the obj of LoginPage class which we will pass to test functions. By doing this we
#cont-avoided writing this step in each test case

@pytest.fixture
def login_page(page:Page):
    login_page_obj = LoginPage(page)
    return login_page_obj

@pytest.fixture
def dashboard_page(page: Page):
    dashboard_page_obj = DashboardPage(page)
    return dashboard_page_obj

#directly returned obj without creating separate variable, as eventually pim_page will catch that obj
@pytest.fixture
def pim_page(page:Page):
     return PimPage(page)

@pytest.fixture
def add_emp_page(page: Page):
    return AddEmployee(page)

@pytest.fixture
def view_personal_details_page(page:Page):
    return ViewPersonalDetails(page)

@pytest.fixture
def view_employee_list(page:Page):
    return ViewEmployeeList(page)

#Implementing screenshot taking functionality on test failure using hooks

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            #creating folder screenshot
            PROJECT_ROOT = Path(__file__).parent.parent
            SCREENSHOT_DIR = PROJECT_ROOT/"screenshots"
            SCREENSHOT_DIR.mkdir(exist_ok=True)
            page.screenshot(path=f"{SCREENSHOT_DIR}/{item.name}_failure.png",full_page=True)