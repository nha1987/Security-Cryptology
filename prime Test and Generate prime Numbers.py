from random import randrange, getrandbits
from itertools import repeat

def isProbablePrime(n, t = 7):
    """Miller-Rabin primality test"""
    
    def isComposite(a):
        """Check if n is composite"""
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    assert n > 0
    if n < 3:
        return [False, False, True][n]
    elif not n & 1:
        return False
    else:
        s, d = 0, n - 1
        while not d & 1:
            s += 1
            d >>= 1
    for _ in repeat(None, t):
        if isComposite(randrange(2, n)):
            return False
    return True

def getPrime(n):
    """Get a n-bit prime"""  
    p = getrandbits(n)
    while not isProbablePrime(p):
        p = getrandbits(n)     
    return p  
    
def multiplicative_inverse(a, b):
    """ Find multiplicative inverse of a modulo b (a > b)
        using Extended Euclidean Algorithm """
    
    origA = a
    X = 0
    prevX = 1
    Y = 1
    prevY = 0

    while b != 0:

        temp = b
        quotient = a/b
        b = a % b
        a = temp

        temp = X
        a = prevX - quotient * X
        prevX = temp

        temp = Y
        Y = prevY - quotient * Y
        prevY = temp

    return origA + prevY      
    
if __name__ == "__main__":
    

    
    # get 2 random prime 64 bits long and assign then the variable names p and q
    p = (getPrime(64))
    q =(getPrime(64))
    m = (p-1)*(q-1)
    n = p*q

    
    print "P is : ", p
    print "Q is : ", q
    print "M is :",	m
    print "N is :",	n
    print "E is :", e
    print "D is :", d
    print "Tuples are :", ((n,e), (n,d))
    
    
    
