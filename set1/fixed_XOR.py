import unittest
import crypto


h1 = '1c0111001f010100061a024b53535009181c'
h2 = '686974207468652062756c6c277320657965'

should_produce = '746865206b696420646f6e277420706c6179'


class test_fixed_XOR(unittest.TestCase):
    def test(self):
        self.assertEqual(crypto.fixed_XOR(h1,h2), should_produce)

if __name__ == '__main__':
    unittest.main()