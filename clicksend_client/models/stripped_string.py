# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StrippedString(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      clicksend_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    clicksend_types = {
        'strip_string': 'str'
    }

    attribute_map = {
        'strip_string': 'strip-string'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, strip_string=None):  # noqa: E501
        """StrippedString - a model defined in Swagger"""  # noqa: E501

        self._strip_string = None
        self.discriminator = 'classType'

        self.strip_string = strip_string

    @property
    def strip_string(self):
        """Gets the strip_string of this StrippedString.  # noqa: E501

        String to be.  # noqa: E501

        :return: The strip_string of this StrippedString.  # noqa: E501
        :rtype: str
        """
        return self._strip_string

    @strip_string.setter
    def strip_string(self, strip_string):
        """Sets the strip_string of this StrippedString.

        String to be.  # noqa: E501

        :param strip_string: The strip_string of this StrippedString.  # noqa: E501
        :type: str
        """
        if strip_string is None:
            raise ValueError("Invalid value for `strip_string`, must not be `None`")  # noqa: E501

        self._strip_string = strip_string

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.clicksend_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StrippedString, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StrippedString):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other