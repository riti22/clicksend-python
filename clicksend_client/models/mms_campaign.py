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


class MmsCampaign(object):
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
        'list_id': 'int',
        'name': 'str',
        'body': 'str',
        '_from': 'str',
        'schedule': 'int',
        'subject': 'str',
        'media_file': 'str'
    }

    attribute_map = {
        'list_id': 'list_id',
        'name': 'name',
        'body': 'body',
        '_from': 'from',
        'schedule': 'schedule',
        'subject': 'subject',
        'media_file': 'media_file'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, list_id=None, name=None, body=None, _from=None, schedule=0, subject=None, media_file=None):  # noqa: E501
        """MmsCampaign - a model defined in Swagger"""  # noqa: E501

        self._list_id = None
        self._name = None
        self._body = None
        self.__from = None
        self._schedule = None
        self._subject = None
        self._media_file = None
        self.discriminator = 'classType'

        self.list_id = list_id
        self.name = name
        self.body = body
        if _from is not None:
            self._from = _from
        if schedule is not None:
            self.schedule = schedule
        self.subject = subject
        self.media_file = media_file

    @property
    def list_id(self):
        """Gets the list_id of this MmsCampaign.  # noqa: E501

        Your list id.  # noqa: E501

        :return: The list_id of this MmsCampaign.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this MmsCampaign.

        Your list id.  # noqa: E501

        :param list_id: The list_id of this MmsCampaign.  # noqa: E501
        :type: int
        """
        if list_id is None:
            raise ValueError("Invalid value for `list_id`, must not be `None`")  # noqa: E501

        self._list_id = list_id

    @property
    def name(self):
        """Gets the name of this MmsCampaign.  # noqa: E501

        Your campaign name.  # noqa: E501

        :return: The name of this MmsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MmsCampaign.

        Your campaign name.  # noqa: E501

        :param name: The name of this MmsCampaign.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def body(self):
        """Gets the body of this MmsCampaign.  # noqa: E501

        Your campaign message.  # noqa: E501

        :return: The body of this MmsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this MmsCampaign.

        Your campaign message.  # noqa: E501

        :param body: The body of this MmsCampaign.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def _from(self):
        """Gets the _from of this MmsCampaign.  # noqa: E501

        Your sender id - more info: http://help.clicksend.com/SMS/what-is-a-sender-id-or-sender-number.  # noqa: E501

        :return: The _from of this MmsCampaign.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this MmsCampaign.

        Your sender id - more info: http://help.clicksend.com/SMS/what-is-a-sender-id-or-sender-number.  # noqa: E501

        :param _from: The _from of this MmsCampaign.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def schedule(self):
        """Gets the schedule of this MmsCampaign.  # noqa: E501

        Your schedule timestamp.  # noqa: E501

        :return: The schedule of this MmsCampaign.  # noqa: E501
        :rtype: int
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this MmsCampaign.

        Your schedule timestamp.  # noqa: E501

        :param schedule: The schedule of this MmsCampaign.  # noqa: E501
        :type: int
        """

        self._schedule = schedule

    @property
    def subject(self):
        """Gets the subject of this MmsCampaign.  # noqa: E501

        Subject of MMS campaign.  # noqa: E501

        :return: The subject of this MmsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this MmsCampaign.

        Subject of MMS campaign.  # noqa: E501

        :param subject: The subject of this MmsCampaign.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def media_file(self):
        """Gets the media_file of this MmsCampaign.  # noqa: E501

        URL pointing to media file.  # noqa: E501

        :return: The media_file of this MmsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._media_file

    @media_file.setter
    def media_file(self, media_file):
        """Sets the media_file of this MmsCampaign.

        URL pointing to media file.  # noqa: E501

        :param media_file: The media_file of this MmsCampaign.  # noqa: E501
        :type: str
        """
        if media_file is None:
            raise ValueError("Invalid value for `media_file`, must not be `None`")  # noqa: E501

        self._media_file = media_file

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
        if issubclass(MmsCampaign, dict):
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
        if not isinstance(other, MmsCampaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
