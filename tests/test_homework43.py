# Open browser
# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class TestPositiveScenarios:
    def test_no_such_element_exception(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        time.sleep(3)
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        time.sleep(5)

        """options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")"""

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()


        wait=WebDriverWait(driver, 10)
        rox_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed

        assert rox_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"
