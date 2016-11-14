#!/usr/bin/env pythondg

def extended_gcd1(a, b):
    x = 0
    y = 1
    previousx = 1
    previousy = 0
    while b != 0:
        quo = a / b
        a, b = b, a % b
        x, previousx = previousx - quo * x, x
        y, previousy = previousy - quo * y, y
    return (previousx, previousy)
 
def extended_gcd2(a, b):
    if b == 0:
        return (1, 0)
    else:
        q, r = a / b, a % b
        s, t = extended_gcd2(b, r)
        return (t, s - q * t)
    
if __name__ == "__main__":
    print extended_gcd1(1851748955399034079,13845053846733511319)


