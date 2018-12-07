#!/usr/bin/python3 -tt
import re

def main():
    orig = ''
    with open('input.sdx', 'r') as ifile:
        orig = ifile.read().replace('\n','')
    x=orig
    y=True
    lalpha = 'abcdefghijklmnopqrstuvwxyz'
    ualpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha = list(zip(list(lalpha),list(ualpha)))
    print(alpha)
    nalpha = []
    for i in alpha:
        nalpha.append(i[0]+i[1])
        nalpha.append(i[1]+i[0])
    print(nalpha)
    toomuch = 53
    tmcheck = 0
    length = len(x)
    while True:
        if length == len(x):
            tmcheck += 1
            if tmcheck > toomuch:
                break
        if length != len(x):
            length = len(x)
        for i in nalpha:
            x = re.sub(i,'',x)
    print('part 1 answer')
    print(len(x))
    p2ans = 100000
    x=''
    for i in alpha:
        x=orig
        t = re.sub(i[0],'',x)
        t = re.sub(i[1],'',t)
        while True:
            if length == len(t):
                tmcheck += 1
                if tmcheck > toomuch:
                    break
            if length != len(t):
                length = len(t)
            for i in nalpha:
                t = re.sub(i,'',t)
        if len(t) < p2ans:
            p2ans = len(t)

    print('part 2 answer')
    print(p2ans)






if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))