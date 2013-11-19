#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import unittest
import os, sys
from urllib import urlencode
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(os.path.dirname(__file__))))))
reload(sys)
sys.setdefaultencoding('utf-8')

from thumbnail import app


class ThumbTest(unittest.TestCase):
    """Unittest for thumbnail
    """
    def _demo(self):
        self.assertEquals(1000, 1000);
        self.assertFalse(False)
        self.assertTrue(True)
        # self.assertRaises(TypeError, (lambda : raise TypeError))

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        self.app = None

    def _thumb(self, width, height):
        request_url = '/thumbnail/7553fa3ecc295c3dfb204eb65441541c.jpg/?'
        request_url += urlencode({'w': str(width), 'h': str(height)})
        rv = self.app.get(request_url)
        self.assertTrue('1' in rv.data)
        self.assertEquals(200, rv.status_code)
    
    def test_thumb(self):
        request_url = '/thumbnail/7553fa3ecc295c3dfb204eb65441541c.jpg/?'
        request_url += urlencode({'w': 100})
        rv = self.app.get(request_url)
        self.assertEquals(400, rv.status_code)

    def test_thumbs(self):
        width = 1000
        while width > 0:
            self._thumb(width, width)
            width -= 1


if __name__ == "__main__":
    unittest.main()
