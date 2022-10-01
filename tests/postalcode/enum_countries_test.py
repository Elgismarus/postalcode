#!/usr/bin/env python3

'''
Unit test for enum Countries
'''

import unittest

from src.postalcode.enums.countries import Countries

class EnumCountriesTest(unittest.TestCase):
  '''
  Enum Countries testing
  '''

  def test_from_string(self):
    '''
    Test to get enum from string
    '''
    val = Countries.key('UK')
    self.assertEqual(val, Countries.UK)

  def test_from_lower_string(self):
    '''
    Test if countries is lower case
    '''
    val = Countries.key('uk')
    self.assertEqual(val, Countries.UK)

  def test_from_key__not_exist(self):
    '''
    Test against a key that does not exist
    '''
    val = Countries.key('unknown')
    self.assertEqual(val, None)
