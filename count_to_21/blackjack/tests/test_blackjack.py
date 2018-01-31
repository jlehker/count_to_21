#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `blackjack` package."""


import unittest
from count_to_21 import blackjack


class TestBlackjack(unittest.TestCase):
    """Tests for `blackjack` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        game = blackjack.Game()
        self.assertEqual(game.say_hi(), 10)

    def test_command_line_interface(self):
        """Test the CLI."""
        game = blackjack.Game()
        pass
