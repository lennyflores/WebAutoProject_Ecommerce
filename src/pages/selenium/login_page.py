from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utils.logger import get_logger
from src.pages.selenium.base_page import BasePage

logger = get_logger(__name__)

class LoginPage(BasePage):

    # Login page locators   
    """self.username_input = page.get_by_role("textbox", name="Username")
    self.password_input = page.get_by_role("textbox", name="Password")
    self.login_button = page.get_by_role("button", name="Login")"""

    self.username_input : Locator = page.locator("[data-test=\"username\"]")
    self.password_input : Locator = page.locator("[data-test=\"password\"]")
    self.login_button : Locator = page.locator("[data-test=\"login-button\"]")

    """page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()"""
 
    # Login page constructor
    def __init__(self, driver):
        super().__init__(driver)        
        self.url = "https://www.saucedemo.com/"
        self.driver.get(self.url)
        logger.info("Navigating to the login page: " + self.url)

    # Login page actions   
    def enter_username(self, username):
        self.enter_text(self.username_input, username)

    def enter_password(self, password):
        self.enter_text(self.password_input, password)
        
    def get_login_header(self):
        return self.find_element(self.login_header)

    def click_login_button(self):
        self.click_element(self.login_button)       

    def get_login_button(self):
        return self.find_element(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()