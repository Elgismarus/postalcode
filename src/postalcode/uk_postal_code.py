#!/usr/bin/env python3

'''
Module UKPostalCode
'''

from .abstract_postal_code import AbstractPostalCode
import re

UK_POSTAL_CODE_REGEX = "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"

class UKPostalCode(AbstractPostalCode):
  '''
  Class for UK postal code operations
  '''

  def __init__(self, postalcode):
    '''
    Construtor
    '''
    super().__init__(postalcode)

  def is_valid(self):
    '''
    Validate if provided postal code
    match UK pattern

    :return: Boolean
    '''
    pattern = re.compile(UK_POSTAL_CODE_REGEX)
    return bool(pattern.match(self.str))
