from selenium import webdriver


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.quit()
