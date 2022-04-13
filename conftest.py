import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome("/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver

    driver.quit()
