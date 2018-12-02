#!/usr/bin/python3 -tt
from collections import Counter

def main():
    ids = []
    with open('input.sdx', 'r+') as ifile:
        for line in ifile:
            x = set(Counter(line).values())
            if 3 in x or 2 in x:
                ids.append(line)

    while len(ids):
        x = ids.pop()
        #print(x)
        for i in ids:
            c=0
            for a,b in zip(x,i):
                if a != b: 
                    c += 1
                if c > 1: 
                    #print(c)
                    break
            if c == 1:
                answer = list(x)
                r = 0
                for a,b in zip(x,i):
                    if a != b:
                        answer.pop(r)
                        break
                    r += 1
                print(''.join(answer))



if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))