import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from src.pages.selenium.login_page import LoginPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestSaucedemoLoginPage:

    @pytest.mark.functional
    def test_successfull_login(self, driver, log_test_name):
        """
        Test that the login page is displayed with all options and login functionality
        """                
        
        # create the page object
        login_page = LoginPage(driver)
        
        # verify the elements displayed
        logger.info("Verifying the elements displayed")
        logger.info("login header: " + login_page.get_login_header().text)
        assert login_page.get_login_header().text == "Swag Labs", "Login Header is not displayed"
        assert login_page.get_login_button().is_displayed()  
        assert login_page.get_login_button().is_enabled()       
        
        # login functionality
        logger.info("Enter the credentials and then click on login button")
        login_page.login("standard_user", "secret_sauce")
        
