import allure
import pytest
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from soft_assert import check, verify


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
    @pytest.mark.functional
    def test_inventory_page_title(self, login, log_test_name):
        """
        Test that Inventory page is displayed with all options
        """                        
        # `login` fixture returns InventoryPage instance
        inventory_page = login
                        
        # Get page title (method implemented in InventoryPage)
        title_text = inventory_page.get_inventory_title().text
        # Assert that check the inventory title is being displayed
        assert title_text == "Products", "Inventory title is not displayed"        
        logger.info("Page title: " + inventory_page.get_inventory_title().text)

    @pytest.mark.functional
    def test_inventory_add_all_items_to_cart(self, login, log_test_name): 
        """
        Test that all items are added to cart successfully
        """                     
        #`login` fixture returns InventoryPage instance
        inventory_page = login

        # get the inventory items added
        items_added=0
        # get the inventory item list
        inventory_items = inventory_page.get_inventory_items()


        with verify():
            # loop through the inventory items
            for item in inventory_items:
                try:                              
                    inventory_page.click_add_to_cart_button()                
                    logger.info("Clicked Add to Cart for a product.")
                    items_added+=1                

                    # check the remove to cart button is displayed
                    check(inventory_page.get_remove_to_cart_button().is_displayed(), "Remove to cart button is not displayed")

                except Exception as e:
                    logger.error(f"Failed to click Add to Cart for a product: {e}")

            # get the cart count from the badge
            cart_count = inventory_page.get_shopping_cart_badge_count()            
            # check the cart count matches the number of items added            
            check(int(cart_count) == items_added, "Cart count does not match")

    
    @pytest.mark.functional
    def test_inventory_remove_all_items_from_cart(self, login, log_test_name): 
        """
        Test that all items are removed from cart successfully
        """                     
        #`login` fixture returns InventoryPage instance
        inventory_page = login

        # get the inventory item list
        inventory_items = inventory_page.get_inventory_items()
        # Add all inventory items to the cart
        inventory_page.click_add_to_cart_for_all_inventory_items()
        # get the cart count from the badge
        items_added = int(inventory_page.get_shopping_cart_badge_count())
        logger.info("Items added to cart: " + str(items_added))
            
        with verify():
            for item in inventory_items:
                try:                              
                    inventory_page.click_remove_to_cart_button()
                    logger.info("Clicked Remove for a product.")
                    items_added-=1                    

                    # check the remove to cart button is displayed
                    check(inventory_page.get_add_to_cart_button().is_displayed(), "Add to cart button is not displayed")

                except Exception as e:
                    logger.error(f"Failed to click Remove for a product: {e}")
                    
            check(items_added == 0, "All items were not removed from the cart")

