import random

def fast_exp(a, e, m):
    r = 1
    if 1 & e:
        r = a
    while e:
        e >>= 1
        a = (a * a) % m
        if e & 1: r = (r * a) % m
    return r

def fermat_test(n):
    n=int(n)
    a=random.randint(2,n-2)
    r=fast_exp(a,(n-1),n)
    if r == 1:
        return True
    else:
        return False

def test():
    print("This is fermats primality test\nPlease use this for just seeing it is prime")
    number = int(input("Enter the number for primality test\n"))
    x=fermat_test(number)
    if x== True:
        print("Probably Prime")
    else:
        print("Probably not a Prime")

test()