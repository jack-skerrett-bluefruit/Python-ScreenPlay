Feature: Blast Off - Manage Product Features

  Scenario: Add a feature with a name
    Given I am viewing Blast Off
    When I add a new feature called "Manage Product Features"
    Then "Manage Product Features" is in the list of features

  #Scenario: Feature cannot be added without a name
    #Given I am viewing Blast Off
    #When I add a new Feature without a name
    #Then no new Feature is in the Feature list

  Scenario: Edit a feature name
    Given I am viewing Blast Off
    And the feature "Manage Product Features" exists
    When "Manage Product Features" is changed to "This Name Has Been Changed" and saved
    Then the feature name is "This Name Has Been Changed"
