from orange_hrm_playwright_framework import config
from orange_hrm_playwright_framework.constants import routes

#creating a class for my login page
class LoginPage:
    #defined a constructor to access page obj from test script & to store all locators from the page
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button",name=" Login ")
        self.forgot_pass_link = page.locator(".orangehrm-login-forgot p")
        self.invalid_login_alert = page.get_by_role("alert")

    #creating method to open the actual login webpage
    def open(self):
        self.page.goto(config.BASE_URL + routes.LOGIN_ROUTE)

    #creating a method to enter username in username field
    def enter_username(self,username):
        self.username_input.fill(username)
    #creating a method to enter password in password field
    def enter_password(self,password):
        self.password_input.fill(password)
    #creating a method to click on login button
    def click_login_btn(self):
        self.login_button.click()
    #creating a method to click on forgot password link
    def click_forgot_pass_lnk(self):
        self.forgot_pass_link.click()

    #creating a business method login combining enter_username, enter_password & clk_login_btn methods
    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()