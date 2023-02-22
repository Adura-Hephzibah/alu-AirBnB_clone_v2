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
            self.console.onecmd('Create State')
            id = self.buffer.getvalue()
            self.assertFalse(len(id) == 43)
