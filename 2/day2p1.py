#!/usr/bin/python3 -tt
from collections import Counter

def main():
    c = {3:0,2:0}
    with open('input.sdx', 'r+') as ifile:
        for line in ifile:
            x = set(Counter(line).values())
            if 3 in x:
               c[3] += 1
            if 2 in x:
                c[2] += 1
    print(c[3] * c[2])

if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))