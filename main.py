# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from selenium.webdriver.common.by import By
import time

class NoSuchElementException:
    def test_positive_homework(self, driver):
        # Open page https://practicetestautomation.com/practice-test-exceptions/
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        time.sleep(15)

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        time.sleep(15)
        # Verify Row 2 input field is displayed
        row2=driver.find_element(By.ID,"row2")
        assert row2.is_displayed(), 'Row 2 is not displayed, but it should be'