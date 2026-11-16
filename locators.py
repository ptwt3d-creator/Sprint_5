from selenium.webdriver.common.by import By


class Locators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//*[text() = 'Личный Кабинет']") # Кнопка перехода в личный кабинет
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//*[text() = 'Войти в аккаунт']") # Копка Войти в аккаунт
    CREATE_ORDER_BUTTON = (By.XPATH, "//*[text() = 'Оформить заказ']") # Кнопка Оформить заказ
    BUNS_TAB = (By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Булки']/parent::*") # Переход Булки
    SOUS_TAB = (By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Соусы']/parent::*") # Переход Соусы
    TOPPINGS_TAB = (By.XPATH, "//*[@class = 'text text_type_main-default'][text() = 'Начинки']/parent::*") # Переход Начинки

    REGISTER_BUTTON = (By.XPATH, "//*[text() = 'Зарегистрироваться']") # Кнопка для Регистрации
    LOGIN_BUTTON = (By.XPATH, "//*[text() = 'Войти']") # Кнопка Войти
    EXIT_BUTTON = (By.XPATH, "//*[text() = 'Выход']") # Кнопка Выход

    LOGIN_FORM_HEADER = (By.XPATH, "//*[text() = 'Вход']") # Загловок Вход форма входа

    NAME_INPUT = (By.XPATH, "//*/label[text() = 'Имя']/following-sibling::input") # поле ввод Имя
    EMAIL_INPUT = (By.XPATH, "//*/label[text() = 'Email']/following-sibling::input") # поле ввод Email
    PASSWORD_INPUT = (By.XPATH, "//*/label[text() = 'Пароль']/following-sibling::input") # поле ввод Пароль

    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[text() = 'Конструктор']/parent::*") # Кнопка Конструктор
    LOGO = (By.XPATH, "//*[@class = 'AppHeader_header__logo__2D0X2']") # Кнопка-логотип Stellar Burgers

    INVALID_PASSWORD_ERROR = (By.XPATH, "//*[text() = 'Некорректный пароль']") # Регистрация - Ошибка при некорректном пароле
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//*[text() = 'Восстановить пароль']") # Кнопка Восстановить пароль




