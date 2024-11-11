from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page

class SignInPage(Page):
    EMAIL_FIELD_TEXT = (By.ID, "email-2")
    PASSWORD_FIELD_TEXT = (By.ID, "field")
    LOGIN_BTN = (By.CSS_SELECTOR, '.login-button')

    def open_sign_in_page(self):
        self.open('https://soft.reelly.io/sign-in')


    def input_email_and_password(self, email, password):
        self.input_text(email, *self.EMAIL_FIELD_TEXT)
        sleep(2)
        self.input_text(password, *self.PASSWORD_FIELD_TEXT)
        sleep(2)

    def click_sign_in(self):
        self.click(*self.LOGIN_BTN)
