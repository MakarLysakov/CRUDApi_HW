# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IllObj(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ill_id: int=None, name: str=None, gender: str=None, status: str=None):  # noqa: E501
        """IllObj - a model defined in Swagger

        :param ill_id: The ill_id of this IllObj.  # noqa: E501
        :type ill_id: int
        :param name: The name of this IllObj.  # noqa: E501
        :type name: str
        :param gender: The gender of this IllObj.  # noqa: E501
        :type gender: str
        :param status: The status of this IllObj.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'ill_id': int,
            'name': str,
            'gender': str,
            'status': str
        }

        self.attribute_map = {
            'ill_id': 'Ill_id',
            'name': 'name',
            'gender': 'gender',
            'status': 'status'
        }
        self._ill_id = ill_id
        self._name = name
        self._gender = gender
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'IllObj':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ill_obj of this IllObj.  # noqa: E501
        :rtype: IllObj
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ill_id(self) -> int:
        """Gets the ill_id of this IllObj.


        :return: The ill_id of this IllObj.
        :rtype: int
        """
        return self._ill_id

    @ill_id.setter
    def ill_id(self, ill_id: int):
        """Sets the ill_id of this IllObj.


        :param ill_id: The ill_id of this IllObj.
        :type ill_id: int
        """

        self._ill_id = ill_id

    @property
    def name(self) -> str:
        """Gets the name of this IllObj.


        :return: The name of this IllObj.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this IllObj.


        :param name: The name of this IllObj.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def gender(self) -> str:
        """Gets the gender of this IllObj.


        :return: The gender of this IllObj.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """Sets the gender of this IllObj.


        :param gender: The gender of this IllObj.
        :type gender: str
        """
        allowed_values = ["мужчина", "женщина"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def status(self) -> str:
        """Gets the status of this IllObj.


        :return: The status of this IllObj.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this IllObj.


        :param status: The status of this IllObj.
        :type status: str
        """
        allowed_values = ["на личении", "выписан"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status