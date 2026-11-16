from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Urls
import pytest


class TestConstructorTabs:
   
    def test_open_buns_section_in_constructor(self, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)

        driver.find_element(*Locators.SOUS_TAB).click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((Locators.SOUS_TAB), "class", "tab_type_current"))

        driver.find_element(*Locators.BUNS_TAB).click()

        element = WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((Locators.BUNS_TAB), "class", "tab_type_current"))

        assert element, "После клика на раздел Булки он не активен."
        
    def test_open_sous_section_in_constructor(self, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)

        driver.find_element(*Locators.SOUS_TAB).click()

        element = WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((Locators.SOUS_TAB), "class", "tab_type_current"))
    
        assert element, "После клика на раздел Соусы он не активен."

    def test_open_toppings_section_in_constructor(self, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)
        
        driver.find_element(*Locators.TOPPINGS_TAB).click()
        
        element = WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((Locators.TOPPINGS_TAB), "class", "tab_type_current"))
        
        assert element, "После клика на раздел Начинки он не активен."