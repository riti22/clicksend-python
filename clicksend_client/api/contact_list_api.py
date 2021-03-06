# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from clicksend_client.api_client import ApiClient


class ContactListApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def lists_by_list_id_delete(self, list_id, **kwargs):  # noqa: E501
        """ListsByListIdDelete  # noqa: E501

        Delete a specific contact list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_by_list_id_delete(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: List ID (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_by_list_id_delete_with_http_info(list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_by_list_id_delete_with_http_info(list_id, **kwargs)  # noqa: E501
            return data

    def lists_by_list_id_delete_with_http_info(self, list_id, **kwargs):  # noqa: E501
        """ListsByListIdDelete  # noqa: E501

        Delete a specific contact list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_by_list_id_delete_with_http_info(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: List ID (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_by_list_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `lists_by_list_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_by_list_id_get(self, list_id, **kwargs):  # noqa: E501
        """Get specific contact list  # noqa: E501

        Get specific contact list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_by_list_id_get(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: List ID (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_by_list_id_get_with_http_info(list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_by_list_id_get_with_http_info(list_id, **kwargs)  # noqa: E501
            return data

    def lists_by_list_id_get_with_http_info(self, list_id, **kwargs):  # noqa: E501
        """Get specific contact list  # noqa: E501

        Get specific contact list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_by_list_id_get_with_http_info(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: List ID (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_by_list_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `lists_by_list_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_by_list_id_put(self, list_id, list_name, **kwargs):  # noqa: E501
        """Update specific contact list  # noqa: E501

        Update specific contact list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_by_list_id_put(list_id, list_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Your list id (required)
        :param str list_name: Your new list name (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_by_list_id_put_with_http_info(list_id, list_name, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_by_list_id_put_with_http_info(list_id, list_name, **kwargs)  # noqa: E501
            return data

    def lists_by_list_id_put_with_http_info(self, list_id, list_name, **kwargs):  # noqa: E501
        """Update specific contact list  # noqa: E501

        Update specific contact list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_by_list_id_put_with_http_info(list_id, list_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Your list id (required)
        :param str list_name: Your new list name (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'list_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_by_list_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `lists_by_list_id_put`")  # noqa: E501
        # verify the required parameter 'list_name' is set
        if ('list_name' not in params or
                params['list_name'] is None):
            raise ValueError("Missing the required parameter `list_name` when calling `lists_by_list_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'list_name' in params:
            body_params = params['list_name']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_get(self, **kwargs):  # noqa: E501
        """Get all contact lists  # noqa: E501

        Get all contact lists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.lists_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def lists_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all contact lists  # noqa: E501

        Get all contact lists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `lists_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `lists_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_import_by_list_id_post(self, list_id, file, **kwargs):  # noqa: E501
        """Import contacts to list  # noqa: E501

        Import contacts to list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_import_by_list_id_post(list_id, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Your contact list id you want to access. (required)
        :param ContactListImport file: ContactListImport model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_import_by_list_id_post_with_http_info(list_id, file, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_import_by_list_id_post_with_http_info(list_id, file, **kwargs)  # noqa: E501
            return data

    def lists_import_by_list_id_post_with_http_info(self, list_id, file, **kwargs):  # noqa: E501
        """Import contacts to list  # noqa: E501

        Import contacts to list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_import_by_list_id_post_with_http_info(list_id, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Your contact list id you want to access. (required)
        :param ContactListImport file: ContactListImport model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_import_by_list_id_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `lists_import_by_list_id_post`")  # noqa: E501
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `lists_import_by_list_id_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'file' in params:
            body_params = params['file']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_post(self, list_name, **kwargs):  # noqa: E501
        """Create new contact list  # noqa: E501

        Create new contact list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_post(list_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str list_name: Your contact list name (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_post_with_http_info(list_name, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_post_with_http_info(list_name, **kwargs)  # noqa: E501
            return data

    def lists_post_with_http_info(self, list_name, **kwargs):  # noqa: E501
        """Create new contact list  # noqa: E501

        Create new contact list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_post_with_http_info(list_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str list_name: Your contact list name (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_name' is set
        if ('list_name' not in params or
                params['list_name'] is None):
            raise ValueError("Missing the required parameter `list_name` when calling `lists_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'list_name' in params:
            body_params = params['list_name']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_remove_duplicates_by_list_id_put(self, list_id, fields, **kwargs):  # noqa: E501
        """Remove duplicate contacts  # noqa: E501

        Remove duplicate contacts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_remove_duplicates_by_list_id_put(list_id, fields, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Your list id (required)
        :param Fields fields: Fields model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_remove_duplicates_by_list_id_put_with_http_info(list_id, fields, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_remove_duplicates_by_list_id_put_with_http_info(list_id, fields, **kwargs)  # noqa: E501
            return data

    def lists_remove_duplicates_by_list_id_put_with_http_info(self, list_id, fields, **kwargs):  # noqa: E501
        """Remove duplicate contacts  # noqa: E501

        Remove duplicate contacts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_remove_duplicates_by_list_id_put_with_http_info(list_id, fields, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Your list id (required)
        :param Fields fields: Fields model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_remove_duplicates_by_list_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `lists_remove_duplicates_by_list_id_put`")  # noqa: E501
        # verify the required parameter 'fields' is set
        if ('fields' not in params or
                params['fields'] is None):
            raise ValueError("Missing the required parameter `fields` when calling `lists_remove_duplicates_by_list_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'fields' in params:
            body_params = params['fields']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/remove-duplicates', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
