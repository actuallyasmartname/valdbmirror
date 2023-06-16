# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from borValBadgeDbServer.models.base_model_ import Model
from borValBadgeDbServer import util


class UserRequestCheckGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, last_checked=None, check_in_progress=None):  # noqa: E501
        """UserRequestCheckGet200Response - a model defined in OpenAPI

        :param last_checked: The last_checked of this UserRequestCheckGet200Response.  # noqa: E501
        :type last_checked: int
        :param check_in_progress: The check_in_progress of this UserRequestCheckGet200Response.  # noqa: E501
        :type check_in_progress: bool
        """
        self.openapi_types = {
            'last_checked': int,
            'check_in_progress': bool
        }

        self._last_checked = last_checked
        self._check_in_progress = check_in_progress

    @classmethod
    def from_dict(cls, dikt) -> 'UserRequestCheckGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _user_requestcheck_get_200_response of this UserRequestCheckGet200Response.  # noqa: E501
        :rtype: UserRequestCheckGet200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def last_checked(self):
        """Gets the last_checked of this UserRequestCheckGet200Response.


        :return: The last_checked of this UserRequestCheckGet200Response.
        :rtype: int
        """
        return self._last_checked

    @last_checked.setter
    def last_checked(self, last_checked):
        """Sets the last_checked of this UserRequestCheckGet200Response.


        :param last_checked: The last_checked of this UserRequestCheckGet200Response.
        :type last_checked: int
        """

        self._last_checked = last_checked

    @property
    def check_in_progress(self):
        """Gets the check_in_progress of this UserRequestCheckGet200Response.


        :return: The check_in_progress of this UserRequestCheckGet200Response.
        :rtype: bool
        """
        return self._check_in_progress

    @check_in_progress.setter
    def check_in_progress(self, check_in_progress):
        """Sets the check_in_progress of this UserRequestCheckGet200Response.


        :param check_in_progress: The check_in_progress of this UserRequestCheckGet200Response.
        :type check_in_progress: bool
        """

        self._check_in_progress = check_in_progress
