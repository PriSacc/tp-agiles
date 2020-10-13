"""
ahorcado model
~~~~~~~~~~~~~
"""
from __future__ import absolute_import

import re
from collections import namedtuple
from utils import WordBank, GameLost, GameWon

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
            answer = WordBank.get()

        # Validate answer
        if not self.is_valid_answer(answer):
            raise ValueError("Debe ingresar una letra de A-Z")
        
        self.answer = answer.upper()
        self._misses = set()
        self._hits = set()

    # API
    # --------------------
    def guess(self, letter): 
        """Add a letter to hit or miss"""

        #validate input
        if not self.is_valid_guess(letter):
            raise ValueError("Debe ser una letra de A-Z")
        
        # add to hit or miss 
        # add to hits or misses
        is_miss = letter.upper() not in self.answer
        if is_miss:
            self._add_miss(letter)
        else:
            self._add_hit(letter)

        return self

    # INSTAMCE PROPERTIES
    # --------------------
    @property
    def misses(self): 
        """List of misses"""

        return sorted(list(self._misses))


    @misses.setter
    def misses(self, letters):
        for letter in letters:
            self._add_miss(letter)

    @property
    def hits(self):
        """List of hits."""

        return sorted(list(self._hits))

    @hits.setter
    def hits(self, letters):
        for letter in letters:
            self._add_hit(letter)

    @property
    def remaining_turns(self):
        """Calculate number of turns remaining."""

        return self.MAX_TURNS - len(self.misses)

    @property
    def status(self):
        """Build a string representation of status."""

        hits = self.hits  # calculated property

        def fill_in(letter):
            """Replace non-hits with `_`."""

            return letter if letter in hits else '_'

        return ''.join(fill_in(letter) for letter in self.answer)

    # UTILITIES
    # -------------------------------------------------------------------
    def _add_miss(self, value):
        """Add a letter to misses.  Check for game over."""

        self._misses.add(value.upper())
        if self.remaining_turns <= 0:
            raise GameLost

    def _add_hit(self, value):
        """Add a letter to hits. Check for game won"""

        self._hits.add(value.upper())
        if self._hits == set(self.answer):
            raise GameWon

    def is_valid_answer(self, word):
        """Validate answer.  Letters only.  Max:16"""

        word = str(word).upper()
        return not not self.answer_rules.search(word)

    def is_valid_guess(self, letter):
        """Validate guess.  Letters only.  Max:1"""

        letter = str(letter).upper()
        return not self.guess_rules.search(letter)

    def __repr__(self):
        return repr(self._repr(self.status, self.misses, self.remaining_turns))




