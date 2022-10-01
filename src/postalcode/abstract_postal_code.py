#!/usr/bin/env python3

'''
Module PostalCode - Abstract
'''
import abc
from abc import ABC, abstractmethod

class AbstractPostalCode(ABC):
  @abstractmethod
  def __init__(self, postalcode) -> None:
    '''
    Constractor

    :param  str   postalcode    String version
    '''
    self.str = postalcode
    pass

  @abstractmethod
  def is_valid(self):
    '''
    Abstract method to validate is postal
    code valid
    '''
    raise NotImplementedError
