Feature: Using selenium-requests
  As a developer
  I should be able to extend behave-webdriver with selenium-requests

  Scenario: use selenium-requests with behave-webdriver
    # use a behave-webdriver step
    Given the base url is "http://localhost:3000"
    # use your own steps using selenium-requests features
    Given I send a GET request to the page "http://localhost:3000"
    Then I expect the response text contains "<h1>DEMO APP</h1>"