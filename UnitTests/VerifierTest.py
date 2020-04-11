import unittest

from WorkLayer.Verifier import Verifier

v = Verifier()

class VerifierTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_num(self):
        global v
        self.assertTrue(v.numberVerifier(5))
        self.assertTrue(v.numberVerifier(0))
        self.assertFalse(v.numberVerifier('a'))
        self.assertFalse(v.numberVerifier('0'))

    def test_str(self):
        global v
        self.assertTrue(v.stringVerifier('12312'))
        self.assertTrue(v.stringVerifier('12312'))
        self.assertTrue(v.stringVerifier('asdasdfs'))
        self.assertTrue(v.stringVerifier('123123sadas  asd'))
        self.assertFalse(v.stringVerifier('!@#^@!'))
        self.assertFalse(v.stringVerifier(''))

    def test_date(self):
        global v
        self.assertTrue(v.dateVerifier('2020-11-12'))
        self.assertTrue(v.dateVerifier('2020-02-29'))
        self.assertFalse(v.dateVerifier('123123sagas  asd'))
        self.assertFalse(v.dateVerifier('1231-1-1'))
        self.assertFalse(v.dateVerifier('1231-01-00'))


if __name__ == '__main__':
    unittest.main()
