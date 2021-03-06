# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


from __future__ import absolute_import

import unittest

import clicksend_client
from clicksend_client.api.account_api import AccountApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self):
        self.api = clicksend_client.api.account_api.AccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_account_get(self):
        """Test case for account_get

        Get account information  # noqa: E501
        """
        pass

    def test_account_post(self):
        """Test case for account_post

        Create a new account  # noqa: E501
        """
        pass

    def test_account_verify_send_put(self):
        """Test case for account_verify_send_put

        Send account activation token  # noqa: E501
        """
        pass

    def test_account_verify_verify_by_activation_token_put(self):
        """Test case for account_verify_verify_by_activation_token_put

        Verify new account  # noqa: E501
        """
        pass

    def test_forgot_password_put(self):
        """Test case for forgot_password_put

        Forgot password  # noqa: E501
        """
        pass

    def test_forgot_password_verify_put(self):
        """Test case for forgot_password_verify_put

        Verify forgot password  # noqa: E501
        """
        pass

    def test_forgot_username_put(self):
        """Test case for forgot_username_put

        Forgot username  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
