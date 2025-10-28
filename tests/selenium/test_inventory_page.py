import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from src.pages.selenium.login_page import LoginPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestsaucedemoInventoryPage:

    @pytest.mark.functional
    @allure.title("Test Inventory Page loading")
    @allure.description("This test checks that the Inventory page is displayed with all options")
    @allure.tag("Inventory", "Smoke", "Functional")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Inventory Page")
    @allure.story("Inventory Page") 
    @allure.link("https://www.saucedemo.com/inventory.html")

    def test_inventory_page_title(self, driver, log_test_name):
        """
        Test that Inventory page is displayed with all options
        """                

        # create the page object
        login_page = LoginPage(driver)
                
        # login functionality
        logger.info("Enter the credentials and then click on login button")
        inventory_page = login_page.login("standard_user", "secret_sauce")
                        
        logger.info("Page title: " + inventory_page.get_inventory_title().text)
        
        # Assert that check the inventory title is being displayed
        assert inventory_page.get_inventory_title().text == "Products", "Inventory title is not displayed"
        

    def test_inventory_add_all_items_to_cart(self, driver, log_test_name): 
        """
        Test that all items are added to cart successfully
        """     
         # create the page object
        login_page = LoginPage(driver)
                
        # login functionality
        logger.info("Enter the credentials and then click on login button")
        inventory_page = login_page.login("standard_user", "secret_sauce")

        # add all items to cart
        items_added = inventory_page.click_add_to_cart_for_all_inventory_items()

        # Assertions
        #assert inventory_page.get_element_text() == "6", "Shopping cart badge number is incorrect"
        cart_count = inventory_page.get_shopping_cart_badge_count()
        assert int(cart_count) == items_added, f"Expected {items_added}, but cart shows {cart_count}"



        #inventory_page.remove_to_cart()                        
        
        # Assertions
        #expect(inventory_page.add_to_cart_button).to_be_visible() 