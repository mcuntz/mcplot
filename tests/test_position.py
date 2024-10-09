#!/usr/bin/env python
"""
This is the unittest for position module.

python -m unittest -v tests/test_position.py
python -m pytest --cov=mcplot --cov-report term-missing -v tests/test_position.py

"""
import unittest


class TestPosition(unittest.TestCase):
    """
    Tests for position.py
    """

    def test_division(self):
        import numpy as np
        from mcplot import position

        pos = position(2, 2, 1)
        self.assertEqual(list(np.around(pos, 3)), [0.125, 0.545, 0.338, 0.335])

        pos = position(2, 2, 1, height=0.5)
        self.assertEqual(list(np.around(pos, 3)), [0.125, 0.71, 0.338, 0.5])

        pos = position(2, 2, 1, width=0.5)
        self.assertEqual(list(np.around(pos, 3)), [0.125, 0.545, 0.5, 0.335])

        pos = position(2, 2, 1, sortcol=True)
        self.assertEqual(list(np.around(pos, 3)), [0.125, 0.545, 0.338, 0.335])

        pos = position(2, 2, 1, golden=True)
        self.assertEqual(list(np.around(pos, 3)), [0.125, 0.419, 0.338, 0.209])

        pos = position(2, 2, 1, inversegolden=True)
        self.assertEqual(list(np.around(pos, 3)), [0.125, 0.545, 0.207, 0.335])

        pos = position(2, 2, 1, golden=True, sortcol=True)
        self.assertEqual(list(np.around(pos, 3)), [0.125, 0.419, 0.338, 0.209])

        pos = position(2, 2, 1, top=1., bottom=0., left=0., right=1.,
                       hspace=0., vspace=0.)
        self.assertEqual(list(np.around(pos, 3)), [0., 0.5, 0.5, 0.5])

        pos = position(2, 2, 2, top=1., bottom=0., left=0., right=1.,
                       hspace=0., vspace=0.)
        self.assertEqual(list(np.around(pos, 3)), [0.5, 0.5, 0.5, 0.5])

        pos = position(2, 2, 3, top=1., bottom=0., left=0., right=1.,
                       hspace=0., vspace=0.)
        self.assertEqual(list(np.around(pos, 3)), [0., 0., 0.5, 0.5])

        pos = position(2, 2, 4, top=1., bottom=0., left=0., right=1.,
                       hspace=0., vspace=0.)
        self.assertEqual(list(np.around(pos, 3)), [0.5, 0., 0.5, 0.5])

        pos = position(2, 2, 1, top=1., bottom=0., left=0., right=1.,
                       hspace=0., vspace=0., golden=True)
        self.assertEqual(list(np.around(pos, 3)), [0., 0.309, 0.5, 0.309])

        pos = position(2, 2, 2, top=1., bottom=0., left=0., right=1.,
                       hspace=0., vspace=0., golden=True)
        self.assertEqual(list(np.around(pos, 3)), [0.5, 0.309, 0.5, 0.309])

        pos = position(2, 2, 3, top=1., bottom=0., left=0., right=1.,
                       hspace=0., vspace=0., golden=True)
        self.assertEqual(list(np.around(pos, 3)), [0., 0., 0.5, 0.309])

        pos = position(2, 2, 4, top=1., bottom=0., left=0., right=1.,
                       hspace=0., vspace=0., golden=True)
        self.assertEqual(list(np.around(pos, 3)), [0.5, 0., 0.5, 0.309])

        figsize = [8, 11]
        pos = position(2, 2, 1, golden=True, sortcol=True, figsize=figsize)
        self.assertEqual(list(np.around(pos, 3)), [0.125, 0.334, 0.338, 0.152])

        pos = position(2, 2, 1, figsize=figsize, left=0.1)
        self.assertEqual(list(np.around(pos, 3)), [0.1, 0.426, 0.35, 0.244])

        pos = position(2, 2, 1, figsize=figsize, left=0.1, golden=True)
        self.assertEqual(list(np.around(pos, 3)), [0.1, 0.34, 0.35, 0.157])

        self.assertRaises(ValueError, position, 2, 2, 1, width=0.6,
                          golden=True)
        self.assertRaises(ValueError, position, 2, 2, 1, height=0.6,
                          inversegolden=True)


if __name__ == "__main__":
    unittest.main()
