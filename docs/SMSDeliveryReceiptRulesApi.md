# clicksend_client.SMSDeliveryReceiptRulesApi

All URIs are relative to *https://rest.clicksend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sms_delivery_receipt_automation_delete**](SMSDeliveryReceiptRulesApi.md#sms_delivery_receipt_automation_delete) | **DELETE** /automations/sms/receipts/{receipt_rule_id} | Delete sms delivery receipt automation
[**sms_delivery_receipt_automation_get**](SMSDeliveryReceiptRulesApi.md#sms_delivery_receipt_automation_get) | **GET** /automations/sms/receipts/{receipt_rule_id} | Get specific sms delivery receipt automation
[**sms_delivery_receipt_automation_post**](SMSDeliveryReceiptRulesApi.md#sms_delivery_receipt_automation_post) | **POST** /automations/sms/receipts | Create sms delivery receipt automations
[**sms_delivery_receipt_automation_put**](SMSDeliveryReceiptRulesApi.md#sms_delivery_receipt_automation_put) | **PUT** /automations/sms/receipts/{receipt_rule_id} | Update sms delivery receipt automation
[**sms_delivery_receipt_automations_get**](SMSDeliveryReceiptRulesApi.md#sms_delivery_receipt_automations_get) | **GET** /automations/sms/receipts | Get all sms delivery receipt automations


# **sms_delivery_receipt_automation_delete**
> str sms_delivery_receipt_automation_delete(receipt_rule_id)

Delete sms delivery receipt automation

Delete sms delivery receipt automation

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
api_instance = clicksend_client.SMSDeliveryReceiptRulesApi(clicksend_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id

try:
    # Delete sms delivery receipt automation
    api_response = api_instance.sms_delivery_receipt_automation_delete(receipt_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSDeliveryReceiptRulesApi->sms_delivery_receipt_automation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_rule_id** | **int**| Receipt rule id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_delivery_receipt_automation_get**
> str sms_delivery_receipt_automation_get(receipt_rule_id)

Get specific sms delivery receipt automation

Get specific sms delivery receipt automation

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
api_instance = clicksend_client.SMSDeliveryReceiptRulesApi(clicksend_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id

try:
    # Get specific sms delivery receipt automation
    api_response = api_instance.sms_delivery_receipt_automation_get(receipt_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSDeliveryReceiptRulesApi->sms_delivery_receipt_automation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_rule_id** | **int**| Receipt rule id | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_delivery_receipt_automation_post**
> str sms_delivery_receipt_automation_post(delivery_receipt_rule)

Create sms delivery receipt automations

Create sms delivery receipt automations

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
api_instance = clicksend_client.SMSDeliveryReceiptRulesApi(clicksend_client.ApiClient(configuration))
delivery_receipt_rule = clicksend_client.DeliveryReceiptRule() # DeliveryReceiptRule | sms delivery receipt rule model

try:
    # Create sms delivery receipt automations
    api_response = api_instance.sms_delivery_receipt_automation_post(delivery_receipt_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSDeliveryReceiptRulesApi->sms_delivery_receipt_automation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_receipt_rule** | [**DeliveryReceiptRule**](DeliveryReceiptRule.md)| sms delivery receipt rule model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_delivery_receipt_automation_put**
> str sms_delivery_receipt_automation_put(receipt_rule_id, delivery_receipt_rule)

Update sms delivery receipt automation

Update sms delivery receipt automation

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
api_instance = clicksend_client.SMSDeliveryReceiptRulesApi(clicksend_client.ApiClient(configuration))
receipt_rule_id = 56 # int | Receipt rule id
delivery_receipt_rule = clicksend_client.DeliveryReceiptRule() # DeliveryReceiptRule | Delivery receipt rule model

try:
    # Update sms delivery receipt automation
    api_response = api_instance.sms_delivery_receipt_automation_put(receipt_rule_id, delivery_receipt_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSDeliveryReceiptRulesApi->sms_delivery_receipt_automation_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_rule_id** | **int**| Receipt rule id | 
 **delivery_receipt_rule** | [**DeliveryReceiptRule**](DeliveryReceiptRule.md)| Delivery receipt rule model | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_delivery_receipt_automations_get**
> str sms_delivery_receipt_automations_get(page=page, limit=limit)

Get all sms delivery receipt automations

Get all sms delivery receipt automations

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
api_instance = clicksend_client.SMSDeliveryReceiptRulesApi(clicksend_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Number of records per page (optional) (default to 10)

try:
    # Get all sms delivery receipt automations
    api_response = api_instance.sms_delivery_receipt_automations_get(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSDeliveryReceiptRulesApi->sms_delivery_receipt_automations_get: %s\n" % e)
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

