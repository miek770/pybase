# -*- coding: utf-8 -*-

import unittest, sys, os

class TestMain(unittest.TestCase):

    def test_imports(self):
        try:
            import main
        except ImportError:
            self.fail()

if __name__ == '__main__':
    unittest.main(verbosity=2)

