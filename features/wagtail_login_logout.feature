Feature: Create_User
  Scenario: 打开管理员登录页面
    Given 在浏览器地址栏里输入网址 "http://127.0.0.1:8000/admin/login/" 并点击回车键
    When 页面加载完毕
    Then 页面会出现 "Sign in to Wagtail" 字样

  Scenario: 管理员登录
    Given 分别在对应的输入框中输入用户名:"superuser"和密码:"123456qq"
    When 点击"Sign in"按钮
    Then 页面会出现欢迎界面，出现"superuser"字样

  Scenario: 登出系统
    Given  点击页面左下角向上符号^
    When 当超链接"Log out"出现时，单击此超链接
    Then 页面跳转到登录页面，并且有字样"You have been successfully logged out"
