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


class PostPostcardApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_postcards_history_export_get(self, filename, **kwargs):  # noqa: E501
        """Export postcard history to a CSV file  # noqa: E501

        Export postcard history to a CSV file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_postcards_history_export_get(filename, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filename: Filename to export to (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_postcards_history_export_get_with_http_info(filename, **kwargs)  # noqa: E501
        else:
            (data) = self.post_postcards_history_export_get_with_http_info(filename, **kwargs)  # noqa: E501
            return data

    def post_postcards_history_export_get_with_http_info(self, filename, **kwargs):  # noqa: E501
        """Export postcard history to a CSV file  # noqa: E501

        Export postcard history to a CSV file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_postcards_history_export_get_with_http_info(filename, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filename: Filename to export to (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filename']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_postcards_history_export_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filename' is set
        if ('filename' not in params or
                params['filename'] is None):
            raise ValueError("Missing the required parameter `filename` when calling `post_postcards_history_export_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filename' in params:
            query_params.append(('filename', params['filename']))  # noqa: E501

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
            '/post/postcards/history/export', 'GET',
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

    def post_postcards_history_get(self, **kwargs):  # noqa: E501
        """Retrieve the history of postcards sent or scheduled  # noqa: E501

        Retrieve the history of postcards sent or scheduled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_postcards_history_get(async_req=True)
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
            return self.post_postcards_history_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_postcards_history_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_postcards_history_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve the history of postcards sent or scheduled  # noqa: E501

        Retrieve the history of postcards sent or scheduled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_postcards_history_get_with_http_info(async_req=True)
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
                    " to method post_postcards_history_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `post_postcards_history_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `post_postcards_history_get`, must be a value greater than or equal to `1`")  # noqa: E501
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
            '/post/postcards/history', 'GET',
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

    def post_postcards_price_post(self, post_postcards, **kwargs):  # noqa: E501
        """Calculate price for sending one or more postcards  # noqa: E501

        Calculate price for sending one or more postcards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_postcards_price_post(post_postcards, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostPostcard post_postcards: PostPostcard model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_postcards_price_post_with_http_info(post_postcards, **kwargs)  # noqa: E501
        else:
            (data) = self.post_postcards_price_post_with_http_info(post_postcards, **kwargs)  # noqa: E501
            return data

    def post_postcards_price_post_with_http_info(self, post_postcards, **kwargs):  # noqa: E501
        """Calculate price for sending one or more postcards  # noqa: E501

        Calculate price for sending one or more postcards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_postcards_price_post_with_http_info(post_postcards, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostPostcard post_postcards: PostPostcard model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_postcards']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_postcards_price_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_postcards' is set
        if ('post_postcards' not in params or
                params['post_postcards'] is None):
            raise ValueError("Missing the required parameter `post_postcards` when calling `post_postcards_price_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'post_postcards' in params:
            body_params = params['post_postcards']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/post/postcards/price', 'POST',
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

    def post_postcards_send_post(self, post_postcards, **kwargs):  # noqa: E501
        """Send one or more postcards  # noqa: E501

        Send one or more postcards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_postcards_send_post(post_postcards, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostPostcard post_postcards: PostPostcard model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_postcards_send_post_with_http_info(post_postcards, **kwargs)  # noqa: E501
        else:
            (data) = self.post_postcards_send_post_with_http_info(post_postcards, **kwargs)  # noqa: E501
            return data

    def post_postcards_send_post_with_http_info(self, post_postcards, **kwargs):  # noqa: E501
        """Send one or more postcards  # noqa: E501

        Send one or more postcards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_postcards_send_post_with_http_info(post_postcards, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostPostcard post_postcards: PostPostcard model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_postcards']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_postcards_send_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_postcards' is set
        if ('post_postcards' not in params or
                params['post_postcards'] is None):
            raise ValueError("Missing the required parameter `post_postcards` when calling `post_postcards_send_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'post_postcards' in params:
            body_params = params['post_postcards']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/post/postcards/send', 'POST',
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
