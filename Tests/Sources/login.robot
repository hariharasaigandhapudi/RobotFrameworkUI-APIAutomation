*** Settings ***
Resource    ../Resources/ui_resource.robot

Test Setup  Test_setup
Test Teardown   Test_teardown

*** Test Cases ***

create_account
    [Template]  Test case to create account
    browserName=${browserName}
#    browser_version=${browser_version}  platform=${platform}    os_version=${os_version}
