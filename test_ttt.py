import unittest

import ttt
from ttt import Board, GameStates


class TestTTT(unittest.TestCase):

    def setUp(self):
        self.valid = list("xo.xo.xo.")

    def test_col_accessor(self):
        b = Board(self.valid)
        self.assertEqual(list('xxx'), b.col(0))
        self.assertEqual(list('ooo'), b.col(1))
        self.assertEqual(list('...'), b.col(2))

    def test_row_accessor(self):
        b = Board(self.valid)
        self.assertEqual(list('xo.'), b.row(0))
        self.assertEqual(list('xo.'), b.row(1))
        self.assertEqual(list('xo.'), b.row(2))

    def test_diag_accessor(self):
        b = Board(self.valid)
        self.assertEqual(list('xo.'), b.diag(0))
        self.assertEqual(list('.ox'), b.diag(1))

    def test_bad_boards(self):

        # or something
        self.assertEqual(GameStates.invalid, ttt.game_state(None))
        self.assertEqual(GameStates.invalid, ttt.game_state("xo.ox.ox."))
        self.assertEqual(GameStates.invalid, ttt.game_state([]))
        self.assertEqual(GameStates.invalid, ttt.game_state(['.']*8))
        self.assertEqual(GameStates.invalid, ttt.game_state(['.']*10))
        self.assertEqual(GameStates.invalid, ttt.game_state(['x']*2 + ['.']*7))
        self.assertEqual(GameStates.invalid, ttt.game_state(['o']*2 + ['.']*7))
        # x goes first
        self.assertEqual(GameStates.invalid, ttt.game_state(['o']*1 + ['.']*8))

    def test_good_boards(self):
        self.assertEqual(GameStates.unfinished, ttt.game_state(['.']*9))
        self.assertEqual(GameStates.x_wins, ttt.game_state(list("xxx.oo...")))
        self.assertEqual(GameStates.x_wins, ttt.game_state(list("xo.xo.x..")))
        self.assertEqual(GameStates.o_wins, ttt.game_state(list("ooo.xx.x.")))

    def test_10(self):
        self.assertEqual(GameStates.invalid, ttt.game_state(list("xo.xo.xo.")))
        self.assertEqual(GameStates.draw, ttt.game_state(list("xoxxoxoxo")))

    def test_double_wins(self):
        self.assertEqual(
            GameStates.invalid,
            ttt.game_state(
                [
                    'x', 'x', 'o',
                    'o', 'x', 'o',
                    'o', 'x', 'x',
                ]
            )
        )
