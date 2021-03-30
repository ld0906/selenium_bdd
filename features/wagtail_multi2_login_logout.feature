@test2
Feature: login-logout2
  Scenario Outline: 登录场景
    Given 在登录页面输入用户名 "<username>" ,密码 "<password>"
    When 点击登录按钮
    Then 判断登录是否成功，页面有字样 "<username>" ,然后登出系统

    Examples:
    |username   |password |
    |superuser  |123456qq |
    |user1      |189189qq |
    |user2      |189189qq |
