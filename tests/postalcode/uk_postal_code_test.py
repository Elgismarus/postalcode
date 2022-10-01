#!/usr/bin/env python3

'''
Unit test for UKPostalCode class
'''

import unittest
import src
import os

from src.postalcode.uk_postal_code import UKPostalCode
from src.postalcode.abstract_postal_code import AbstractPostalCode

class UKPostalCodeTest(unittest.TestCase):
  '''
  Test UK postal code class
  '''

  def test_instanciate(self):
    '''
    Test can instanciate
    '''
    self.assertIsInstance(UKPostalCode(''), AbstractPostalCode)

  def test_is_valid(self):
    '''
    Test logic is_valid
    '''
    uk_postal_codes = {}
    dirname = os.path.dirname(__file__)
    data_path = os.path.join(dirname, 'countries/test_data_uk.txt')

    with open(data_path) as ukfile:
        for line in ukfile:
            pt, expected = line.partition("=")[::2]
            example = UKPostalCode(pt)
            self.assertEqual(
              example.is_valid(),
              expected.strip() == 'true',
              f'Uncaught for postal code {pt}'
            )
