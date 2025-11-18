Feature: Product Search
  As a customer
  I want to search for products
  So that I can quickly find items I want to purchase

  @ui @search @smoke
  Scenario: Search for a product by name
    Given I am on the homepage
    When I search for "jacket"
    Then I should see search results for "jacket"
    And the results should contain relevant products
    And each product should display name, price, and image

  @ui @search @critical
  Scenario: Search with exact product name
    Given I am on the homepage
    When I search for "Radiant Tee"
    Then I should see "Radiant Tee" in the search results
    And the first result should be "Radiant Tee"

  @ui @search
  Scenario: Search with partial product name
    Given I am on the homepage
    When I search for "shirt"
    Then I should see multiple products containing "shirt"
    And the results count should be greater than 1

  @ui @search
  Scenario: Filter search results by price
    Given I am on the homepage
    When I search for "shoes"
    And I filter by price range "$50 - $100"
    Then all displayed products should be within the price range
    And I should see a filter indicator for "$50 - $100"

  @ui @search
  Scenario: Filter search results by category
    Given I am on the homepage
    When I search for "clothing"
    And I filter by category "Women"
    Then I should see only women's products
    And the category filter "Women" should be active

  @ui @search
  Scenario: Sort search results by price ascending
    Given I am on the homepage
    When I search for "pants"
    And I sort by "Price: Low to High"
    Then the products should be sorted by price in ascending order
    And the first product should have the lowest price

  @ui @search
  Scenario: Sort search results by price descending
    Given I am on the homepage
    When I search for "bags"
    And I sort by "Price: High to Low"
    Then the products should be sorted by price in descending order
    And the first product should have the highest price

  @ui @search @negative
  Scenario: Search with no results
    Given I am on the homepage
    When I search for "xyznonexistentproduct123"
    Then I should see a message "Your search returned no results"
    And no products should be displayed
    And I should see suggestions to modify my search

  @ui @search @negative
  Scenario: Search with empty query
    Given I am on the homepage
    When I submit an empty search
    Then I should remain on the current page
    Or I should see all products

  @ui @search
  Scenario: Search with special characters
    Given I am on the homepage
    When I search for "t-shirt & pants"
    Then the search should handle special characters correctly
    And I should see relevant results

  @ui @search
  Scenario: View product details from search results
    Given I am on the homepage
    When I search for "watch"
    And I click on the first product in search results
    Then I should be navigated to the product detail page
    And I should see complete product information

  @ui @search
  Scenario: Add product to cart from search results
    Given I am on the homepage
    When I search for "bottle"
    And I select a product from search results
    And I add the product to cart
    Then the product should be added to my cart
    And I should see a success notification

  @ui @search @pagination
  Scenario: Navigate through search result pages
    Given I am on the homepage
    When I search for "top"
    And the results span multiple pages
    Then I should see pagination controls
    When I click on page 2
    Then I should see different products on page 2
    And the page indicator should show "2"

  @ui @search
  Scenario: Search suggestions appear while typing
    Given I am on the homepage
    When I start typing "jack" in the search box
    Then I should see autocomplete suggestions
    And suggestions should include "jacket"
    When I click on a suggestion
    Then the search should be executed with that term

  @ui @search
  Scenario Outline: Search for different product categories
    Given I am on the homepage
    When I search for "<product_type>"
    Then I should see search results for "<product_type>"
    And the results should contain at least <min_count> products

    Examples:
      | product_type | min_count |
      | shirt        | 5         |
      | pants        | 3         |
      | shoes        | 4         |
      | jacket       | 2         |
      | accessories  | 3         |

  @ui @search @performance
  Scenario: Search results load within acceptable time
    Given I am on the homepage
    When I search for "popular product"
    Then the search results should load within 3 seconds
    And all product images should be displayed

  @ui @search
  Scenario: Clear search and return to homepage
    Given I have searched for "test product"
    And I am viewing search results
    When I clear the search
    Then I should return to the homepage
    And the search box should be empty