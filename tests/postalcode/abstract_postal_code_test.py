#!/usr/bin/env python3

'''
Unit test for AbstractPostalCode class
'''

import unittest
from src.postalcode.abstract_postal_code import AbstractPostalCode

class AbstractPostalCodeTest(unittest.TestCase):
  '''
  Test suite for abstract postal code class
  '''

  def test_cannot_instanciate(self):
    '''
    Validation that abstract class cannot be instanciate
    '''
    with self.assertRaises(Exception) as context:
        AbstractPostalCode('')

    self.assertEqual(
        "Can't instantiate abstract class AbstractPostalCode with abstract methods __init__, is_valid",
        str(context.exception)
    )
