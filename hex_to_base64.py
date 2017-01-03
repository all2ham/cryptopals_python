import crypto
import unittest

input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
should_produce = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

class tests_1_1a(unittest.TestCase):
    def test(self):
        self.assertEqual(crypto.hex_to_base64(input),should_produce)
class tests_1_1b(unittest.TestCase):
    def test(self):
        self.assertEqual(crypto.base64_to_hex(should_produce),input)

if __name__ == '__main__':
    unittest.main()