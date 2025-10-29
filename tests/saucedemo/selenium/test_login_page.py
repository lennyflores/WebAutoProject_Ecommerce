import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from src.pages.saucedemo.selenium.login_page import LoginPage
from utils.logger import get_logger
from config.config import Config
from soft_assert import check, verify



logger = get_logger(__name__)
class TestSaucedemoLoginPage:

    @pytest.mark.functional
    @pytest.mark.priority("high")
    def test_successfull_login(self, driver, env, log_test_name):
        """
        Verify user can log in successfully with valid credentials.
        """
          
        logger.info("Enter the credentials and then click on login button")
        # create the Login page object
        login_page = LoginPage(driver, env["env"])

        # verify the elements displayed
        logger.info("Verifying the elements displayed")
        logger.info("login header: " + login_page.get_login_header().text)
        assert login_page.get_login_header().text == "Swag Labs", "Login Header is not displayed"
        assert login_page.get_login_button().is_displayed()  
        assert login_page.get_login_button().is_enabled()   

        # login with valid credentials
        inventory_page = login_page.login(env["user"], env["pass"])       

        # verify the inventory page is loaded
        assert inventory_page.is_page_loaded(), "Inventory page did not load after login"
        logger.info(f"Login successful for user: {Config.USER}")
        
    @pytest.mark.functional
    @pytest.mark.priority("high")
    @pytest.mark.parametrize("read_data", ["credentials_errors"], indirect=True)
    def test_login_invalid(self, driver, env, read_data, log_test_name):
        """
        Verify error message appears when login fails with invalid credentials.
        """
        # create the Login page object
        login_page = LoginPage(driver, env["env"])
        
        with verify():
            # loop through the data
            for data in read_data:
                # clear the username and password fields
                login_page.clear_username()
                login_page.clear_password()   
                
                # login with invalid credentials
                login_page.login(data["username"], data["password"])
                
                # get the error message from the json file
                expected_message = (data['error_message'])
                logger.info(f"Expected message: {expected_message}")

                # get the error message from the login page
                error_message = login_page.get_error_message().text
                logger.info("Current Error message: " + error_message)
                      
                # verify the error message matches the expected message  
                check(error_message is not None)
                check(expected_message == error_message, "Error message does not match")                
        

                