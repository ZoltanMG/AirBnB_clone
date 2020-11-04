#!/usr/bin/python3
"""
User inheriting from BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that define atributes puiblic
    with string empty
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
