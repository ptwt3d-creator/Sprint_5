from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Urls
import pytest


class TestLogin:
    
    def test_login_with_button_to_page_registration(self, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.REGISTER_BUTTON)))
        
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.NAME_INPUT)))
        
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_FORM_HEADER)))
        
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("AlexanderSobolev51_999@yandex.ru")
        
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("42314231")
        
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.CREATE_ORDER_BUTTON)))

    def test_login_with_personal_account_to_main_page(self, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_BUTTON)))
        
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("AlexanderSobolev51_999@yandex.ru")
        
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("42314231")
        
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.CREATE_ORDER_BUTTON)))
    
    def test_login_with_main_page_button_login(self, driver):  
        driver.get(Urls.STELLAR_BURGERS_MAIN)
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_BUTTON)))
        
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("AlexanderSobolev51_999@yandex.ru")
        
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("42314231")
        
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.CREATE_ORDER_BUTTON)))

    def test_login_with_button_to_page_password_recovery(self, driver):
        driver.get(Urls.STELLAR_BURGERS_MAIN)
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.RESTORE_PASSWORD_BUTTON)))
        
        driver.find_element(*Locators.RESTORE_PASSWORD_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_BUTTON)))
        
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_FORM_HEADER)))
        
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("AlexanderSobolev51_999@yandex.ru")
        
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("42314231")
        
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.CREATE_ORDER_BUTTON)))