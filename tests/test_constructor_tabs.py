from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls
import pytest


class TestConstructorTabs:
   
    def test_open_buns_section_in_constructor(self, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)

        driver.find_element(By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Соусы']/parent::*").click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Соусы']/parent::*"), "class", "tab_type_current"))

        driver.find_element(By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Булки']/parent::*").click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Булки']/parent::*"), "class", "tab_type_current"))
    
    def test_open_sous_section_in_constructor(self, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)

        driver.find_element(By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Соусы']/parent::*").click()

        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Соусы']/parent::*"), "class", "tab_type_current"))
    
    def test_open_toppings_section_in_constructor(self, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)
        
        driver.find_element(By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Начинки']/parent::*").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Начинки']/parent::*"), "class", "tab_type_current"))
        