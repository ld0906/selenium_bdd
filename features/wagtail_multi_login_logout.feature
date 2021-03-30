@test1
Feature: Login_Logout


  Scenario: 打开管理员登录页面
    Given 在浏览器地址栏里输入网址 "http://127.0.0.1:8000/admin/login/" 并点击回车键1
    When 页面加载完毕1
    Then 页面会出现 "Sign in to Wagtail" 字样1


  Scenario: 管理员登录登出
    Given 分别在对应的输入框中输入用户名和密码，并且点击Sign in按钮
      |name|passwd|
      |superuser|123456qq|
      |user1|189189qq|
      |user2|189189qq|
    When 登录成功，出现字符"Welcome to the mysite Wagtail CMS"
    Then 点击页面左下角向上符号，并且点击"Log out"超链接,出现字样"You have been successfully logged out"
      |name|passwd|
      |superuser|123456qq|
      |user1|189189qq|
      |user2|189189qq|

