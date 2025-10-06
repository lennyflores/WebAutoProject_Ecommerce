from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from src.pages.login_page import LoginPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestsaucedemoLoginPage:
    
    @classmethod
    def setup_class(self):
        # start the session
        self.driver = webdriver.Chrome()
        logger.info("Starting the session")
        self.driver.implicitly_wait(10)
    
    def test_saucedemo_login_page(self):
        """
        Test that the login page is displayed with all options and login functionality
        """                
        
        # create the page object
        login_page = LoginPage(self.driver)
        
        # verify the elements displayed
        logger.info("Verifying the elements displayed")
        logger.info("login header: " + login_page.get_login_header().text)
        assert login_page.get_login_header().text == "Swag Labs", "Login Header is not displayed"
        assert login_page.get_login_button().is_displayed()  
        assert login_page.get_login_button().is_enabled()       
        
        # login functionality
        logger.info("Enter username")
        login_page.enter_username("standard_user")
        logger.info("Enter password")
        login_page.enter_password("secret_sauce")
        logger.info("Click login button")
        login_page.click_login_button()
        
                
    
    @classmethod
    def teardown_class(self):
        # Close the browser
        logger.info("Closing the browser")
        self.driver.quit()