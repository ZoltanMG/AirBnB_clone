#!/usr/bin/python3
"""
Review class inheriting from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that defines public class
    atributies with tree string empty
    """

    place_id = ""
    user_id = ""
    text = ""
