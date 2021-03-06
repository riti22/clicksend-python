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
from clicksend_client.api.email_to_sms_api import EmailToSmsApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestEmailToSmsApi(unittest.TestCase):
    """EmailToSmsApi unit test stubs"""

    def setUp(self):
        self.api = clicksend_client.api.email_to_sms_api.EmailToSmsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sms_email_sms_get(self):
        """Test case for sms_email_sms_get

        Get list of email to sms allowed addresses  # noqa: E501
        """
        pass

    def test_sms_email_sms_post(self):
        """Test case for sms_email_sms_post

        Create email to sms allowed address  # noqa: E501
        """
        pass

    def test_sms_email_sms_stripped_string_delete(self):
        """Test case for sms_email_sms_stripped_string_delete

        Delete email to sms stripped string rule  # noqa: E501
        """
        pass

    def test_sms_email_sms_stripped_string_get(self):
        """Test case for sms_email_sms_stripped_string_get

        Get email to sms stripped string rule  # noqa: E501
        """
        pass

    def test_sms_email_sms_stripped_string_post(self):
        """Test case for sms_email_sms_stripped_string_post

        Create email to sms stripped string rule  # noqa: E501
        """
        pass

    def test_sms_email_sms_stripped_string_put(self):
        """Test case for sms_email_sms_stripped_string_put

        Update email to sms stripped string rule  # noqa: E501
        """
        pass

    def test_sms_email_sms_stripped_strings_get(self):
        """Test case for sms_email_sms_stripped_strings_get

        Get list of email to sms stripped string rules  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
