#!/usr/bin/python3
""" Defines a user class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines a class user that inherits from BaseModel"""
    email = ""
    first_name = ""
    last_name = ""
    password = ""
