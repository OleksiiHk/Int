from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page

class SettingAp(Page):
    COMMUNITY = "a.page-setting-block.w-inline-block[href='/community']"

    def click_community(self):
        self.click(self.COMMUNITY)