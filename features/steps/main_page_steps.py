from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@then ("Click on settings option")
def click_settings(context):
    context.app.main_page.click_settings()
    # sleep(2)