from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open the main page soft')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()

@then ("Log in to the page")
def input_email_and_password(context):
    context.app.sign_in_page.input_email_and_password('galactionov94@gmail.com', '1234567890QQQ!')

@then ("Click on the continue button")
def click_sign_in(context):
    context.app.sign_in_page.click_sign_in()
    sleep(10)