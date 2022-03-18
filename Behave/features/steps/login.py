from behave import *
from selenium import webdriver

@when('Go to login page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:8000/login")

@when('Input valid credentials')
def step_impl(context):
    context.driver.find_element_by_name("username").send_keys("test")
    context.driver.find_element_by_name("password").send_keys("testpass1234")
    context.driver.find_element_by_xpath("/html/body/form/div/div[4]/button").click()

@then('Successfully logged in')
def step_impl(context):
    usernamemenu = context.driver.find_element_by_link_text("test")
    assert usernamemenu.is_displayed()

@then('Input invalid credentials')
def step_impl(context):
    context.driver.find_element_by_name("username").send_keys("wrongusername")
    context.driver.find_element_by_name("password").send_keys("wrongpassword")
    context.driver.find_element_by_xpath("/html/body/form/div/div[4]/button").click()

@then('Could not login')
def step_impl(context):
    assert context.driver.current_url == "http://127.0.0.1:8000/login"