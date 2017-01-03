import crypto
import unittest

class tests_2_1(unittest.TestCase):
    def test(self):
        self.assertEqual(crypto.pkcs7_pad(s,l),s_w_pad)

if __name__ == '__main__':
    s = "YELLOW SUBMARINE"
    l = 20
    s_w_pad = "YELLOW SUBMARINE\x04\x04\x04\x04"
    unittest.main()