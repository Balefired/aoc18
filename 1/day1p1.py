#!/usr/bin/python3 -tt

def main():
    x = 0
    with open('input.sdx', 'r+') as ifile:
        for line in ifile: x += int(line)
    print(x)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))