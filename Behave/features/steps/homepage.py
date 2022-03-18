from behave import *
from selenium import webdriver

@given('Launch Microsoft Edge')
def step_impl(context):
    context.driver=webdriver.Edge()

@when('Open page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:8000/")

@then('Verify that the image is present')
def step_impl(context):
    status=context.driver.find_element_by_class_name("cover-img").is_displayed()
    assert status is True

@then('Close Microsoft Edge')
def step_impl(context):
    context.driver.close()