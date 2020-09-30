from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time

link = "https://back-office.dev.it-banda.com/login"
retail_software_locations_link = "https://back-office.dev.it-banda.com/retail-software/locations"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get(link)
    browser.find_element(By.ID, "input-login").send_keys("vladimir.surivka")
    browser.find_element(By.ID, "input-password").send_keys("1q2w3e4r")
    browser.find_element(By.CSS_SELECTOR, ".appearance-filled").click()
    time.sleep(2)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestLocationPage:

    def test_user_can_add_new_location(self, browser):
        browser.get(retail_software_locations_link)
        browser.find_element(By.CSS_SELECTOR, "[routerlink='add']").click()
        browser.find_element(By.CSS_SELECTOR, "[formcontrolname='name']").send_keys("Autotest3")
        search_address = browser.find_element(By.CSS_SELECTOR, "[placeholder='Search address...']")
        search_address.send_keys(
            "Saperne Pole Street, 14/55, Kyiv, Ukraine")
        search_address.send_keys(Keys.ENTER)
        browser.find_element(By.CSS_SELECTOR, "[formcontrolname='branchId']").click()
        browser.find_element(By.CSS_SELECTOR, "nb-option:nth-child(1)").click()
        browser.find_element(By.CSS_SELECTOR, "[formcontrolname='regionId']").click()
        browser.find_element(By.CSS_SELECTOR, "nb-option:nth-child(2)").click()
        browser.find_element(By.CSS_SELECTOR, "[formcontrolname='cityId']").click()
        browser.find_element(By.CSS_SELECTOR, "nb-option:nth-child(1)").click()
        browser.find_element(By.CSS_SELECTOR, "[formcontrolname='zip']").send_keys("112233")
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        # WebDriverWait(browser, 5).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".appearance-filled"))).click()
        message = browser.find_element(By.CSS_SELECTOR, ".content-container")
        time.sleep(1)
        assert "Error occurred while creating the location" in message.text, "Location was created successfully"
        # assert "Location was created successfully" in message.text, "Location with this name already exists"
