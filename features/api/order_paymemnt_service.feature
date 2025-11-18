Feature: Order Payment API
  As an API client
  I want to process order payments
  So that customers can complete their purchases

  @api @payment @smoke
  Scenario: Process a successful payment
    Given the payment service is available
    And I have a valid order with ID "12345"
    When I submit a payment for order "12345" with:
      | amount        | 99.99           |
      | currency      | USD             |
      | payment_method| credit_card     |
      | card_number   | 4111111111111111|
    Then the response status code should be 200
    And the payment status should be "completed"
    And the payment should have a transaction ID
    And the order status should be updated to "paid"

  @api @payment @critical
  Scenario: Process payment with valid credit card
    Given the payment service is available
    And I have an order ready for payment
    When I process payment with credit card "4532015112830366"
    And the CVV is "123"
    And the expiry date is "12/2025"
    Then the response status code should be 200
    And the payment should be authorized
    And I should receive a payment confirmation

  @api @payment @critical
  Scenario: Process payment with PayPal
    Given the payment service is available
    And I have an order with total "149.99"
    When I initiate PayPal payment
    Then the response status code should be 200
    And I should receive a PayPal redirect URL
    And the payment status should be "pending"

  @api @payment @negative
  Scenario: Reject payment with invalid card number
    Given the payment service is available
    When I submit payment with card number "1234567890123456"
    Then the response status code should be 400
    And the response should contain error "invalid card number"
    And the payment should not be processed

  @api @payment @negative
  Scenario: Reject payment with expired card
    Given the payment service is available
    When I submit payment with card expiry "01/2020"
    Then the response status code should be 400
    And the response should contain error "card expired"
    And the payment status should be "failed"

  @api @payment @negative
  Scenario: Reject payment with insufficient funds
    Given the payment service is available
    When I submit payment for amount "10000.00"
    And the card has insufficient funds
    Then the response status code should be 402
    And the response should contain error "insufficient funds"
    And the payment should be declined

  @api @payment @negative
  Scenario: Reject payment without required fields
    Given the payment service is available
    When I submit payment without card number
    Then the response status code should be 400
    And the response should contain validation error
    And the error should mention "card_number is required"

  @api @payment @security
  Scenario: Payment data is transmitted securely
    Given the payment service is available
    When I submit a payment request
    Then the connection should use HTTPS
    And the card number should be encrypted in transit
    And sensitive data should not appear in logs

  @api @payment
  Scenario: Process partial refund
    Given the payment service is available
    And I have a completed payment with ID "PAY123"
    And the original amount was "100.00"
    When I request a partial refund of "30.00"
    Then the response status code should be 200
    And the refund should be processed
    And the refunded amount should be "30.00"
    And the remaining payment should be "70.00"

  @api @payment
  Scenario: Process full refund
    Given the payment service is available
    And I have a completed payment with ID "PAY456"
    When I request a full refund
    Then the response status code should be 200
    And the payment status should be "refunded"
    And the full amount should be refunded
    And the customer should receive refund confirmation

  @api @payment @negative
  Scenario: Prevent duplicate payment processing
    Given the payment service is available
    And I have submitted a payment with reference "REF789"
    When I submit the same payment again with reference "REF789"
    Then the response status code should be 409
    And the response should contain error "duplicate transaction"
    And no additional payment should be processed

  @api @payment
  Scenario: Retrieve payment details
    Given the payment service is available
    And a payment with ID "PAY999" exists
    When I request payment details for "PAY999"
    Then the response status code should be 200
    And the response should contain payment amount
    And the response should contain payment method
    And the response should contain transaction date
    And the response should contain payment status

  @api @payment @validation
  Scenario: Payment response matches expected schema
    Given the payment service is available
    When I process a valid payment
    Then the response status code should be 200
    And the response schema should be valid for "payment_schema.json"
    And all required fields should be present

  @api @payment
  Scenario: List all payments for an order
    Given the payment service is available
    And order "ORD123" has multiple payment attempts
    When I request all payments for order "ORD123"
    Then the response status code should be 200
    And the response should contain a list of payments
    And each payment should have status and amount
    And payments should be ordered by date descending

  @api @payment
  Scenario: Update payment status
    Given the payment service is available
    And a pending payment with ID "PAY111" exists
    When I update the payment status to "completed"
    Then the response status code should be 200
    And the payment status should be "completed"
    And the update timestamp should be recorded

  @api @payment @authorization
  Scenario: Authorize payment without capture
    Given the payment service is available
    When I authorize a payment of "250.00" without capturing
    Then the response status code should be 200
    And the payment status should be "authorized"
    And the funds should be reserved
    And the payment should not be captured yet

  @api @payment
  Scenario: Capture previously authorized payment
    Given the payment service is available
    And I have an authorized payment with ID "PAY222"
    When I capture the authorized payment
    Then the response status code should be 200
    And the payment status should be "captured"
    And the funds should be transferred

  @api @payment
  Scenario Outline: Process payments in different currencies
    Given the payment service is available
    When I submit payment of "<amount>" in "<currency>"
    Then the response status code should be 200
    And the payment should be processed in "<currency>"
    And the converted amount should be calculated

    Examples:
      | amount | currency |
      | 100.00 | USD      |
      | 85.50  | EUR      |
      | 75.00  | GBP      |
      | 500.00 | MXN      |

  @api @payment @webhook
  Scenario: Receive payment webhook notification
    Given the payment service is available
    And I have configured a webhook endpoint
    When a payment is completed
    Then a webhook should be sent to my endpoint
    And the webhook should contain payment details
    And the webhook signature should be valid

  @api @payment @performance
  Scenario: Payment processing completes within acceptable time
    Given the payment service is available
    When I submit a valid payment
    Then the payment should be processed within 3 seconds
    And the response status code should be 200

  @api @payment @timeout
  Scenario: Handle payment gateway timeout
    Given the payment service is available
    When the payment gateway times out
    Then the response status code should be 504
    And the response should contain timeout error
    And the payment status should be "pending"
    And a retry mechanism should be available