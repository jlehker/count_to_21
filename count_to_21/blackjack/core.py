# -*- coding: utf-8 -*-


class Card:
    """
    A standard playing card with a rank and a suit. Also has a point value from 1 to 11.
    Aces have point values that depend on the Hand.
    """


class Deck:
    """
    A complete set of 52 standard Cards.
    """


class Hand:
    """
    A collection of Cards with one or two point values: a hard value (an ace counts as 1)
    and a soft value (an ace counts as 11). The house will reveal one Card to the player.
    """


class Player:
    """
    Places the initial ante Bets, updates the stake with amounts won and lost. Accepts or declines offered additional
    bets, including insurance, and split. Accepts or declines offered resolution, including even money.
    Chooses among hit, double and stand options.
    """


class Game:
    """
    Runs the game: offers bets to Player, deals the Cards from the Deck to Hands, updates the state of the game,
    collects losing bets, pays winning bets. Splits Hands. Responds to player choices of hit, double and stand.
    This encapsulates the basic sequence of play into a single class.
    """

    def __init__(self):
        self.test = 10

    def say_hi(self):
        return self.test
