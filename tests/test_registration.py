from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Urls
import pytest

class TestRegistration:

    def test_registration(self, unique_email, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)
    
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.REGISTER_BUTTON)))
        
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.NAME_INPUT)))
        
        driver.find_element(*Locators.NAME_INPUT).send_keys("Алксндр")
        
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(unique_email)
        
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("42314231")
        
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_FORM_HEADER)))

        assert element, "После клика на регистрацию на странице заголовок 'Вход' не найден."

    def test_have_message_error_for_invalid_password(self, unique_email, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.REGISTER_BUTTON)))
        
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.NAME_INPUT)))
        
        driver.find_element(*Locators.NAME_INPUT).send_keys("Алксндр")
        
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(unique_email)
        
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("4")
        
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.INVALID_PASSWORD_ERROR)))

        assert element, "При вводе не корректного пароля в регистрации, не обнаружено сообщение об ошибке."    