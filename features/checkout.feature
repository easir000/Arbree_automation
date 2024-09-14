Feature: Checkout an item from SauceDemo

  Scenario: Successful checkout process
    Given I navigate to the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    And I add "Sauce Labs Backpack" to the cart
    Then I verify that "Sauce Labs Backpack" is added to the cart
    And I proceed to checkout
    And I complete the checkout with "Easir", "Maruf", and "1234"
    Then I verify the checkout is successful
