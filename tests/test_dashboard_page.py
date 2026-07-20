from playwright.sync_api import Page, expect
from orange_hrm_playwright_framework.test_data import users_data
from orange_hrm_playwright_framework.pages.pim_page import PimPage
import re
#both login_page & dashboard+page fixtures are given to the test function
def test_navigate_to_PIM_success(login_page,dashboard_page):
    #we cannot directly open dashboard page, we need to open login page first
    login_page.open()
    #login with user
    login_page.login(users_data.ADMIN["username"], users_data.ADMIN["password"])
    #on the dashboard page, click on PIM link
    dashboard_page.click_pim()

    #assert we have landed on pim page by verifying the header on the page
    #to access header locator which we have stored in PimPage class.. we need to create obj of that class
    pim_page_obj = PimPage(dashboard_page.page)
    expect(pim_page_obj.header).to_contain_text("PIM")

    #assert we have landed on correct URL
    expect(dashboard_page.page).to_have_url(re.compile(r"/pim/viewEmployeeList"))