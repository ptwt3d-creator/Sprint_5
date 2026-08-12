from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls
import pytest


def test_open_constructor_from_personal_account_page(driver):    
    driver.get(Urls.STELLAR_BURGERS_MAIN)
    
    driver.find_element(By.XPATH, "//*[text() = 'Личный Кабинет']").click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Войти']")))
    
    driver.find_element(By.XPATH, "//*/label[text() = 'Email']/following-sibling::input").send_keys("AlexanderSobolev51_999@yandex.ru")
    
    driver.find_element(By.XPATH, "//*/label[text() = 'Пароль']/following-sibling::input").send_keys("42314231")
    
    driver.find_element(By.XPATH, "//*[text() = 'Войти']").click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Оформить заказ']")))
    
    driver.find_element(By.XPATH, "//*[text() = 'Личный Кабинет']").click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Выход']")))
    
    driver.find_element(By.XPATH, "//*[@class = 'AppHeader_header__logo__2D0X2']").click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Соусы']")))
