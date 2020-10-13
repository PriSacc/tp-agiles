"""
ahorcado model
~~~~~~~~~~~~~
"""
from __future__ import absolute_import

import re
from collections import namedtuple
# from .utils import WordBank, GameLost, GameWon

class Ahorcado(object):
    """
    Add comment here
    """

    # CLASS PROPERTIES 
    # ----------------
    MAX_TURNS = 10
    answer_rules = re.compile('^[A-Z]{1,16}$')
    guess_rules = re.compile('^[A-Z]$')
    _repr = namedtuple('ahorcado', ['status', 'fallo', 'turnos_restantes'])

    # CONSTRUCTOR
    # -----------
    def __init__(self, answer=None):

        if not answer:
            # Populate answer
            answer = # WordBank



