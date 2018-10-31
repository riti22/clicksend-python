# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.sms_delivery_receipt_rules_api import SMSDeliveryReceiptRulesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSMSDeliveryReceiptRulesApi(unittest.TestCase):
    """SMSDeliveryReceiptRulesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.sms_delivery_receipt_rules_api.SMSDeliveryReceiptRulesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sms_delivery_receipt_automation_delete(self):
        """Test case for sms_delivery_receipt_automation_delete

        Delete sms delivery receipt automation  # noqa: E501
        """
        pass

    def test_sms_delivery_receipt_automation_get(self):
        """Test case for sms_delivery_receipt_automation_get

        Get specific sms delivery receipt automation  # noqa: E501
        """
        pass

    def test_sms_delivery_receipt_automation_post(self):
        """Test case for sms_delivery_receipt_automation_post

        Create sms delivery receipt automations  # noqa: E501
        """
        pass

    def test_sms_delivery_receipt_automation_put(self):
        """Test case for sms_delivery_receipt_automation_put

        Update sms delivery receipt automation  # noqa: E501
        """
        pass

    def test_sms_delivery_receipt_automations_get(self):
        """Test case for sms_delivery_receipt_automations_get

        Get all sms delivery receipt automations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()