Feature: User login 

    Background: Reaching Log in page 
        Given Launch Microsoft Edge 
        When Go to login page

    Scenario: Valid login details provided
        And Input valid credentials 
        Then Successfully logged in 

    Scenario: Invalid login details provided
        And Input invalid credentials 
        Then Could not login