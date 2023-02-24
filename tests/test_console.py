#!/usr/bin/python3
"""Test"""
import unittest
from unittest.mock import patch
from io import StringIO
import models
from console import HBNBCommand


class test_console(unittest.TestCase):
    ''' Test the console module'''

    def setUp(self):
        '''setup for'''
        self.store = models.storage
        self.buffer = StringIO()
        self.console = HBNBCommand()

    def tearDown(self):
        ''''''
        del self.buffer
        del self.store

    def test_all(self):
        """test all"""
        with patch('sys.stdout', self.buffer):
            self.console.onecmd('all Ade')
            self.assertEqual("** class doesn't exist **\n",
                             self.buffer.getvalue())
        # with patch('sys.stdout', self.buffer):
        #     self.console.onecmd("all State")
        #     self.assertEqual("[]\n", self.buffer.getvalue())

    def test_create(self):
        """test create"""
        with patch('sys.stdout', self.buffer):
            self.console.onecmd('create State name="Abia"')
            id = self.buffer.getvalue()
            self.assertFalse(len(id) == 43)

    def test_create_many(self):
        """test create"""
        with patch('sys.stdout', self.buffer):
            self.console.onecmd('create State name="California"')
            state_id = self.buffer.getvalue()[:-1]
        with patch('sys.stdout', self.buffer):
            self.console.onecmd(
                'create City state_id={} name="San_Francisco"'.format(
                    state_id))
            city_id = self.buffer.getvalue()[:-1]
        with patch('sys.stdout', self.buffer):
            self.console.onecmd(
                'create User email="my@me.com" password="pwd" first_name="FN"')
            user_id = self.buffer.getvalue()[:-1]
            # self.console.onecmd(
            #     'create Place city_id={} user_id={} name="My_house"\
            #         description="no_description_yet" number_rooms=4\
            #         number_bathrooms=1 max_guest=3 price_by_night=100\
            #             latitude=120.12 longitude=101.4'.format(
            #         city_id, user_id))
            self.assertTrue(len(state_id) == 36)
