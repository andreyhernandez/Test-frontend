@regression_tests

Feature: Validate element created dropdown column

  Scenario: Validate URL of Home page
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The url page should be equal to the next "https://www.kayak.com.co/" url

  Scenario Outline: Navigate between countries and validate the URL
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I navigate to the "<url>" URL
    Then The url page should be equal to the next "<url>" url

    Examples:
      | url                       |
      | https://www.kayak.com.my/ |
      | https://www.kayak.com.pr/ |
      | https://www.kayak.com.br/ |

  
  Scenario Outline: Navigate between countries and validate the URL
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I click on the menu button
    And I click on the "<option>" option
    Then The url page should be equal to the next "<url>" url

    Examples: 
      | option                     | url                                                   |
      | search_for_flights         | https://www.kayak.com.co/flights                      |
      | search_for_hotels          | https://www.kayak.com.co/stays                        |
      | car_search                 | https://www.kayak.com.co/cars                         |
      | Go_to_Explore              | https://www.kayak.com.co/explore/                     |
      | Visit_our_blog             | https://www.kayak.com.co/news/                        |
      | Search_for_direct_flights  | https://www.kayak.com.co/direct                       |
      | best_time_to_travel        | https://www.kayak.com.co/el-mejor-momento-para-viajar |
      | KAYAK_for_Business         | https://www.kayak.com.co/business                     |
      | Trips                      | https://www.kayak.com.co/trips                        |

      

  Scenario Outline: Navigate between options and validate the URL
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I navigate to the "<url>" URL
    Then The url page should be equal to the next "<url>" url

    Examples:
      | url                                                   |
      | https://www.kayak.com.co/flights                      |
      | https://www.kayak.com.co/stays                        |
      | https://www.kayak.com.co/cars                         |
      | https://www.kayak.com.co/news/                        |
      | https://www.kayak.com.co/direct                       |
      | https://www.kayak.com.co/el-mejor-momento-para-viajar |
      | https://www.kayak.com.co/business                     |
      | https://www.kayak.com.co/trips                        |
     


