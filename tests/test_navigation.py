from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Urls
import pytest

class TestNavigation:

    def test_open_constructor_from_personal_account_page(self, driver):    
        driver.get(Urls.STELLAR_BURGERS_MAIN)
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_FORM_HEADER)))
        
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("AlexanderSobolev51_999@yandex.ru")
        
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("42314231")
        
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.CREATE_ORDER_BUTTON)))
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.EXIT_BUTTON)))
        
        driver.find_element(*Locators.LOGO).click()
        
        element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.SOUS_TAB)))

        assert element, "После клика на Конструктор с Личного кабинета не найден раздел Соусы."

    def test_open_personal_account_from_main_page(self, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_FORM_HEADER)))
        
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("AlexanderSobolev51_999@yandex.ru")
        
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("42314231")
        
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.CREATE_ORDER_BUTTON)))
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.EXIT_BUTTON)))

        assert element, "Не найдена кнопка Выход после клика на переход в Личный кабинет." 