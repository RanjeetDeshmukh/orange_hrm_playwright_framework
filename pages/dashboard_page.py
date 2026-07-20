#creating class for dashboard page
from orange_hrm_playwright_framework import config
from orange_hrm_playwright_framework.constants import routes

class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.dashboard_header = page.locator("#app h6")
        self.pim_link = page.locator(".oxd-main-menu-item").filter(has_text="PIM")

    def open(self):
        self.page.goto(config.BASE_URL+routes.DASHBOARD_ROUTE)

    def click_pim(self):
        self.pim_link.click()

