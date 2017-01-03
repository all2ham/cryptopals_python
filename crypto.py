import binascii
import base64
import string

def hex_to_base64(h):
    """Takes hex string as input and returns base64 string"""
    return base64.b64encode(binascii.a2b_hex(h))

def base64_to_hex(b64):
    """Takes b64 string as input and returns hex string"""
    return binascii.b2a_hex(base64.b64decode(b64))

def fixed_XOR(h1,h2):
    """Takes two equal length hex buffers and produce XOR combination."""
    return '{0:02x}'.format(int(h1,16) ^ int(h2,16))

def chi_squared(test,exp):
    ssd = 0
    for l in string.ascii_lowercase:
        ssd += ((test[l]-exp[l])**2)/exp[l]
    return ssd


def char_count_to_frequency(char_count_dict,slen):
    s_freq = {}
    if slen == 0:
        return None
    else:
        for k,v in char_count_dict.iteritems():
            s_freq[k] = v/float(slen)
        return s_freq

def english_char_freq():
    #init english dict
    english_freq = [
        0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,  # A-G
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,  # H-N
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,  # O-U
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074, 0.18317            # V-Z and space
    ]
    english_freq_dict = {}
    for i,l in enumerate(string.ascii_lowercase+' '):
        english_freq_dict[l] = english_freq[i]
    return english_freq_dict

def try_and_score_repeating_key(h1,key):
    guess_dict = dict.fromkeys(string.ascii_lowercase +' ', 0)
    english_freq_dict = english_char_freq()
    msghex = h1
    mlen = len(msghex)
    encrypted = ''
    for i,c in enumerate(msghex):
        g =  (int(msghex[(2*i):((2*i)+2)],16)^int(key, 16))
        encrypted += '{0:02x}'.format(int(g))
        if (2*i)>mlen-3:
          break
    # def recursively_apply_key(msg,encrypted,key):
    #     if len(msg)==0:
    #         return encrypted
    #     firstpart, remainder = msg[:2], msg[2:]
    #     g =  (int(firstpart,16)^int(key,16))
    #     encrypted += '{0:02x}'.format(int(g))
    #     return recursively_apply_key(remainder,encrypted,key)
    # guess = binascii.a2b_hex(recursively_apply_key(h1,encrypted,key))
    guess = binascii.a2b_hex(encrypted)

    filtered_string = ''.join(filter(lambda x:x in (string.ascii_letters + ' '), guess))
    for l in filtered_string:
        guess_dict[l.lower()] += 1
    testfreq =  char_count_to_frequency(guess_dict,len(filtered_string))
    if testfreq:
        score = chi_squared(testfreq,english_freq_dict)
    else:
        score = float('inf')
    return key, filtered_string, score

def break_single_byte_cypher(h1):
    hex_set = "0123456789abcdef"
    kL = [k1 + k2 for k1 in hex_set for k2 in hex_set] # list of all bytes in hex
    results = []
    for k in kL:
        results.append(try_and_score_repeating_key(h1,k))
    best = min(results, key=lambda p: (p[2]))
    # print 'Best match occurs with key: '+(best[0])+'\n Decrypted message is: ' + best[1] + '\n matches English character frequency with chi squared value of: '+str(best[2])
    # return best
    # print results
    return best

def encrypt_repeating_key_XOR(msg,key):
    """Takes message string and applies repeating key string XOR.
    Returns encrypted string."""
    msghex = binascii.b2a_hex(msg)
    keys = []
    encrypted = ''
    klen = len(key)
    mlen = len(msghex)
    for c in key:
        keys.append(binascii.b2a_hex(c))
    for i,c in enumerate(msghex):
        g =  (int(msghex[(2*i):((2*i)+2)],16)^int(keys[(i+klen)%klen], 16))
        encrypted += '{0:02x}'.format(int(g))
        if (2*i)>mlen-3:
          break
    # def recursively_apply_key(msg,encrypted,iter):
    #     if len(msg)==0:
    #         return encrypted
    #     firstpart, remainder = msg[:2], msg[2:]
    #     g =  (int(firstpart,16)^int(keys[iter%klen], 16))
    #     encrypted += '{0:02x}'.format(int(g))
    #     iter += 1
    #     return recursively_apply_key(remainder,encrypted,iter)
    # return recursively_apply_key(msghex,encrypted,iter)
    return encrypted

def hamming_distance(s1,s2):
    """Finds hamming distance between two ASCII strings"""
    xor = fixed_XOR(binascii.b2a_hex(s1),binascii.b2a_hex(s2))
    hd = 0
    for d in bin(int(xor, 16))[2:]:
        if d == '1':
            hd +=1
    return hd


def pkcs7_pad(block,l):
    return '{0:{1}<{len}}'.format(block,'\x04',len = l)


if __name__ == "__main__":
    pass