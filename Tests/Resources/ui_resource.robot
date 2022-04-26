*** Settings ***
Documentation    This suite relates to signup of page and login to page after signup.

Library     UIselenium
Library     inputconfig


*** Keywords ***

Test_setup
    set selenium implicit wait      1
    set selenium speed      .15
    set selenium timeout    30

Test_teardown
    Close All Browsers

Test case to create account
    [Arguments]     ${csv}=${Empty}     ${browserName}=${Empty}
    ${resp}=    get_input_from_csv      input
    ${email} =  set variable    ${resp}[create_account_mail]
    ${title} =  set variable    ${resp}[create_account_title]
    ${firstname} =  set variable    ${resp}[create_account_firstname]
    ${lastname} =  set variable    ${resp}[create_account_lastname]
    ${password} =  set variable    ${resp}[create_account_password]
    ${date} =  set variable    ${resp}[create_account_date]
    ${month} =  set variable    ${resp}[create_account_month]
    ${year} =  set variable    ${resp}[create_account_year]
    ${address_firstname} =  set variable    ${resp}[create_account_address_firstname]
    ${address_lastname} =  set variable    ${resp}[create_account_address_lastname]
    ${company} =  set variable    ${resp}[create_account_company]
    ${address1} =  set variable    ${resp}[create_account_address1]
    ${address2} =  set variable    ${resp}[create_account_address2]
    ${city} =  set variable    ${resp}[create_account_city]
    ${state} =  set variable    ${resp}[create_account_state]
    ${postalcode} =  set variable    ${resp}[create_account_postalcode]
    ${country} =  set variable    ${resp}[create_account_country]
    ${additional_info} =  set variable    ${resp}[create_account_additional_info]
    ${homephone} =  set variable    ${resp}[create_account_homephone]
    ${mobilephone} =  set variable    ${resp}[create_account_mobilephone]
    ${assignalias} =  set variable    ${resp}[create_account_assignalias]
    open page   ${resp}[base_url]   ${browserName}  ${resp}[page_title]
    click signin button
    enter email to create account   ${email}
    click create account button
    verify create account page opened
    enter title to the account  ${title}
    enter firstname to create account   ${firstname}
    enter lastname to create account    ${lastname}
    enter password to create account    ${password}
    select date of birth to create account   ${date}    ${month}    ${year}
    signup for newsletter
    receive special offers from partners
    enter firstname in address to create account    ${address_firstname}
    enter lastname in address to create account     ${address_lastname}
    enter company in address to create account      ${company}
    enter address line1 in address to create account    ${address1}
    enter address line2 in address to create account    ${address2}
    enter city in address to create account     ${city}
    select state in address to create account   ${state}
    enter postalcode in address to create account   ${postalcode}
    select country in address to create account     ${country}
    enter additional information in address to create account   ${additional_info}
    enter home phone in address to create account   ${homephone}
    enter mobile phone in address to create account     ${mobilephone}
    assign address for future reference to create account   ${assignalias}
    click register button to create account
    verify new account created successfully and account page should be open
    click signout button on page







