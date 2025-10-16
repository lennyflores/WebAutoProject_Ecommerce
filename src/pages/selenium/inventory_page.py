from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utils.logger import get_logger
from src.pages.selenium.base_page import BasePage


logger = get_logger(__name__)

class InventoryPage(BasePage):

    # inventory page locators
    inventory_title = (By.CLASS_NAME, "title")
        
    def __init__(self, driver):
        super().__init__(driver)        
       

    # inventory page actions  
    def get_inventory_title(self):
        return self.find_element(self.inventory_title)



    