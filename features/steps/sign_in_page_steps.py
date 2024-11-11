from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open the main page soft')
def open_main(context):
    context.app.sign_in_page.open_sign_in_page()
