# config.py
import os
import pytest
from dotenv import load_dotenv

# loads variables from .env file
load_dotenv() 


class Config:
    """Centralized access to environment settings.
    Central configuration for all environment variables.
    - CI/CD: uses system environment variables (USER, PASS)
    - Local: falls back to .env values (SWAGLABS_USERNAME, SWAGLABS_PASSWORD")
    """

    USER = os.getenv("USER")
    PASS = os.getenv("PASS")
    BASE_URL = {
    "development": "https://www.saucedemo.com/",
    "staging": "http://staging.demoqa.com",
    "production": "https://www.saucedemo.com/"
}
    

    if not USER:
        USER = os.getenv("SWAGLABS_USERNAME")
    if not PASS:
        PASS = os.getenv("SWAGLABS_PASSWORD")

    @staticmethod
    def validate():
        """Ensure required variables exist."""
        missing = [key for key in ["USER", "PASS"] if not getattr(Config, key)]
        if missing:
            raise EnvironmentError(
                f"Missing environment variables: {', '.join(missing)}. "
                f"Define them in system env (for CI) or .env (for local)."
            )
    

