from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utils.logger import get_logger
from src.pages.base_page import BasePage
#from src.pages.elements_page import ElementsPage

logger = get_logger(__name__)

class InventoryPage(BasePage):

    # inventory page locators
    inventory_title = (By.CLASS_NAME, "title")
        
    def __init__(self, driver):
        super().__init__(driver)        
       

    # inventory page actions  
    def enter_username(self, username):
        self.enter_text(self.username_input, username)

    def enter_password(self, password):
        self.enter_text(self.password_input, password)

    def get_inventory_title(self):
        return self.find_element(self.inventory_title)



    