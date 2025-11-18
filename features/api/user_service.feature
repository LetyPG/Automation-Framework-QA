Feature: User Service API
  As a client of the system
  I want to retrieve and validate user data
  To ensure the API is working correctly

  @api @user_service @smoke
  Scenario: Retrieve a specific user's data
    Given the user service is available
    When I request the user with ID "2"
    Then the response status code should be 200
    And the response body should contain the user email "janet.weaver@reqres.in"
    And the response schema should be valid