from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.api import logger
import pageobj
from robot.utils import asserts
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class UIselenium(SeleniumLibrary):

    #Declaring global variable to fetch page objects from pageobject.yaml file
    global obj_dict
    # Calling pageobjects yaml to load and assigned to global variable,Using global variable page object will be calling
    obj_dict = pageobj.load_yaml_pageobj_file("pageobject")

    @keyword('open page')
    # def open_page(self,base_url,browserName,browser_version,platform,os_version,page_title):
    def open_page(self, base_url, browserName, page_title):
        """
        This method relates to open page in browser and verifying page title once page open successfully.
            Args:
                base_url(string)- Url of the page should be passed
                browser(string)- Type of browser in which test case has to execute
                page_title(string) - Title of the page to verify once page opens successfully
            Return:
                None

        """
        logger.console("Opening Browser: " + browserName)
        logger.console("Base URL: "+ base_url)
        # browser_cap = {"browser": browserName,"browser_version":browser_version,"os":platform,"os_version": os_version}
        # remote_url = "https://hariharasaigandh_lgtUMF:Eaj6eQb9zPSjQmfFuH1G@hub-cloud.browserstack.com/wd/hub"
        # browser_options = Options()
        # # browser_options.add_argument('--headless')
        # browser_options.add_argument('--no-sandbox')
        # browser_options.add_argument('--disable-dev-shm-usage')
        # self.open_browser(url=base_url,browser=browserName,options=chrome_options,desired_capabilities=browser_cap,remote_url=remote_url)
        if browserName== "chrome":
            browsermanager = ChromeDriverManager()
            self.open_browser(url=base_url, browser=browserName,executable_path=browsermanager.install())
        elif browserName== "ff":
            browsermanager = GeckoDriverManager()
            self.open_browser(url=base_url, browser=browserName,executable_path=browsermanager.install())
        elif browserName== "edge":
            browsermanager = EdgeChromiumDriverManager()
            self.open_browser(url=base_url, browser=browserName,executable_path=browsermanager.install())
        self.title_should_be(page_title)

    @keyword('click signin button')
    def click_signin_button(self):
        """
        This method relates to clicking on sign in button
            Args:
                None
            Return:
                None
        """
        self.click_element(obj_dict["signup"]["signup_button"])

    @keyword('enter email to create account')
    def enter_email_to_create_account(self,email):
        """
        This method relates to enter email in corresponding field to signup
            Args:
                    email(string)- email text to enter in email field
            Return:
                    None
        """
        self.wait_until_element_is_enabled(obj_dict["signup"]["create_account_email"])
        self.input_text(obj_dict["signup"]["create_account_email"],email)

    @keyword('click create account button')
    def click_create_account_button(self):
        """
        This method relates to clicking create account button
            Args:
                   None
            Return:
                    None
        """
        self.click_element(obj_dict["signup"]["create_account_button"])

    @keyword('verify create account page opened')
    def verify_create_account_page_opened(self):
        """
        This method relates to verify create account page is opened
            Args:
                   None
            Return:
                    None
        """
        self.wait_until_element_is_visible(obj_dict["signup"]["create_account_div"],60)
        logger.console(self.get_text(obj_dict["signup"]["create_account_div"]))
        asserts.assert_true("CREATE AN ACCOUNT" == self.get_text(obj_dict["signup"]["create_account_div"]), "Create Account page is not opened")

    @keyword('enter title to the account')
    def enter_title_to_the_account(self, title):
        """
        This method relates to clicking title radio button of the user
            Args:
                   title(string) - title to be selected based on this input
            Return:
                    None
        """
        if title== "Mr":
            self.click_element(obj_dict["signup"]["create_account_gender_mr"])
        else:
            self.click_element(obj_dict["signup"]["create_account_gender_mrs"])

    @keyword('enter firstname to create account')
    def enter_firstname_to_create_account(self, firstname):
        """
        This method relates to enter firstname to create account
            Args:
                   firstname(string) - firstname field text to enter
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_firstname"], firstname)

    @keyword('enter lastname to create account')
    def enter_lastname_to_create_account(self, lastname):
        """
        This method relates to enter lastname to create account
            Args:
                   lastname(string) - lastname field text to enter
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_lastname"], lastname)

    @keyword('enter password to create account')
    def enter_password_to_create_account(self, password):
        """
        This method relates to enter password to create account
            Args:
                   password(string) - password field text to enter
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_password"], password)

    @keyword('select date of birth to create account')
    def select_date_of_birth_to_create_account(self, date, month, year):
        """
        This method relates to select date of birth to create account
            Args:
                   date(string) - date field text to select from drop down
                   month(string) - month field text to select from drop down
                   year(string) - year field text to select from drop down
            Return:
                    None
        """
        self.select_from_list_by_value(obj_dict["signup"]["create_account_dob_date"], date)
        self.select_from_list_by_value(obj_dict["signup"]["create_account_dob_month"], month)
        self.select_from_list_by_value(obj_dict["signup"]["create_account_dob_year"], year)

    @keyword('signup for newsletter')
    def signup_for_newsletter(self):
        """
        This method relates to check signup news letter
            Args:
                   None
            Return:
                    None
        """
        self.click_element(obj_dict["signup"]["create_account_signup_newsletter"])

    @keyword('receive special offers from partners')
    def receive_special_offers_from_partners(self):
        """
        This method relates to check to receive special offer from partners
            Args:
                   None
            Return:
                    None
        """
        self.click_element(obj_dict["signup"]["create_account_special_offers"])


    @keyword('enter firstname in address to create account')
    def enter_firstname_in_address_to_create_account(self, firstname):
        """
        This method relates to enter firstname in address to create account
            Args:
                   firstname(string) - firstname field text to enter in address
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_address_firstname"], firstname)

    @keyword('enter lastname in address to create account')
    def enter_lastname_in_address_to_create_account(self, lastname):
        """
        This method relates to enter lastname in address to create account
            Args:
                   lastname(string) - lastname field text to enter in address
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_address_lastname"], lastname)

    @keyword('enter company in address to create account')
    def enter_company_in_address_to_create_account(self, company):
        """
        This method relates to enter company in address to create account
            Args:
                   company(string) - company field text to enter in address
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_address_company"], company)

    @keyword('enter address line1 in address to create account')
    def enter_address_line1_in_address_to_create_account(self, address1):
        """
        This method relates to enter address line1 in address to create account
            Args:
                   address1(string) - address line1 field text to enter in address
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_address_address"], address1)

    @keyword('enter address line2 in address to create account')
    def enter_address_line2_in_address_to_create_account(self, address2):
        """
        This method relates to enter address line2 in address to create account
            Args:
                   address2(string) - address line2 field text to enter in address
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_address_address_line2"], address2)

    @keyword('enter city in address to create account')
    def enter_city_in_address_to_create_account(self, city):
        """
        This method relates to enter city in address to create account
            Args:
                   city(string) - city field text to enter in address
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_address_city"], city)

    @keyword('select state in address to create account')
    def enter_state_in_address_to_create_account(self, state):
        """
        This method relates to select state in address to create account
            Args:
                   state(string) - state field text to select in address
            Return:
                    None
        """
        self.select_from_list_by_label(obj_dict["signup"]["create_account_address_state"], state)

    @keyword('enter postalcode in address to create account')
    def enter_postalcode_in_address_to_create_account(self, postalcode):
        """
        This method relates to enter postalcode in address to create account
            Args:
                   postalcode(string) - postalcode field text to enter in address
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_address_zip"], postalcode)

    @keyword('select country in address to create account')
    def enter_country_in_address_to_create_account(self, country):
        """
        This method relates to select country in address to create account
            Args:
                   country(string) - country field text to select in address
            Return:
                    None
        """
        self.select_from_list_by_label(obj_dict["signup"]["create_account_address_country"], country)

    @keyword('enter additional information in address to create account')
    def enter_additional_information_in_address_to_create_account(self, addl_info):
        """
        This method relates to enter additional information in address to create account
            Args:
                   addl_info(string) - additional information field text to enter in address
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_address_additional_information"], addl_info)

    @keyword('enter home phone in address to create account')
    def enter_home_phone_in_address_to_create_account(self, homephone):
        """
        This method relates to enter homephone in address to create account
            Args:
                   homephone(string) - homephone field text to enter in address
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_address_homephone"], homephone)

    @keyword('enter mobile phone in address to create account')
    def enter_mobile_phone_in_address_to_create_account(self, mobilephone):
        """
        This method relates to enter mobilephone in address to create account
            Args:
                   mobilephone(string) - mobilephone field text to enter in address
            Return:
                    None
        """
        self.input_text(obj_dict["signup"]["create_account_address_mobilephone"], mobilephone)

    @keyword('assign address for future reference to create account')
    def assign_address_for_future_reference_to_create_account(self, assignaliasaddress):
        """
        This method relates to enter assign address for future reference to create account
            Args:
                   assignaliasaddress(string) - assignaliasaddress field text to enter in address
            Return:
                    None
        """
        if assignaliasaddress != "My Address":
            self.clear_element_text(obj_dict["signup"]["create_account_address_assign_future_ref"])
            self.input_text(obj_dict["signup"]["create_account_address_assign_future_ref"], assignaliasaddress)
        else:
            pass

    @keyword('click register button to create account')
    def click_register_button_to_create_account(self):
        """
        This method relates to click register button to create account
            Args:
                   None
            Return:
                    None
        """
        self.click_element(obj_dict["signup"]["create_account_register_button"])

    @keyword('verify new account created successfully and account page should be open')
    def verify_new_account_created_successfully_and_account_page_should_be_open(self):
        """
            This method relates to verify new account created successfully and account page should be open
                Args:
                       None
                Return:
                        None
        """
        self.wait_until_element_is_visible(obj_dict["signup"]["create_account_myaccount_div"], 60)
        logger.console(self.get_text(obj_dict["signup"]["create_account_myaccount_div"]))
        asserts.assert_true("MY ACCOUNT" == self.get_text(obj_dict["signup"]["create_account_myaccount_div"]),
                            "My Account page is not opened")

    @keyword('click signout button on page')
    def click_signout_button_on_page(self):
        """
            This method relates to click signout button on page
                Args:
                       None
                Return:
                        None
        """
        self.click_element(obj_dict["mainpage"]["signout_button"])

