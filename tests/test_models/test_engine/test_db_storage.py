#!/usr/bin/python3
import unittest
import models
import os
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', "if is db")
class test_DBStorage(unittest.TestCase):
    """ dbStorage test cases"""

    def setUp(self):
        """ Set up test environment """
        self.store = models.storage

    def tearDown(self):
        """ Remove storage file at end of tests """
        del self.store

    def test_place(self):
        """test"""
        place = Place(name='Park', number_rooms=3,
                      number_bathrooms=1, max_guest=6, price_by_night=120)
        place.save()
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.price_by_night, 120)
        self.assertTrue(place.id in self.store.all())

    def test_state(self):
        """test"""
        state = State(name='Lagos')
        state.save()
        self.assertEqual(state.name, 'Lagos')
        self.assertTrue(state.id in self.store.all())

    def test_city(self):
        """test"""
        city = City(name='SanDiego')
        new_state = State(name="CA")
        new_state.save()
        city.state_id = new_state.id
        city.save()
        self.assertEqual(city.state_id, new_state.id)
        self.assertEqual(city.name, 'SanDiego')
        self.assertTrue(city.id in self.store.all())

    def test_user(self):
        """test"""
        user = User(email="gui@hbtn.io", password="guipwd")
        user.save()
        self.assertTrue(user.id in self.store.all())
        self.assertEqual(user.email, 'gui@hbtn.io')

    def test_multiple(self):
        """test"""
        # show Place <new place ID>
        state = State(name="California")
        state.save()
        city = City(state_id=state.id, name="San_Francisco_is_super_cool")
        city.save()
        user = User(email="my@me.com", password="pwd",
                    first_name="FN", last_name="LN")
        user.save()
        place = Place(city_id=city.id, user_id=user.id, name="My_house",
                      description="no_description_yet",
                      number_rooms=4, number_bathrooms=1, max_guest=3,
                      price_by_night=100, latitude=120.12, longitude=101.4)
        place.save()
        self.assertEqual(city.state_id, state.id)
        self.assertEqual(city.name, 'San_Francisco_is_super_cool')
        self.assertTrue(city.id in self.store.all())
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.price_by_night, 100)
        self.assertTrue(place.id in self.store.all())
        self.assertTrue(user.id in self.store.all())
        self.assertEqual(user.email, 'my@me.com')
