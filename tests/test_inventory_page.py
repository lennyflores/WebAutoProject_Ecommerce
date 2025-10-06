from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestsaucedemoLoginPage:
    
    @classmethod
    def setup_class(self):
        # start the session
        self.driver = webdriver.Chrome()
        logger.info("Starting the session")
        self.driver.implicitly_wait(10)
    
    def test_saucedemo_inventory_page(self):
        """
        Test that Inventory page is displayed with all options
        """                

        # create the page object
        login_page = LoginPage(self.driver)
        
        
        # login functionality
        logger.info("Enter username")
        login_page.enter_username("standard_user")
        logger.info("Enter password")
        login_page.enter_password("secret_sauce")
        logger.info("Click login button")     
        login_page.click_login_button()
        
        # create the inventory page
        inventory_page = InventoryPage(self.driver)

        # verify the inventory title
        logger.info("Page title: " + inventory_page.get_inventory_title().text)
        assert inventory_page.get_inventory_title().text == "Products", "Inventory title is not displayed"
        

    @classmethod
    def teardown_class(self):
        # Close the browser
        logger.info("Closing the browser")
        self.driver.quit()