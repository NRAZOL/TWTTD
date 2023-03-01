'''https://www.codewars.com/kata/541c8630095125aba6000c00'''


def digital_root(n):
    while len(str(n)) > 1:
        n = sum([int(''.join(i)) for i in str(n)])
    return n