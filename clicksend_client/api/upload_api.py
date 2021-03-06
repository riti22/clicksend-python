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


class UploadApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def uploads_post(self, convert, **kwargs):  # noqa: E501
        """Upload File  # noqa: E501

        Upload File  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.uploads_post(convert, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str convert:  (required)
        :param UploadFile upload_file:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.uploads_post_with_http_info(convert, **kwargs)  # noqa: E501
        else:
            (data) = self.uploads_post_with_http_info(convert, **kwargs)  # noqa: E501
            return data

    def uploads_post_with_http_info(self, convert, **kwargs):  # noqa: E501
        """Upload File  # noqa: E501

        Upload File  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.uploads_post_with_http_info(convert, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str convert:  (required)
        :param UploadFile upload_file:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['convert', 'upload_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method uploads_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'convert' is set
        if ('convert' not in params or
                params['convert'] is None):
            raise ValueError("Missing the required parameter `convert` when calling `uploads_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'convert' in params:
            query_params.append(('convert', params['convert']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'upload_file' in params:
            body_params = params['upload_file']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/uploads', 'POST',
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
