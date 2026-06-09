Feature: Donation Registration

  Scenario: Successful donation registration
    Given a donor named "John"
    When they donate 100
    Then the system should display "Donation of £100 received from John"

  Scenario: Invalid donation amount
    Given a donor named "Alex"
    When they donate -50
    Then the system should display "Invalid donation amount"

  Scenario: Empty donor name
    Given an empty donor name
    When they donate 100
    Then the system should display "Invalid donor name"