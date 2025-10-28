import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from src.pages.selenium.login_page import LoginPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestSaucedemoCheckoutPage:

    @pytest.mark.functional
    @allure.title("Test Inventory Page loading")
    @allure.description("This test checks that the Inventory page is displayed with all options")
    @allure.tag("Inventory", "Smoke", "Functional")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Inventory Page")
    @allure.story("Inventory Page") 
    @allure.link("https://www.saucedemo.com/inventory.html")

    def test_cart_checkout_page_title(self, driver, log_test_name):
        """
        Test that checkout page is displayed with all options
        """                

        # create the page object
        login_page = LoginPage(driver)
                
        # login functionality
        logger.info("Enter the credentials and then click on login button")
        inventory_page = login_page.login("standard_user", "secret_sauce")
        inventory_page.click_add_to_cart_for_all_inventory_items()
        cart_page = inventory_page.click_shopping_cart_badge()
        checkout_page = cart_page.click_checkout_button()        
                        
        
        # Assert that check the inventory title is being displayed
        assert checkout_page.get_checkout_title().text == "Checkout: Your Information", "Checkout title is not displayed"
    

    def test_cart_checkout_your_information(self, driver, log_test_name): 
        """
        Test that checkout functionality
        """     
        # create login page object
        login_page = LoginPage(driver)
                
        # login functionality
        logger.info("Enter the credentials and then click on login button")
        inventory_page = login_page.login("standard_user", "secret_sauce")
        inventory_page.click_add_to_cart_for_all_inventory_items()
        cart_page = inventory_page.click_shopping_cart_badge()
        checkout_page = cart_page.click_checkout_button()   

        # Assert that check the checkout title is being displayed
        assert checkout_page.get_checkout_title().text == "Checkout: Your Information", "Checkout title is not displayed"

        checkout_page.enter_your_information("John", "Doe", "12345")  
        checkout_page.click_continue_button() 
                                
        # Assert that check the Checkout: Overview page is displayed


    def test_cart_checkout_overview(self, driver, log_test_name): 
        """
        Test that checkout overview page is displayed with all options
        """     
        # create login page object
        login_page = LoginPage(driver)
                
        # login functionality
        logger.info("Enter the credentials and then click on login button")
        inventory_page = login_page.login("standard_user", "secret_sauce")
        inventory_page.click_add_to_cart_for_all_inventory_items()
        cart_page = inventory_page.click_shopping_cart_badge()
        checkout_page = cart_page.click_checkout_button()   

        checkout_page.enter_your_information("John", "Doe", "12345")  
        checkout_overview_page = checkout_page.click_continue_button()

        assert checkout_overview_page.get_checkout_overview_title().text == "Checkout: Overview", "Checkout overview title is not displayed"

        checkout_complete_page = checkout_overview_page.click_finish_button()
                                
        # Assert that check the Checkout: Overview page is displayed
        assert checkout_complete_page.get_checkout_complete_title().text == "Checkout: Complete!", "Checkout complete title is not displayed"

    def test_cart_checkout_complete(self, driver, log_test_name): 
        """
        Test that checkout overview page is displayed with all options
        """     
        # create login page object
        login_page = LoginPage(driver)
                
        # login functionality
        logger.info("Enter the credentials and then click on login button")
        inventory_page = login_page.login("standard_user", "secret_sauce")
        inventory_page.click_add_to_cart_for_all_inventory_items()
        cart_page = inventory_page.click_shopping_cart_badge()
        checkout_page = cart_page.click_checkout_button()   

        checkout_page.enter_your_information("John", "Doe", "12345")  
        checkout_overview_page = checkout_page.click_continue_button()

        assert checkout_overview_page.get_checkout_overview_title().text == "Checkout: Overview", "Checkout overview title is not displayed"

        checkout_complete_page = checkout_overview_page.click_finish_button()
                                
        # Assert that check the Checkout: Overview page is displayed
        assert checkout_complete_page.get_checkout_complete_title().text == "Checkout: Complete!", "Checkout complete title is not displayed"