from behave import given,when,then
from selenium.webdriver.common.by import By
import time

#Scenario: login-logout2
@given('在登录页面输入用户名 "{username}" ,密码 "{password}"')
def step_impl(context,username,password):
    context.driver.get("http://127.0.0.1:8000/admin/login/")
    context.driver.find_element(By.ID, "id_username").send_keys(username)
    context.driver.find_element(By.ID, "id_password").send_keys(password)

@when('点击登录按钮')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[contains(@data-clicked-text,'Signing in')]").click()

@then('判断登录是否成功，页面有字样 "{username}" ,然后登出系统')
def step_impl(context,username):
    assert username in context.driver.page_source
    context.driver.find_element(By.XPATH, "//em[contains(text(),'" + username + "')]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Log out')]").click()
    time.sleep(3)