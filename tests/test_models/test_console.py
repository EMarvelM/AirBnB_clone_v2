#!/usr/bin/python3
""" """
from unittest.mock import patch
import sys
from io import StringIO
from tests.test_models.test_base_model import test_basemodel
from console import HBNBCommand

class test_console(test_basemodel):
    """ Tests for the HBNBCommand class """
    def setUp(self):
        """Set up resources before each test method"""
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF_command(self, mock_stdout):
        with patch('builtins.input', side_effect=KeyboardInterrupt):
            self.console.cmdloop()
        self.assertEqual(mock_stdout.getvalue(), '\n')
