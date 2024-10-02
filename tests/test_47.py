# Open browser
# selenium 4
import time

import pytest
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
        #Type text into the second input field
        rox_2_input_element.send_keys("Stole")
        #Push Save button using locator By.name(“Save”)
        driver.find_element(By.ID,"save_btn").click()
        #driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()
        #Verify text saved
        confrimation_div=driver.find_element(By.XPATH,"//div[@id='confirmation']")
        assert confrimation_div.is_displayed()
        #  confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        # confirmation_message = confirmation_element.text
        # assert confirmation_message == "Row 2 was saved", "Confirmation message is not expected"
    @pytest.mark.debug
    def test_clear_input_feald(self):
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            time.sleep(3)
            driver.get("https://practicetestautomation.com/practice-test-exceptions/")
            time.sleep(5)

            edit_button=driver.find_element(By.XPATH,"/html//button[@id='edit_btn']")
            edit_button.click()


            row_1_input_feald=driver.find_element(By.XPATH, "// div[ @ id = 'row1'] / input[ @ value = 'Pizza']")
            wait = WebDriverWait(driver, 10)
            wait.until(ec.element_to_be_clickable(row_1_input_feald))
            row_1_input_feald.clear()

            row_1_input_feald.send_keys("Sima")


            save_button=driver.find_element(By.XPATH,"/html//button[@id='save_btn']")
            save_button.click()

            confrimation_div = driver.find_element(By.XPATH, "//div[@id='confirmation']")
            assert confrimation_div.is_displayed(), "Row 1 was saved"
            assert confrimation_div.text == "Row 1 was saved"

    @pytest.mark.debug
    def test_push_add_button(self):
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            time.sleep(3)
            driver.get("https://practicetestautomation.com/practice-test-exceptions/")
            time.sleep(5)

            instructions_text=driver.find_element(By.XPATH, "/html//p[@id='instructions']")
            assert instructions_text.is_displayed()

            edit_button=driver.find_element(By.XPATH,"/html//button[@id='add_btn']")
            edit_button.click()

            wait = WebDriverWait(driver, 10)
            assert wait.until(ec.invisibility_of_element((By.XPATH, "/html//p[@id='instructions']")))


