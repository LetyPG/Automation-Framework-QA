Feature: User Account Management
  As a registered user
  I want to manage my account information
  So that I can keep my profile up-to-date and secure

  Background:
    Given I am logged into my account

  @ui @account @smoke
  Scenario: View account information
    Given I am on the account dashboard
    When I navigate to "Account Information"
    Then I should see my personal details
    And I should see my email address
    And I should see my name displayed

  @ui @account @critical
  Scenario: Update account email successfully
    Given I am on the account information page
    When I update my email to "newemail@example.com"
    And I confirm the changes with my password
    Then I should see a success message "You saved the account information."
    And my email should be updated to "newemail@example.com"

  @ui @account @critical
  Scenario: Change account password
    Given I am on the account information page
    When I click on "Change Password"
    And I enter my current password "OldPass123!"
    And I enter my new password "NewPass456!"
    And I confirm my new password "NewPass456!"
    And I save the changes
    Then I should see a success message "You saved the account information."
    And I should be able to login with my new password

  @ui @account
  Scenario: Update personal information
    Given I am on the account information page
    When I update my first name to "John"
    And I update my last name to "Doe"
    And I save the changes
    Then I should see a success message
    And my name should be updated to "John Doe"

  @ui @account @negative
  Scenario: Fail to update email with invalid format
    Given I am on the account information page
    When I update my email to "invalid-email"
    And I save the changes
    Then I should see an error message "Please enter a valid email address"
    And my email should not be changed

  @ui @account @negative
  Scenario: Fail to change password with incorrect current password
    Given I am on the account information page
    When I click on "Change Password"
    And I enter an incorrect current password
    And I enter a new password "NewPass789!"
    And I save the changes
    Then I should see an error message "The password doesn't match this account"
    And my password should not be changed

  @ui @account @security
  Scenario: Password must meet complexity requirements
    Given I am on the account information page
    When I click on "Change Password"
    And I enter my current password
    And I enter a weak password "123"
    And I save the changes
    Then I should see an error message about password strength
    And the password should not be updated

  @ui @account
  Scenario: View order history from account
    Given I am on the account dashboard
    When I navigate to "My Orders"
    Then I should see a list of my previous orders
    And each order should display order number, date, and status

  @ui @account
  Scenario: View address book
    Given I am on the account dashboard
    When I navigate to "Address Book"
    Then I should see my saved addresses
    And I should see options to add, edit, or delete addresses

  @ui @account
  Scenario Outline: Update account with different valid emails
    Given I am on the account information page
    When I update my email to "<email>"
    And I confirm the changes with my password
    Then I should see a success message
    And my email should be updated to "<email>"

    Examples:
      | email                    |
      | john.doe@example.com     |
      | jane_smith@test.co.uk    |
      | user+test@domain.org     |