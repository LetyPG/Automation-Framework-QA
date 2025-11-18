Feature: User Login
  As a registered user
  I want to log in
  So I can access my account

  @ui @login @smoke
  Scenario: Successful Login
    Given I am on the login page
    When I enter "standard_user" and "secret_sauce"
    Then I should be logged in successfully