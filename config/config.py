import os

from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv("standard_user")
password = os.getenv("secret_sauce")


BASE_URL = {
    "development": "https://www.saucedemo.com/",
    "staging": "http://staging.demoqa.com",
    "production": "https://www.saucedemo.com/"
}