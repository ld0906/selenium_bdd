from behave import given,when,then
from selenium.webdriver.common.by import By
import time

#

# Scenario 1: 打开管理员登录页面
@given('在浏览器地址栏里输入网址 "{url}" 并点击回车键1')
def step_impl(context,url):
    #context.driver = webdriver.Firefox()
    context.driver.get(url)

@when('页面加载完毕1')
def step_impl(context):
    time.sleep(3)

@then('页面会出现 "{keyword}" 字样1')
def step_impl(context,keyword):
    assert keyword in context.driver.page_source


#Scenario 2: 管理员登录登出, 这里使用context.table是在given步骤内，一直循环，知道循环体结束再执行其他步骤，
#比如when步骤。

@given('分别在对应的输入框中输入用户名和密码，并且点击Sign in按钮')
def step_impl(context):
    for row in context.table:
        context.driver.find_element(By.ID, "id_username").clear()
        context.driver.find_element(By.ID,"id_username").send_keys(row['name'])
        context.driver.find_element(By.ID, "id_password").clear()
        context.driver.find_element(By.ID,"id_password").send_keys(row['passwd'])
        context.driver.find_element(By.XPATH, "//button[contains(@data-clicked-text,'Signing in')]").click()


@when('登录成功，出现字符"{login_keyword}"')
def step_impl(context,login_keyword):
   assert login_keyword in context.driver.page_source

@then('点击页面左下角向上符号，并且点击"{logout}"超链接,出现字样"{logout_keyword}"')
def step_impl(context,logout,logout_keyword):
    for row in context.table:
        context.driver.find_element(By.XPATH, "//em[contains(text(),'" + row['name'] + "')]").click()
        time.sleep(5)
        context.driver.find_element(By.XPATH, "//a[contains(text(),'" + logout + "')]").click()
        time.sleep(5)
        assert logout_keyword in context.driver.page_source

