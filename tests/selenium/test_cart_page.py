import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from src.pages.selenium import cart_page
from src.pages.selenium.login_page import LoginPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestsaucedemoCartPage:

    @pytest.mark.functional
    @allure.title("Test Inventory Page loading")
    @allure.description("This test checks that the Inventory page is displayed with all options")
    @allure.tag("Inventory", "Smoke", "Functional")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Inventory Page")
    @allure.story("Inventory Page") 
    @allure.link("https://www.saucedemo.com/inventory.html")

    def test_cart_page_title(self, driver, log_test_name):
        """
        Test that cart page is displayed with all options
        """                

        # create the page object
        login_page = LoginPage(driver)
                
        # login functionality
        logger.info("Enter the credentials and then click on login button")
        inventory_page = login_page.login("standard_user", "secret_sauce")
        inventory_page.click_add_to_cart_for_all_inventory_items()
        cart_page = inventory_page.click_shopping_cart_badge()

                        
        logger.info("Page title: " + cart_page.get_cart_title().text)
        
        # Assert that check the inventory title is being displayed
        assert cart_page.get_cart_title().text == "Your Cart", "Cart title is not displayed"
        

    def test_cart_checkout(self, driver, log_test_name): 
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
                                
        
        # Assert that check the inventory title is being displayed
        assert cart_page.get_cart_title().text == "Checkout: Your Information", "Checkout title is not displayed"
        