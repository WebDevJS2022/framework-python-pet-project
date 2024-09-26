from pages.base_page import BasePage
from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test(driver):
    page = BasePage(driver, 'https://the-internet.herokuapp.com/')
    page.open()
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h1')
        ))
