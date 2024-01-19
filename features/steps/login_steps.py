from lib2to3.pgen2 import driver

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@given(u'I am on the homepage')
def step_impl(context):
    context.browser.get("https://magento.softwaretestingboard.com/")
    assert (context.browser.find_element(By.CSS_SELECTOR, "div[class='panel header'] span[class='not-logged-in']"))


@when(u'I click sign in')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, "div[class='panel header'] li[data-label='or'] a").click()
    assert context.browser.find_element(By.CSS_SELECTOR, ".base").text == "Customer Login"


@when(u'I input email field with {email} email')
def step_impl(context, email):
    input_email = context.browser.find_element(By.CSS_SELECTOR, "#email")
    if email == 'correct':
        input_email.send_keys("Dam@inc.com")
    elif email == 'incorrect format':
        input_email.send_keys("dadinc.com")
    elif email == 'incorrect':
        input_email.send_keys("dad@inc.com")


@when(u'I input password field with {password} password')
def step_impl(context, password):
    input_password = context.browser.find_element(By.CSS_SELECTOR, "#pass")
    if password == 'correct':
        input_password.send_keys("Qwer1234!")
    elif password == 'incorrect':
        input_password.send_keys("Qweew")


@when(u'I click login button')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, "button.action.login.primary > span:nth-child(1)").click()


@then(u'I {result} login')
def step_impl(context, result):
    if result == 'successfully':
        context.browser.implicitly_wait(5)
        assert (context.browser.find_element(By.CSS_SELECTOR, "div[class='panel header'] span[class='logged-in']"))
    elif result == 'failed due incorrect password':
        context.browser.implicitly_wait(5)
        assert (context.browser.find_element(By.CSS_SELECTOR, "div[data-bind='html: $parent.prepareMessageForHtml("
                                                              "message.text)']"))
    elif result == 'failed due incorrect email format':
        context.browser.implicitly_wait(5)
        assert (context.browser.find_element(By.CSS_SELECTOR, "#email-error"))
