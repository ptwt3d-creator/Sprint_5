from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest


def test_open_personal_account_from_main_page():
    driver = webdriver.Chrome()
    
    driver.get("https://stellarburgers.education-services.ru/")
    
    driver.find_element(By.XPATH, "//*[text() = 'Личный Кабинет']").click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Войти']")))
    
    driver.find_element(By.XPATH, "//*/label[text() = 'Email']/following-sibling::input").send_keys("AlexanderSobolev51_999@yandex.ru")
    
    driver.find_element(By.XPATH, "//*/label[text() = 'Пароль']/following-sibling::input").send_keys("42314231")
    
    driver.find_element(By.XPATH, "//*[text() = 'Войти']").click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Оформить заказ']")))
    
    driver.find_element(By.XPATH, "//*[text() = 'Личный Кабинет']").click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Выход']")))
    
    driver.quit()