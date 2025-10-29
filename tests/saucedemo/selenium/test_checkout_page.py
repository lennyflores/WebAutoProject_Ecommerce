from tabnanny import check
import allure
import pytest
from selenium.webdriver.common.by import By
from src.pages.saucedemo.selenium.login_page import LoginPage
from utils.logger import get_logger
from soft_assert import check, verify


logger = get_logger(__name__)
class TestSaucedemoCheckoutPage:

    @pytest.mark.functional
    @allure.title("Test Checkout Page loading")  
    @allure.link("https://www.saucedemo.com/inventory.html")
    def test_cart_checkout_page_title(self, login, log_test_name):
        """
        Test that checkout page is displayed with all options
        """                
        # `login` fixture returns InventoryPage instance
        inventory_page = login

        # add all items to cart                    
        inventory_page.click_add_to_cart_for_all_inventory_items()
        # click on shopping cart badge
        cart_page = inventory_page.click_shopping_cart_badge()
        # click on checkout button
        checkout_page = cart_page.click_checkout_button()        
                                
        # Assert that check the inventory title is being displayed
        assert checkout_page.get_checkout_title().text == "Checkout: Your Information", "Checkout title is not displayed"
    
    @pytest.mark.functional
    @allure.title("Test Checkout Your Information")  
    @allure.link("https://www.saucedemo.com/inventory.html")
    def test_cart_checkout_your_information(self, login, log_test_name): 
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

        checkout_page.enter_your_information("John", "Doe", "12345")  
        checkout_page.click_continue_button() 
                                
        # Assert that check the Checkout: Overview page is displayed


    def test_cart_checkout_overview(self, login, log_test_name): 
        """
        Test that checkout overview page is displayed with all options
        """     
       # `login` fixture returns InventoryPage instance
        inventory_page = login
        # add all items to cart
        inventory_page.click_add_to_cart_for_all_inventory_items()
        # click on shopping cart badge
        cart_page = inventory_page.click_shopping_cart_badge()
        # click on checkout button
        checkout_page = cart_page.click_checkout_button()   

        checkout_page.enter_your_information("John", "Doe", "12345")  
        checkout_overview_page = checkout_page.click_continue_button()

        with verify():
            # Assert that check the checkout overview title is being displayed            
            check(checkout_overview_page.get_checkout_overview_title().text == "Checkout: Overview", "Checkout overview title is not displayed")
            checkout_complete_page = checkout_overview_page.click_finish_button()
                                
            # Assert that check the Checkout: Overview page is displayed            
            check(checkout_complete_page.get_checkout_complete_title().text == "Checkout: Complete!", "Checkout complete title is not displayed")

    def test_cart_checkout_complete(self, login, log_test_name): 
        """
        Test that checkout overview page is displayed with all options
        """     
        # `login` fixture returns InventoryPage instance
        inventory_page = login
        # add all items to cart
        inventory_page.click_add_to_cart_for_all_inventory_items()
        # click on shopping cart badge
        cart_page = inventory_page.click_shopping_cart_badge()
        # click on checkout button
        checkout_page = cart_page.click_checkout_button()   

        checkout_page.enter_your_information("John", "Doe", "12345")  
        checkout_overview_page = checkout_page.click_continue_button()

        with verify():
            # Assert that check the checkout overview title is being displayed            
            check(checkout_overview_page.get_checkout_overview_title().text == "Checkout: Overview", "Checkout overview title is not displayed")
            checkout_complete_page = checkout_overview_page.click_finish_button()                                        
            # Assert that check the Checkout: Overview page is displayed            
            check(checkout_complete_page.get_checkout_complete_title().text == "Checkout: Complete!", "Checkout complete title is not displayed")