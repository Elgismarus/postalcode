#!/usr/bin/env python3

'''
Unit test for postal code helper
'''

import unittest
from unittest import mock

from src.postalcode.enums.countries import Countries
from src.postalcode.helper import valid_postal_code
from src.postalcode.uk_postal_code import UKPostalCode

class HelperTest(unittest.TestCase):
  '''
  Test postal code helper
  '''

  def test_valid_postal_code_not_supported(self):
    '''
    Test return not supported if country not yet
    implemented
    '''
    with self.assertRaises(Exception) as context:
        valid_postal_code('unknown', '')

    self.assertEqual(
        "Country 'unknown' not yet supported.",
        str(context.exception)
    )

  @mock.patch('src.postalcode.uk_postal_code')
  def test_valid_postal_code_uk(self, mock_uk):
    '''
    Test call UKPostalCode validator
    '''
    self.assertTrue(
      valid_postal_code(Countries.UK, 'EC1A 1BB')
    )
    instance = mock_uk.return_value
    instance.validate.calledOnce()

    self.assertFalse(
      valid_postal_code(Countries.UK, 'A11')
    )

  @mock.patch('src.postalcode.uk_postal_code')
  def test_valid_postal_code_string(self, mock_uk):
    '''
    Test when country is string
    '''
    self.assertTrue(
      valid_postal_code('UK', 'EC1A 1BB')
    )
    instance = mock_uk.return_value
    instance.validate.calledOnce()

    self.assertTrue(
      valid_postal_code('uk', 'EC1A 1BB')
    )
    instance = mock_uk.return_value
    instance.validate.calledOnce()
