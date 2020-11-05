#!/usr/bin/python3
"""
City class inheriting from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that define public class atribute
    with two string empty
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
