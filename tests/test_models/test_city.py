#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        my_state = State()
        new = self.value()
        new.state_id = my_state.id
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        new.name = 'Kigali'
        self.assertEqual(type(new.name), str)
