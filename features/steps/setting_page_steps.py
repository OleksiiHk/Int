from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@then ('Click on Community option')
def click_community(context):
    context.app.setting_page.click_community()

@when ('Verify the right page opens')
def verify_community_page_is_open(context):
    context.app.setting_page.verify_community_page_is_open()
    # sleep(2)

@when ('Verify “Contact support” button is available and clickable')
def verify_contact_support_button(context):
    context.app.setting_page.verify_contact_support_button()