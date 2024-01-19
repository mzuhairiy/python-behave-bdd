Feature: Login Feature

Scenario Outline: User want to login with <condition>
    Given I am on the homepage
    When I click sign in
    And I input email field with <email> email
    And I input password field with <password> password
    And I click login button
    Then I <result> login

        Examples:
      | case     | condition            | email            | password  | result                            |
      | positive | valid credential     | correct          | correct   | successfully                      |
      | negative | wrong password       | correct          | incorrect | failed due incorrect password     |
      | negative | invalid email format | incorrect format | correct   | failed due incorrect email format |
    #  | negative | not registered email | incorrect        | correct   | failed                            |
    #  | negative | empty email field    | empty            | correct   | failed                            |
    #  | negative | empty password field | correct          | empty     | failed                            |