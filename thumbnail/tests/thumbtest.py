#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.abspath(os.path.dirname(__file__)))))
reload(sys)
sys.setdefaultencoding('utf-8')


class ThumbTest(unittest.TestCase):
    """Unittest for thumbnail
    """
    def _demo(self):
        self.assertEquals(1000, 1000);
        self.assertFalse(False)
        self.assertTrue(True)
        # self.assertRaises(TypeError, (lambda : raise TypeError))


if __name__ == "__main__":
    unittest.main()
        
