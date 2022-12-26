# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.ill_array import IllArray  # noqa: E501
from swagger_server.models.ill_array_ill_id_body import IllArrayIllIdBody  # noqa: E501
from swagger_server.models.ill_obj import IllObj  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIllArrayController(BaseTestCase):
    """IllArrayController integration test stubs"""

    def test_change_ill_by_id(self):
        """Test case for change_ill_by_id

        Метод изменения информации о больном по идентификатору
        """
        body = IllArrayIllIdBody()
        response = self.client.open(
            '/MakarLysakov/Hosp/1.0.0/Ill_array/{Ill_id}'.format(ill_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_ill(self):
        """Test case for create_ill

        Метод внесения информации о пациенте
        """
        body = IllObj()
        response = self.client.open(
            '/MakarLysakov/Hosp/1.0.0/ill',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_toy_by_id(self):
        """Test case for delete_toy_by_id

        Метод удаления пациента по индентификатору
        """
        response = self.client.open(
            '/MakarLysakov/Hosp/1.0.0/Ill_array/{Ill_id}'.format(ill_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_allill(self):
        """Test case for get_allill

        Выдает список пациентов
        """
        response = self.client.open(
            '/MakarLysakov/Hosp/1.0.0/ill',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ill_by_id(self):
        """Test case for get_ill_by_id

        Метод получения больного по идентификатору
        """
        response = self.client.open(
            '/MakarLysakov/Hosp/1.0.0/Ill_array/{Ill_id}'.format(ill_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
