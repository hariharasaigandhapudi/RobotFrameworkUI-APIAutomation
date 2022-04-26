from RequestsLibrary import RequestsOnSessionKeywords as r
from robot.api.deco import keyword
from robot.api import logger
from robot.utils import asserts
from schema import Schema, And, Use, Optional, SchemaError


class Requests(r):
    @keyword
    def create_session_for_api(self,session,url,headers):
        self.create_session(alias=session,url=url,headers=headers)

    @keyword
    def get_api_details(self,session, url):
        response = self.get_on_session(alias=session,url=url)
        return response

    @keyword
    def post_api_details(self, session, url,payload):
        response = self.post_on_session(alias=session, url=url,json=payload)
        return response

    @keyword
    def get_response_code(self,response):
        asserts.assert_equal(response.status_code,200,"Status code is not matched.")

    @keyword
    def post_response_code(self, response):
        asserts.assert_equal(response.status_code,201, "Status code is not matched.")

    @keyword
    def get_response_in_json(self, response):
        logger.info(response.json())

    @keyword
    def validate_response_structure(self,conf_schema, response):
        try:
            conf_schema.validate(response.json())
            logger.info("Validated response structure with expected one")
        except SchemaError:
            asserts.fail("Response structure is not as expected.")


