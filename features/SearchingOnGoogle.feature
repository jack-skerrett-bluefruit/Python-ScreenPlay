Feature: Searching the internet
  Anything can be searched for on Google

  Scenario: Searching for "Hello World"
    Given Byran has opened Google
    When they search for "Hello World"
    Then they should see a result for '"Hello, World!" program - Wikipedia'
