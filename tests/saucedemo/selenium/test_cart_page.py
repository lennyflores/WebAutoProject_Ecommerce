import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from src.pages.saucedemo.selenium.login_page import LoginPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestsaucedemoCartPage:

    @pytest.mark.functional
    @allure.title("Test Cart Page loading")
    @allure.description("This test checks that the Cart page is displayed with all options")
    @allure.tag("Cart", "Smoke", "Functional")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Cart Page")
    @allure.story("Cart Page") 
    @allure.link("https://www.saucedemo.com/cart.html")
    def test_cart_page_title(self, login, log_test_name):
        """
        Test that cart page is displayed with all options
        """                
        # `login` fixture returns InventoryPage instance
        inventory_page = login
        # add all items to cart
        inventory_page.click_add_to_cart_for_all_inventory_items()
        # click on shopping cart badge
        cart_page = inventory_page.click_shopping_cart_badge()                        
        logger.info("Page title: " + cart_page.get_cart_title().text)
        
        # Assert that check the inventory title is being displayed
        assert cart_page.get_cart_title().text == "Your Cart", "Cart title is not displayed"
        

    def test_cart_checkout(self, login, log_test_name): 
        """
        Test that checkout functionality
        """     
        # `login` fixture returns InventoryPage instance
        inventory_page = login
        # add all items to cart
        inventory_page.click_add_to_cart_for_all_inventory_items()
        # click on shopping cart badge
        cart_page = inventory_page.click_shopping_cart_badge()
        # click on checkout button
        checkout_page = cart_page.click_checkout_button()                                        
        
        # Assert that check the checkout title is being displayed
        assert checkout_page.get_checkout_title().text == "Checkout: Your Information", "Checkout title is not displayed"
        