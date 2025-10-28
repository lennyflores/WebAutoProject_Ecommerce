from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utils.logger import get_logger
from src.pages.selenium.base_page import BasePage
from src.pages.selenium.inventory_page import InventoryPage

logger = get_logger(__name__)

class LoginPage(BasePage):

    # Login page locators   
    login_header = (By.XPATH, "//*[@id='root']/div/div[1]") 
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
 
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
        logger.info("Enter username")
        self.enter_username(username)
        logger.info("Enter password")
        self.enter_password(password)
        logger.info("Click login button")
        self.click_login_button()
        return InventoryPage(self.driver) 