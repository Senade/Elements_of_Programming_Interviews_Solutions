#!/usr/bin/env python3
import unittest
from eopi_solutions import strings

class TestStrings(unittest.TestCase):
    def test_int_to_str(self) -> None:
        self.assertEqual(strings.int_to_str(123), "123")
        self.assertEqual(strings.int_to_str(0), "0")
        self.assertEqual(strings.int_to_str(-123), "-123")
    
    def test_str_to_int(self) -> None:
        self.assertEqual(strings.str_to_int("123"), 123)
        self.assertEqual(strings.str_to_int("0"), 0)
        self.assertEqual(strings.str_to_int("-123"), -123)