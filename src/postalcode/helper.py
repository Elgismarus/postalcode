#!/usr/bin/env python3

'''
Postal code helpers
'''

from .enums.countries import Countries
from .uk_postal_code import UKPostalCode

def valid_postal_code(country, postal_code):
  '''
  Validate postal code for country specify

  :param  str   country       Short name country
  :param  str   postal_code   Postal code to validate
  :return: Boolean
  '''
  matcher = country if isinstance(country, Countries) else Countries.key(country)
  match matcher:
    case Countries.UK:
      pc = UKPostalCode(postal_code)
      return pc.is_valid()
    case _:
      raise NameError("Country '" + country + "' not yet supported.")
