Feature: Product Service API
  As an API client
  I want to interact with the product service
  So that I can manage and retrieve product information

  @api @product @smoke
  Scenario: Retrieve all products
    Given the product service is available
    When I request all products
    Then the response status code should be 200
    And the response should contain a list of products
    And each product should have id, name, and price fields

  @api @product @smoke
  Scenario: Retrieve a specific product by ID
    Given the product service is available
    When I request the product with ID "1"
    Then the response status code should be 200
    And the response body should contain product details
    And the product should have a valid name
    And the product should have a valid price

  @api @product @critical
  Scenario: Create a new product
    Given the product service is available
    When I create a product with the following details:
      | name        | Test Product        |
      | price       | 29.99              |
      | category    | Electronics        |
      | description | A test product     |
    Then the response status code should be 201
    And the response should contain the created product
    And the product should have an assigned ID

  @api @product @critical
  Scenario: Update an existing product
    Given the product service is available
    And a product with ID "1" exists
    When I update the product with ID "1" with:
      | name  | Updated Product Name |
      | price | 39.99               |
    Then the response status code should be 200
    And the response should contain the updated product
    And the product name should be "Updated Product Name"
    And the product price should be "39.99"

  @api @product
  Scenario: Partially update a product (PATCH)
    Given the product service is available
    And a product with ID "2" exists
    When I partially update the product with ID "2":
      | price | 49.99 |
    Then the response status code should be 200
    And only the price should be updated to "49.99"
    And other product fields should remain unchanged

  @api @product @critical
  Scenario: Delete a product
    Given the product service is available
    And a product with ID "5" exists
    When I delete the product with ID "5"
    Then the response status code should be 204
    When I request the product with ID "5"
    Then the response status code should be 404

  @api @product @negative
  Scenario: Retrieve non-existent product
    Given the product service is available
    When I request the product with ID "999999"
    Then the response status code should be 404
    And the response should contain an error message

  @api @product @negative
  Scenario: Create product with missing required fields
    Given the product service is available
    When I create a product without a name
    Then the response status code should be 400
    And the response should contain a validation error
    And the error should mention "name is required"

  @api @product @negative
  Scenario: Create product with invalid price
    Given the product service is available
    When I create a product with price "-10.00"
    Then the response status code should be 400
    And the response should contain a validation error
    And the error should mention "invalid price"

  @api @product @validation
  Scenario: Product response matches expected schema
    Given the product service is available
    When I request the product with ID "1"
    Then the response status code should be 200
    And the response schema should be valid for "product_schema.json"

  @api @product
  Scenario: Filter products by category
    Given the product service is available
    When I request products with category "Electronics"
    Then the response status code should be 200
    And all returned products should belong to "Electronics" category
    And the results should contain at least 1 product

  @api @product
  Scenario: Filter products by price range
    Given the product service is available
    When I request products with price between "20" and "50"
    Then the response status code should be 200
    And all returned products should have prices between 20 and 50
    And the results should be sorted by price

  @api @product
  Scenario: Search products by name
    Given the product service is available
    When I search for products with name containing "Phone"
    Then the response status code should be 200
    And all returned products should have "Phone" in their name
    And the response should include match count

  @api @product @pagination
  Scenario: Paginate through products
    Given the product service is available
    When I request products with page "1" and limit "10"
    Then the response status code should be 200
    And the response should contain 10 products
    And the response should include pagination metadata
    And I should be able to request the next page

  @api @product
  Scenario: Get products sorted by price ascending
    Given the product service is available
    When I request all products sorted by "price" in "asc" order
    Then the response status code should be 200
    And the products should be sorted by price in ascending order

  @api @product
  Scenario Outline: Retrieve products in different categories
    Given the product service is available
    When I request products in category "<category>"
    Then the response status code should be 200
    And all products should be in "<category>" category
    And the response should contain at least <min_count> products

    Examples:
      | category    | min_count |
      | Electronics | 5         |
      | Clothing    | 10        |
      | Books       | 8         |
      | Home        | 6         |

  @api @product @performance
  Scenario: Product API responds within acceptable time
    Given the product service is available
    When I request all products
    Then the response should be received within 2 seconds
    And the response status code should be 200

  @api @product @security
  Scenario: Unauthorized access to create product
    Given I am not authenticated
    When I attempt to create a product
    Then the response status code should be 401
    And the response should contain "unauthorized" message