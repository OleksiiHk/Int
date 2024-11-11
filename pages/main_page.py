from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page

class MainPage(Page):
    SETTINGS_BTN = (By.CSS_SELECTOR, "a.menu-button-block.w-inline-block[href='/settings']")

    def click_settings(self):
        self.click(*self.SETTINGS_BTN)