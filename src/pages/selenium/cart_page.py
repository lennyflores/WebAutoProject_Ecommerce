from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utils.logger import get_logger
from src.pages.selenium.base_page import BasePage
from src.pages.selenium.checkout_page import CheckoutPage


logger = get_logger(__name__)

class CartPage(BasePage):

    # inventory page locators
    cart_title = (By.CLASS_NAME, "title")
    checkout_button = (By.ID, "checkout")
    
    inventory_list = (By.XPATH, "//*[@id='inventory_container']/div/div[@class='inventory_item']")
    add_to_cart_button = (By.XPATH, "//*[@id='inventory_container']/div/div[@class='inventory_item']/div[@class='inventory_item_description']/div[@class='pricebar']/button[text()='Add to cart']")    
    shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")


    def __init__(self, driver):
        super().__init__(driver)        
       

    # inventory page actions  
    def get_cart_title(self):
        return self.find_element(self.cart_title)

    def get_cart_items(self):
        """Return a list of WebElements representing inventory items."""
        return self.driver.find_elements(*self.inventory_list)

    """
    def click_add_to_cart_for_all_inventory_items(self):
        cart_count=0
        inventory_items = self.get_inventory_items()
        for item in inventory_items:
            try:
                add_button = item.find_element(*self.add_to_cart_button)
                add_button.click()                
                sleep(2)
                print("Clicked Add to Cart for one product.")
                cart_count+=1
            except Exception as e:
                print(f"Failed to click Add to Cart for a product: {e}")
        return cart_count
    """        
    def click_checkout_button(self):
        checkout_button = self.find_element(self.checkout_button)
        checkout_button.click()
        return CheckoutPage(self.driver)

        
    


    