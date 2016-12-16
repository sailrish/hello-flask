import os
import server
import unittest

class ServerTestCase(unittest.TestCase):

    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()

    def test_root(self):
        res = self.app.get('/')
        assert 'Hello, Flask!' in res.data

if __name__ == '__main__':
    unittest.main()
