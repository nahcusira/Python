from itertools import chain, product
import hashlib
import string

def bruteforce(charset, maxlength):
    return (''.join(ch)
        for ch in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

passwordhash = '5f4dcc3b5aa765d61d8327deb882cf99'
for plaintext in bruteforce(string.ascii_lowercase, 10):
    bruteforcedhash = hashlib.md5(plaintext.encode('utf-8')).hexdigest()
    if bruteforcedhash == passwordhash:
        print('plain text of the given hash is',plaintext)
        break