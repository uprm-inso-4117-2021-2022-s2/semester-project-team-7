Feature: Home page image shown 
    Scenario: Image shown on home page 
        Given Launch Microsoft Edge 
        When Open page 
        Then Verify that the image is present 
        And Close Microsoft Edge 