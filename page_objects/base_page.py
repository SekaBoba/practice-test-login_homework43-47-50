from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    #this method should not be accessible from tests only from other page objects, so we should make
    #them protected
    def _find(self, locator: tuple) -> WebElement:
        return  self._driver.find_element(*locator)

    def _type(self, locator: tuple, text:str, time: int=10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _wait_until_element_is_visible(self, locator: tuple, time: int=10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _clear(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    @property
    # current_url property should return a string (doesn't execute any steps, that why they are not methods)
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple)->bool:
        try:
            return  self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
    """def _open_url(self, url: str):
        self._driver.get(self.__url)"""

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int =10 )->bool:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))