from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utils.logger import get_logger
from src.pages.saucedemo.selenium.base_page import BasePage


logger = get_logger(__name__)

class CheckoutPage(BasePage):

    # checkout page locators
    checkout_title = (By.CLASS_NAME, "title")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    zip_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")


    def __init__(self, driver):
        super().__init__(driver)        
       

    # inventory page actions  
    def get_checkout_title(self):
        return self.find_element(self.checkout_title)

    def enter_first_name(self, first_name):
        self.enter_text(self.first_name, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.last_name, last_name)

    def enter_zip_code(self, zip_code):
        self.enter_text(self.zip_code, zip_code)
        
    def click_continue_button(self):
        self.click_element(self.continue_button)
        return CheckoutOverviewPage(self.driver)

    def get_checkout_title(self):
        return self.find_element(self.checkout_title)

    def enter_your_information(self, first_name, last_name, zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)

#page fragment
class CheckoutOverviewPage(BasePage):

    # checkout page locators
    checkout_overview_title = (By.CLASS_NAME, "title")
    summary_subtotal_label = (By.CSS_SELECTOR, "subtotal-label")
    summary_tax_label = (By.CSS_SELECTOR, "tax-label")
    summary_total_label = (By.CSS_SELECTOR, "total-label")
    finish_button = (By.ID, "finish")
    

    def __init__(self, driver):
        super().__init__(driver)        
       

    # inventory page actions  
    def get_checkout_overview_title(self):
        return self.find_element(self.checkout_overview_title)
    
    def get_summary_subtotal_label(self):
        return self.find_element(self.summary_subtotal_label)

    def get_summary_tax_label(self):
        return self.find_element(self.summary_tax_label)

    def get_summary_total_label(self):
        return self.find_element(self.summary_total_label)

    def get_checkout_title(self):
        return self.find_element(self.checkout_title)

    def click_finish_button(self):
        self.click_element(self.finish_button)
        return CheckoutCompletePage(self.driver)


#page fragment
class CheckoutCompletePage(BasePage):

    # checkout page locators
    checkout_complete_title = (By.CLASS_NAME, "title")
    checkout_complete_header = (By.CLASS_NAME, "complete-header")
    back_home_button = (By.ID, "back-to-products")
    

    def __init__(self, driver):
        super().__init__(driver)        
       

    # inventory page actions  
    def get_checkout_complete_title(self):
        return self.find_element(self.checkout_complete_title)
    
    def get_checkout_complete_header(self):
        return self.find_element(self.checkout_complete_header)

    def click_back_home_button(self):
        self.click_element(self.back_home_button)
        #return InventoryPage(self.driver)



    


    