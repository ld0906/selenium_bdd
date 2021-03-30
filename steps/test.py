from behave import given,when,then
from selenium.webdriver.common.by import By
import time


@given('输入用户名如下')
def step_impl(context):
    for row in context.table:
        context.driver.get("https://www.baidu.com")
        context.driver.find_element(By.ID,'kw').send_keys(row['name'])
        time.sleep(3)
        context.driver.find_element(By.ID, 'kw').clear()


@when('打开页面')
def step_impl(context):
    context.driver.find_element(By.ID,'kw').send_keys('test')
    time.sleep(3)

@then('输出用户名')
def step_impl(context):
    pass
