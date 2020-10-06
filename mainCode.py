import os
import sys
import time
import multiprocessing
import hashlib
import binascii
import itertools

MATRIX_SIZE = [3, 3]
MAX_LEN = MATRIX_SIZE[0]*MATRIX_SIZE[1]
MIN_POSITIONS_NUMBER = 3
FOUND = multiprocessing.Event()


def lookup(param):
    global FOUND
    lenhash = param[0]
    target = param[1]
    positions = param[2]

    if FOUND.is_set() is True:
        return None

    # get all possible permutations
    perms = itertools.permutations(positions, lenhash)
    # for each permutation
    for item in perms:
        # build the pattern string
        if FOUND.is_set() is True:
            return None
        pattern = ''.join(str(v) for v in item)
        # convert the pattern to hex (so the string '123' becomes '\x01\x02\x03')
        key = binascii.unhexlify(
            ''.join('%02x' % (ord(c) - ord('0')) for c in pattern))
        # compute the hash for that key
        sha1 = hashlib.sha1(key).hexdigest()
        # pattern found
        if sha1 == target:
            FOUND.set()
            return pattern
    # pattern not found
    return None


def show_pattern(pattern):
    """
    Shows the pattern "graphically"
    """

    gesture = [None, None, None, None, None, None, None, None, None]

    cont = 1
    for i in pattern:
        gesture[int(i)] = cont
        cont += 1

    print("[+] Gesture:\n")

    for i in range(0, 3):
        val = [None, None, None]
        for j in range(0, 3):
            val[j] = " " if gesture[i * 3 +
                                    j] is None else str(gesture[i * 3 + j])

        print('  -----  -----  -----')
        print('  | %s |  | %s |  | %s |  ' % (val[0], val[1], val[2]))
        print('  -----  -----  -----')


def crack(target_hash):
    ncores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(ncores)
    # generates the matrix positions IDs
    positions = [i for i in range(MAX_LEN)]

    # sets the length for each worker
    def generate_worker_params(x): return [x, target_hash, positions]
    params = [generate_worker_params(i) for i in range(
        MIN_POSITIONS_NUMBER, MAX_LEN + 1)]

    result = pool.map(lookup, params)
    pool.close()
    pool.join()

    ret = None
    for r in result:
        if r is not None:
            ret = r
            break
    return ret


def main():
    print('')
    print('################################')
    print('# Android Pattern Lock Cracker #')
    print('#             v1.0             #')
    print('# ---------------------------- #')
    print('#    Script by Chema Garcia    #')
    print('#     Modified by unpass       #')
    print('#     chema@safetybits.net     #')
    print('#         @realxnesia          #')
    print('################################\n')

    #print('[i] Taken from: http://forensics.spreitzenbarth.de/2012/02/28/cracking-the-pattern-lock-on-android/\n')

    # check parameters
    if len(sys.argv) != 2:
        sys.stdout = open("logs.txt","a")
        print('[+] Usage: %s /path/to/gesture.key\n' % sys.argv[0])
        sys.exit(0)
        sys.stdout.close()

    # check gesture.key file
    if not os.path.isfile(sys.argv[1]):
        sys.stdout = open("logs.txt","a")
        print("[!] ERROR")
        print("[e] Cannot access to %s file\n" % sys.argv[1])
        print("[!] Make sure you save the gesture file along with the script folder(!)")
        sys.exit(-1)
        sys.stdout.close()

    with open(sys.argv[1], "rb") as f:
        gest = f.read(hashlib.sha1().digest_size).hex()

    f.close()

    # check hash length
    if len(gest) / 2 != hashlib.sha1().digest_size:
        sys.stdout = open("logs.txt","a")
        print("[!] ERROR")
        print("[e] Invalid gesture file?\n")
        sys.exit(-2)
        sys.stdout.close

    # try to crack the pattern
    t0 = time.time()
    pattern = crack(gest)
    t1 = time.time()

    if pattern is None:
        sys.stdout = open("logs.txt","a")
        print(" ")
        print("[!] The pattern was not found...")
        rcode = -1
        sys.stdout.close()
    else:
        sys.stdout = open("logs.txt","a")
        print(" ")
        print("[*] The pattern has been FOUND!!! => %s\n" % pattern)
        show_pattern(pattern)
        print("")
        print("It took: %.4f seconds" % (t1-t0))
        rcode = 0
        sys.stdout.close()

    sys.exit(rcode)

if __name__ == "__main__":
    main()
