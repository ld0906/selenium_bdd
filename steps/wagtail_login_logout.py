from behave import given,when,then
from selenium.webdriver.common.by import By
import time


# Scenario 1: 打开管理员登录页面
@given('在浏览器地址栏里输入网址 "{url}" 并点击回车键')
def step_impl(context,url):
    #context.driver = webdriver.Firefox()
    context.driver.get(url)


@when('页面加载完毕')
def step_impl(context):
    time.sleep(5)

@then('页面会出现 "{keyword}" 字样')
def step_impl(context,keyword):
    assert keyword in context.driver.page_source


#Scenario 2: 管理员登录

@given('分别在对应的输入框中输入用户名:"{username}"和密码:"{password}"')
def step_impl(context,username,password):
    context.driver.find_element(By.ID,"id_username").send_keys(username)
    context.driver.find_element(By.ID,"id_password").send_keys(password)

@when('点击"{button_text}"按钮')
def step_impl(context,button_text):
    context.driver.find_element(By.XPATH,"//button[contains(@data-clicked-text,'Signing in')]").click()

@then('页面会出现欢迎界面，出现"{user_keyword}"字样')
def step_impl(context,user_keyword):
    assert user_keyword in context.driver.page_source


#Scenario 3: 登出系统
@given('点击页面左下角向上符号^')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//em[contains(text(),'superuser')]").click()

@when('当超链接"{logout}"出现时，单击此超链接')
def step_impl(context):
    pass





