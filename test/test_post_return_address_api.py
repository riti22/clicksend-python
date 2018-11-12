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
from clicksend_client.api.post_return_address_api import PostReturnAddressApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestPostReturnAddressApi(unittest.TestCase):
    """PostReturnAddressApi unit test stubs"""

    def setUp(self):
        self.api = clicksend_client.api.post_return_address_api.PostReturnAddressApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_return_addresses_by_return_address_id_delete(self):
        """Test case for post_return_addresses_by_return_address_id_delete

        Delete specific post return address  # noqa: E501
        """
        pass

    def test_post_return_addresses_by_return_address_id_get(self):
        """Test case for post_return_addresses_by_return_address_id_get

        Get specific post return address  # noqa: E501
        """
        pass

    def test_post_return_addresses_by_return_address_id_put(self):
        """Test case for post_return_addresses_by_return_address_id_put

        Update post return address  # noqa: E501
        """
        pass

    def test_post_return_addresses_get(self):
        """Test case for post_return_addresses_get

        Get list of post return addresses  # noqa: E501
        """
        pass

    def test_post_return_addresses_post(self):
        """Test case for post_return_addresses_post

        Create post return address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
