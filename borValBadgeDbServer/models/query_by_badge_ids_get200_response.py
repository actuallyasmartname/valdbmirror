# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from borValBadgeDbServer.models.base_model_ import Model
from borValBadgeDbServer.models.badge_info import BadgeInfo
from borValBadgeDbServer import util


class QueryByBadgeIdsGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None):  # noqa: E501
        """QueryByBadgeIdsGet200Response - a model defined in OpenAPI

        :param data: The data of this QueryByBadgeIdsGet200Response.  # noqa: E501
        :type data: List[BadgeInfo]
        """
        self.openapi_types = {
            'data': List[BadgeInfo]
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'QueryByBadgeIdsGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _query_byBadgeIds_get_200_response of this QueryByBadgeIdsGet200Response.  # noqa: E501
        :rtype: QueryByBadgeIdsGet200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this QueryByBadgeIdsGet200Response.


        :return: The data of this QueryByBadgeIdsGet200Response.
        :rtype: List[BadgeInfo]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this QueryByBadgeIdsGet200Response.


        :param data: The data of this QueryByBadgeIdsGet200Response.
        :type data: List[BadgeInfo]
        """

        self._data = data
