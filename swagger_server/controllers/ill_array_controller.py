import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.ill_array import IllArray  # noqa: E501
from swagger_server.models.ill_array_ill_id_body import IllArrayIllIdBody  # noqa: E501
from swagger_server.models.ill_obj import IllObj  # noqa: E501
from swagger_server import util
from flask import abort, make_response

storage = []

def change_ill_by_id(ill_id, body=None):  # noqa: E501
    """Метод изменения информации о больном по идентификатору

     # noqa: E501

    :param ill_id: Идентификатор больного
    :type ill_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: IllObj
    """
    if connexion.request.is_json:
        body = IllArrayIllIdBody.from_dict(connexion.request.get_json())  # noqa: E501
        for i in storage:
            if i.ill_id == ill_id:
                if body.name != '':
                    i.name = body.name
                if body.gender == 'мужчина' or body.gender == 'женщина':
                    i.gender = body.gender
                elif body.gender == '':
                    pass
                else:
                    return 'введите "мужчина" или "женщина"'
                if body.status == 'на личении' or body.status == 'выписан':
                    i.status = body.status
                elif body.status == '':
                    pass
                else:
                    return 'введите "на личении" или "выписан"'
    return make_response('', 200)


def create_ill(body):  # noqa: E501
    """Метод внесения информации о пациенте

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: IllObj
    """
    if connexion.request.is_json:
        body = IllObj.from_dict(connexion.request.get_json())  # noqa: E501
        id_app = body.ill_id
        for i in storage:
            if i.ill_id == id_app:
                abort(400)

    storage.append(body)
    return make_response('', 200)


def delete_toy_by_id(ill_id):  # noqa: E501
    """Метод удаления пациента по индентификатору

     # noqa: E501

    :param ill_id: Идентификатор больного
    :type ill_id: int

    :rtype: None
    """
    for i in storage:
        if i.ill_id == ill_id:
            storage.remove(i)
            return make_response('', 200)

    return abort(404)


def get_allill():  # noqa: E501
    """Выдает список пациентов

     # noqa: E501


    :rtype: IllArray
    """
    return make_response(storage, 200)


def get_ill_by_id(ill_id):  # noqa: E501
    """Метод получения больного по идентификатору

     # noqa: E501

    :param ill_id: Идентификатор больного
    :type ill_id: int

    :rtype: IllObj
    """
    for i in storage:
        if i.ill_id == ill_id:
            return i

    return abort(404)
