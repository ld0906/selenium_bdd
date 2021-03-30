Feature: Test

  @test
  Scenario: TestS1
    Given 输入用户名如下
    |name|
    |jason1|
    |jason2|

    When 打开页面
    Then 输出用户名
