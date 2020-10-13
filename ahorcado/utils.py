# coding=utf-8
"""
hangman.utils
~~~~~~~~~~~~~
App utilities.
"""
from __future__ import absolute_import

from random import choice

__all__ = ['WordBank', 'FlashMessage', 'GameLost', 'GameWon', 'GameOverNotificationComplete']


class WordBank(object):
    """Default collection of words to choose from"""

    WORDS = ['AUTO', 'CASA', 'PERRO', 'AVION', 'LORO', 'LEON', 'HORNO', 'RAYO', 'COMPUTADORA', 'CAMIONETA',
            'PELOTA', 'FUEGO', 'CONEJO', 'JIRAFA', 'ELEFANTE']

    @classmethod
    def set(cls, *values):
        """Set word list."""

        cls.WORDS = list(values)

    @classmethod
    def get(cls):
        """Get a random word from word list."""

        return choice(cls.WORDS)


class FlashMessage(object):
    """Basic "flash message" implementation."""

    message = ''
    game_lost = False
    game_won = False

    def __call__(self, message):
        """Set message to be flashed."""

        self.message = str(message)

    def __str__(self):
        """Returns and clears the message"""

        message, self.message = self.message, ''
        return str(message)

    def __bool__(self):
        # Python3 compatibility
        return self.__nonzero__()

    def __nonzero__(self):
        # Python2 compatibility
        return bool(self.message)

    def __eq__(self, other):
        return bool(self.message) == other

    def __format__(self, format_spec):
        """Format and clear flash message"""

        return format(str(self), format_spec)


class GameWon(Exception):
    """Raised when answer has been guessed."""


class GameLost(Exception):
    """Raised when out of turns."""


class GameOverNotificationComplete(Exception):
    """Raised when controller should break game loop."""