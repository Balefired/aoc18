#!/usr/bin/python3 -tt

def main():
    i = []
    x = 0
    xlist=set()
    flag = True

    with open('input.sdx', 'r+') as ifile:
        for line in ifile: i.append(int(line))

    print(i)

    while flag:
        for val in i: 
            x += val
            if x in xlist: 
                flag = False 
                break
            else:
                xlist.add(x)
                

    print(x)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))