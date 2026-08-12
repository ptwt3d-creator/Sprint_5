import pytest
import datetime
from selenium import webdriver

@pytest.fixture
def unique_email():
    current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    email = f'unic_email_timestamp_{current_time}@mail.ru'
    return email

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()