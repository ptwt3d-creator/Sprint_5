from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest


def test_have_message_error_for_invalid_password(unique_email):
    driver = webdriver.Chrome()
    
    driver.get("https://stellarburgers.education-services.ru/register")
    
    driver.find_element(By.XPATH, "//*[text() = 'Личный Кабинет']").click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Зарегистрироваться']")))
    
    driver.find_element(By.XPATH, "//*[text() = 'Зарегистрироваться']").click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*/label[text() = 'Имя']/following-sibling::input")))
    
    driver.find_element(By.XPATH, "//*/label[text() = 'Имя']/following-sibling::input").send_keys("Алксндр")
    
    driver.find_element(By.XPATH, "//*/label[text() = 'Email']/following-sibling::input").send_keys(unique_email)
    
    driver.find_element(By.XPATH, "//*/label[text() = 'Пароль']/following-sibling::input").send_keys("4")
    
    driver.find_element(By.XPATH, "//*[text() = 'Зарегистрироваться']").click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Некорректный пароль']")))
    
    driver.quit()