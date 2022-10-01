#!/usr/bin/env python3

'''
Enum for countries code
'''

from enum import Enum

class Countries(Enum):
    UK = 'UK'

    @classmethod
    def key(self, key):
        '''
        Return enum base on matching key

        :param  str     key     Matching key
        :return:    Matching enum key. If key does
                    does not match, return None
        :type: Enum
        '''
        try:
            return Countries[key.upper()]
        except:
            return None
