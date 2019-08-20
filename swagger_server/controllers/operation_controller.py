import connexion
import six

from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.history import History  # noqa: E501
from swagger_server.models.balance import Balance  # noqa: E501
from swagger_server import util

from dboperations import dboperations 


def balance(body):  # noqa: E501
    """Retrieve the account balance

     # noqa: E501

    :param body: Balance object
    :type body: dict | bytes

    :rtype: None
    """
    balance=''
    if connexion.request.is_json:
        body = Balance.from_dict(connexion.request.get_json())  # noqa: E501
        balance = dboperations().balance(body.email)
    return { 
        "Account balance":balance
        }
    

def deposit(body):  # noqa: E501
    """Add funds to account

     # noqa: E501

    :param body: Order object
    :type body: dict | bytes

    :rtype: None
    """
    deposit=''
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
        deposit = dboperations().deposit(body.email,str(body.value))
    return { 
        "status":deposit
        }

def withdraw(body):  # noqa: E501
    """Remove funds from account

     # noqa: E501

    :param body: Order object
    :type body: dict | bytes

    :rtype: None
    """
    withdraw=''
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
        withdraw=dboperations().withdraw(body.email,str(body.value))
    return { 
        "ststus":withdraw
        }

def history(body):  # noqa: E501
    """Retrieve the account balance

     # noqa: E501

    :param body: History object
    :type body: dict | bytes

    :rtype: None
    """
    history=[]
    if connexion.request.is_json:
        body = History.from_dict(connexion.request.get_json())  # noqa: E501
        history=dboperations().get_history(body.email,body._from,body.to)
        print(history)
    return history