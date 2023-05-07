# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from borValBadgeDbServer.models.base_model_ import Model
from borValBadgeDbServer import util


class BadgeInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, badge_id=None, found=None, created=None, awarding_universe=None, value=None):  # noqa: E501
        """BadgeInfo - a model defined in OpenAPI

        :param badge_id: The badge_id of this BadgeInfo.  # noqa: E501
        :type badge_id: int
        :param found: The found of this BadgeInfo.  # noqa: E501
        :type found: bool
        :param created: The created of this BadgeInfo.  # noqa: E501
        :type created: int
        :param awarding_universe: The awarding_universe of this BadgeInfo.  # noqa: E501
        :type awarding_universe: int
        :param value: The value of this BadgeInfo.  # noqa: E501
        :type value: str
        """
        self.openapi_types = {
            'badge_id': int,
            'found': bool,
            'created': int,
            'awarding_universe': int,
            'value': str
        }

        self.attribute_map = {
            'badge_id': 'badge_id',
            'found': 'found',
            'created': 'created',
            'awarding_universe': 'awarding_universe',
            'value': 'value'
        }

        self._badge_id = badge_id
        self._found = found
        self._created = created
        self._awarding_universe = awarding_universe
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'BadgeInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BadgeInfo of this BadgeInfo.  # noqa: E501
        :rtype: BadgeInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def badge_id(self):
        """Gets the badge_id of this BadgeInfo.


        :return: The badge_id of this BadgeInfo.
        :rtype: int
        """
        return self._badge_id

    @badge_id.setter
    def badge_id(self, badge_id):
        """Sets the badge_id of this BadgeInfo.


        :param badge_id: The badge_id of this BadgeInfo.
        :type badge_id: int
        """

        self._badge_id = badge_id

    @property
    def found(self):
        """Gets the found of this BadgeInfo.


        :return: The found of this BadgeInfo.
        :rtype: bool
        """
        return self._found

    @found.setter
    def found(self, found):
        """Sets the found of this BadgeInfo.


        :param found: The found of this BadgeInfo.
        :type found: bool
        """

        self._found = found

    @property
    def created(self):
        """Gets the created of this BadgeInfo.


        :return: The created of this BadgeInfo.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this BadgeInfo.


        :param created: The created of this BadgeInfo.
        :type created: int
        """

        self._created = created

    @property
    def awarding_universe(self):
        """Gets the awarding_universe of this BadgeInfo.


        :return: The awarding_universe of this BadgeInfo.
        :rtype: int
        """
        return self._awarding_universe

    @awarding_universe.setter
    def awarding_universe(self, awarding_universe):
        """Sets the awarding_universe of this BadgeInfo.


        :param awarding_universe: The awarding_universe of this BadgeInfo.
        :type awarding_universe: int
        """

        self._awarding_universe = awarding_universe

    @property
    def value(self):
        """Gets the value of this BadgeInfo.


        :return: The value of this BadgeInfo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BadgeInfo.


        :param value: The value of this BadgeInfo.
        :type value: str
        """
        allowed_values = ["Free", "Valuable", "Legacy"]  # noqa: E501
        if value not in allowed_values:
            raise ValueError(
                "Invalid value for `value` ({0}), must be one of {1}"
                .format(value, allowed_values)
            )

        self._value = value
