# clicksend_client.DeliveryIssuesApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delivery_issues_get**](DeliveryIssuesApi.md#delivery_issues_get) | **GET** /delivery-issues | Get all delivery issues
[**delivery_issues_post**](DeliveryIssuesApi.md#delivery_issues_post) | **POST** /delivery-issues | Create delivery Issue


# **delivery_issues_get**
> str delivery_issues_get(page=page, limit=limit)

Get all delivery issues

Get all delivery issues

### Example
```python
from __future__ import print_function
import time
import clicksend_client
from clicksend_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = clicksend_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = clicksend_client.DeliveryIssuesApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all delivery issues
    api_response = api_instance.delivery_issues_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryIssuesApi->delivery_issues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Number of records per page | [optional] [default to 10]

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delivery_issues_post**
> str delivery_issues_post(delivery_issue)

Create delivery Issue

Create delivery Issue

### Example
```python
from __future__ import print_function
import time
import clicksend_client
from clicksend_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = clicksend_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = clicksend_client.DeliveryIssuesApi(clicksend_client.ApiClient(configuration))
delivery_issue = clicksend_client.DeliveryIssue() # DeliveryIssue | DeliveryIssue model

try:
    # Create delivery Issue
    api_response = api_instance.delivery_issues_post(delivery_issue)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryIssuesApi->delivery_issues_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_issue** | [**DeliveryIssue**](DeliveryIssue.md)| DeliveryIssue model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

