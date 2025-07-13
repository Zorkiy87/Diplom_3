from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Кнопка входа в аккаунт
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"
    # Поле ввода email
    EMAIL_INPUT_FIELD_LOGIN = By.XPATH, "//input[@name='name']"
    # Поле ввода пароля
    PASSWORD_INPUT_FIELD_LOGIN = By.XPATH, "//input[@name='Пароль']"
    # Кнопка выхода из аккаунта
    # BUTTON_EXIT_FROM_ACCOUNT = By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']"
    # Кнопка ленты заказов
    # FEED_BUTTON = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
