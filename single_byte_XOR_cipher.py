import crypto

h1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
# has been xor'd against a single character, find the key

print crypto.break_single_byte_cypher(h1)