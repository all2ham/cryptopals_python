import crypto

msg = 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
key = 'ICE'

x = crypto.encrypt_repeating_key_XOR(msg,key)
print 'Input was encrypted to: '+x