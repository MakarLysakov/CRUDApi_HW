# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IllArrayIllIdBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ill_id: int=None, name: str=None, gender: str=None, status: str=None):  # noqa: E501
        """IllArrayIllIdBody - a model defined in Swagger

        :param ill_id: The ill_id of this IllArrayIllIdBody.  # noqa: E501
        :type ill_id: int
        :param name: The name of this IllArrayIllIdBody.  # noqa: E501
        :type name: str
        :param gender: The gender of this IllArrayIllIdBody.  # noqa: E501
        :type gender: str
        :param status: The status of this IllArrayIllIdBody.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'IllArrayIllIdBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ill_array_Ill_id_body of this IllArrayIllIdBody.  # noqa: E501
        :rtype: IllArrayIllIdBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ill_id(self) -> int:
        """Gets the ill_id of this IllArrayIllIdBody.


        :return: The ill_id of this IllArrayIllIdBody.
        :rtype: int
        """
        return self._ill_id

    @ill_id.setter
    def ill_id(self, ill_id: int):
        """Sets the ill_id of this IllArrayIllIdBody.


        :param ill_id: The ill_id of this IllArrayIllIdBody.
        :type ill_id: int
        """

        self._ill_id = ill_id

    @property
    def name(self) -> str:
        """Gets the name of this IllArrayIllIdBody.


        :return: The name of this IllArrayIllIdBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this IllArrayIllIdBody.


        :param name: The name of this IllArrayIllIdBody.
        :type name: str
        """

        self._name = name

    @property
    def gender(self) -> str:
        """Gets the gender of this IllArrayIllIdBody.


        :return: The gender of this IllArrayIllIdBody.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """Sets the gender of this IllArrayIllIdBody.


        :param gender: The gender of this IllArrayIllIdBody.
        :type gender: str
        """

        self._gender = gender

    @property
    def status(self) -> str:
        """Gets the status of this IllArrayIllIdBody.


        :return: The status of this IllArrayIllIdBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this IllArrayIllIdBody.


        :param status: The status of this IllArrayIllIdBody.
        :type status: str
        """

        self._status = status