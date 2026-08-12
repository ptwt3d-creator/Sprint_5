from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest


class TestLogin:
    
    def test_login_with_button_to_page_registration(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        
        driver.find_element(By.XPATH, "//*[text() = 'Личный Кабинет']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Зарегистрироваться']")))
        
        driver.find_element(By.XPATH, "//*[text() = 'Зарегистрироваться']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*/label[text() = 'Имя']/following-sibling::input")))
        
        driver.find_element(By.XPATH, "//*[text() = 'Войти']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Вход']")))
        
        driver.find_element(By.XPATH, "//*/label[text() = 'Email']/following-sibling::input").send_keys("AlexanderSobolev51_999@yandex.ru")
        
        driver.find_element(By.XPATH, "//*/label[text() = 'Пароль']/following-sibling::input").send_keys("42314231")
        
        driver.find_element(By.XPATH, "//*[text() = 'Войти']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Оформить заказ']")))

    def test_login_with_personal_account_to_main_page(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        
        driver.find_element(By.XPATH, "//*[text() = 'Личный Кабинет']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Войти']")))
        
        driver.find_element(By.XPATH, "//*/label[text() = 'Email']/following-sibling::input").send_keys("AlexanderSobolev51_999@yandex.ru")
        
        driver.find_element(By.XPATH, "//*/label[text() = 'Пароль']/following-sibling::input").send_keys("42314231")
        
        driver.find_element(By.XPATH, "//*[text() = 'Войти']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Оформить заказ']")))
    
    def test_login_with_main_page_button_login(self, driver):  
        driver.get("https://stellarburgers.education-services.ru")
        
        driver.find_element(By.XPATH, "//*[text() = 'Войти в аккаунт']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Войти']")))
        
        driver.find_element(By.XPATH, "//*/label[text() = 'Email']/following-sibling::input").send_keys("AlexanderSobolev51_999@yandex.ru")
        
        driver.find_element(By.XPATH, "//*/label[text() = 'Пароль']/following-sibling::input").send_keys("42314231")
        
        driver.find_element(By.XPATH, "//*[text() = 'Войти']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Оформить заказ']")))

    def test_login_with_button_to_page_password_recovery(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        
        driver.find_element(By.XPATH, "//*[text() = 'Личный Кабинет']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Восстановить пароль']")))
        
        driver.find_element(By.XPATH, "//*[text() = 'Восстановить пароль']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Войти']")))
        
        driver.find_element(By.XPATH, "//*[text() = 'Войти']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Вход']")))
        
        driver.find_element(By.XPATH, "//*/label[text() = 'Email']/following-sibling::input").send_keys("AlexanderSobolev51_999@yandex.ru")
        
        driver.find_element(By.XPATH, "//*/label[text() = 'Пароль']/following-sibling::input").send_keys("42314231")
        
        driver.find_element(By.XPATH, "//*[text() = 'Войти']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text() = 'Оформить заказ']")))