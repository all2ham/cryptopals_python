import os
import crypto
import unittest
import itertools
import numpy as np
import binascii
import base64

key_guess_range = [2,40]

#importing data
# crypt = ''
# f = open(os.path.dirname(__file__) + '../ch6.txt')
# for line in f:
#     # crypt += line
#     crypt += line.rstrip('\n')

# crypt = crypto.base64_to_hex(crypt)

crypt = base64.b64decode(open(os.path.dirname(__file__) + 'ch6.txt', 'r').read())


# finding most probable size of key
results = []
for size in range(key_guess_range[0],key_guess_range[1]+1):
    first4blocks = [crypt[0:size],
                    crypt[size:(2*size)],
                    crypt[(2*size):(3*size)],
                    crypt[(3*size):(4*size)],
                    ]

    # print crypto.hamming_distance(b1,b2)/size
    hamming_values = []
    for pair in itertools.combinations(first4blocks,2):
        hamming_values.append(crypto.hamming_distance(pair[0],pair[1])/size)
    results.append((size, np.average(hamming_values)))

top3 = sorted(results, key=lambda v: (v[1]))[:3]
print top3

def splice_into_blocks(s,bs):
    blocklist = []
    if (len(s)%bs):
        s = s+'0'*(bs-len(s)%bs)
    for i in range((len(s)/bs)+1):
        blocklist.append(list(s[bs*(i):bs*(i+1)]))
    del blocklist[-1]
    return blocklist

bl = splice_into_blocks(crypt, 29)

def byte_transpose(blocklist):
    bs = len(blocklist[0])
    blocklist_t = [['0']*len(blocklist) for i in range(bs)]
    for k1,i in enumerate(blocklist):
        for k2,j in enumerate(i):
            blocklist_t[k2][k1] = j
    return [''.join(i) for i in blocklist_t]

keyis = ''
for i in byte_transpose(bl):
    x = crypto.break_single_byte_cypher(binascii.b2a_hex(i))
    # if len(x[1]) > 1:
    print 'block: ' + str(i), x[0], '{0:04f}'.format(x[2]), x[1]
    keyis += binascii.a2b_hex(x[0])

print keyis
print binascii.a2b_hex(crypto.encrypt_repeating_key_XOR(crypt,keyis))

class tests_1_6(unittest.TestCase):
    def test(self):
        self.assertEqual(crypto.hamming_distance(s1,s2),should_produce)

if __name__ == '__main__':
    s1 = "this is a test"
    s2 = "wokka wokka!!!"
    should_produce = 37
    unittest.main()