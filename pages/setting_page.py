from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page

class SettingPage(Page):
    COMMUNITY_BTN = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Community']")
    CONTACT_SUPPORT_BTN = (By.CSS_SELECTOR, "a#w-node-f7ead340-ee2a-2b84-cdd5-5a35322aacbf-7f66deba.chat-button.w-button[href='https://t.me/reelly_dubai_bot?start=w18415667']")

    def click_community(self):
        self.click(*self.COMMUNITY_BTN)

    def verify_community_page_is_open(self):
        self.verify_partial_url('community')

    def verify_contact_support_button(self):
        self.wait_to_be_clickable_click(*self.CONTACT_SUPPORT_BTN)