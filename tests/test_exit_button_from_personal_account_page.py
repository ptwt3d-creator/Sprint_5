from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Urls
import pytest


def test_exit_button_from_personal_account_page(driver):
    driver.get(Urls.STELLAR_BURGERS_MAIN)

    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_BUTTON)))

    driver.find_element(*Locators.EMAIL_INPUT).send_keys("AlexanderSobolev51_999@yandex.ru")

    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("42314231")

    driver.find_element(*Locators.LOGIN_BUTTON).click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.CREATE_ORDER_BUTTON)))

    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.EXIT_BUTTON)))

    driver.find_element(*Locators.EXIT_BUTTON).click()

    element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOGIN_FORM_HEADER)))

    assert element, "После клика на выхода из личного кабинета не обнаружен Заголовок формы входа."