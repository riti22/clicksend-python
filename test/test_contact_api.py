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
from clicksend_client.api.contact_api import ContactApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestContactApi(unittest.TestCase):
    """ContactApi unit test stubs"""

    def setUp(self):
        self.api = clicksend_client.api.contact_api.ContactApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_lists_contacts_by_list_id_and_contact_id_delete(self):
        """Test case for lists_contacts_by_list_id_and_contact_id_delete

        Delete a contact  # noqa: E501
        """
        pass

    def test_lists_contacts_by_list_id_and_contact_id_get(self):
        """Test case for lists_contacts_by_list_id_and_contact_id_get

        Get a specific contact  # noqa: E501
        """
        pass

    def test_lists_contacts_by_list_id_and_contact_id_put(self):
        """Test case for lists_contacts_by_list_id_and_contact_id_put

        Update specific contact  # noqa: E501
        """
        pass

    def test_lists_contacts_by_list_id_get(self):
        """Test case for lists_contacts_by_list_id_get

        Get all contacts in a list  # noqa: E501
        """
        pass

    def test_lists_contacts_by_list_id_post(self):
        """Test case for lists_contacts_by_list_id_post

        Create new contact  # noqa: E501
        """
        pass

    def test_lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put(self):
        """Test case for lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put

        Remove all opted out contacts  # noqa: E501
        """
        pass

    def test_lists_transfer_contact_put(self):
        """Test case for lists_transfer_contact_put

        Transfer contact to another list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
