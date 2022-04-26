*** Settings ***
Documentation    This suite relates to signup of page and login to page after signup.

Library     Requests
Library     inputconfig
Variables     schema_validation_file.py
Variables     payloads_file.py

*** Keywords ***

Test_setup
    set selenium implicit wait      1
    set selenium speed      .15
    set selenium timeout    30

Test_teardown
    Close All Browsers

Test case to fetch details
    ${resp}=    get_input_from_csv      input
    &{headers}=     Create Dictionary   "accept"="application/json"
    create session for api  ${resp}[session]    ${resp}[get_api_url]        ${headers}
    ${get_response}=    get api details     ${resp}[session]    ${resp}[get_api_url]
    get response code   ${get_response}
    get response in json    ${get_response}
    validate response structure     ${get_api}  ${get_response}
    delete all sessions

Test case to post details
    ${resp}=    get_input_from_csv      input
    &{headers}=     Create Dictionary   "Content-type"="application/json; charset=UTF-8"
    create session for api  ${resp}[session]    ${resp}[post_api_url]        ${headers}
    ${post_response}=    post api details     ${resp}[session]    ${resp}[post_api_url]  ${post_details}
    post response code   ${post_response}
    get response in json    ${post_response}
    validate response structure     ${post_api}  ${post_response}
    delete all sessions
