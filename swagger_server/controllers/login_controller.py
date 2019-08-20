import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

from dboperations import dboperations 

def login_user(body):  # noqa: E501
    """Login the user

    Retrieve the api key. # noqa: E501

    :param body: User object
    :type body: dict | bytes

    :rtype: None
    """
    login=''
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        login = dboperations().login(body)
    return { 
        "apiKey":login, 
        "user":body.email
        }

def register_account(body):  # noqa: E501
    """Register a new account

     # noqa: E501

    :param body: User information
    :type body: dict | bytes

    :rtype: None
    """
    login=''
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        login = dboperations().register_user(body)
        if  (login[0]=='ok'):
            return { "apiKey":login[1], 
                    "user":body.email }
        return {'error':'user already registered'}