
def gcd(a, b):
    if a == 0:
        return b, 0, 1
    ans, x, y = gcd(b % a, a)
    return ans, y - (b // a) * x, x


def mod_inv(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        raise Exception("Inverse Modulo doesn't exist")
    return x % m


def mod_pow(b, e, m):
    res = 1
    for i in range(e):
        res *= b % m
    return res % m


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def e_sel(p, q):
    lim = (p - 1) * (q - 1)
    e_val = 2
    while e_val < lim:
        try:
            mod_inv(e_val, lim)
            break
        except:
            e_val += 1
    return e_val


def encrypt(msg, n, e):
    return mod_pow(msg, e, n)


def decrypt(cip, n, d):
    return mod_pow(cip, d, n)


def rsa_encrypt(m, n, e):
    return ''.join([chr(encrypt(ord(x), n, e)) for x in m])


def rsa_decrypt(c, n, d):
    return ''.join([chr(decrypt(ord(x), n, d)) for x in c])


def key_gen(p, q):
    e = e_sel(p, q)
    totient = (p - 1) * (q - 1)
    d = mod_inv(e, totient)
    n = p * q
    return n, e, d


# p, q = 7, 13
# e = e_sel(p, q)
# print(e)
# totient = (p - 1) * (q - 1)
# d = mod_inv(e, totient)
# n = p * q
# print(n, e)
# print(n, d)


# msg = "HELLO THERE I AM TEJAS. WE HAVE LAB TODAY."
# print("Message: ")
# print(msg)
# print()

# print("Encryption: ")
# cip = rsa_encrypt(msg, n, e)
# print(cip)

# print()
# print("Decryption: ")
# txt = rsa_decrypt(cip, n, d)
# print(txt)
