#!/usr/bin/python3 -tt

def main():
    inst = []
    ans = ''
    with open('input.sdx', 'r+') as ifile:
        for line in ifile:
            x = line.split()
            inst.append((x[1],x[7]))
    
    
    while True:
        if len(inst) == 1:
            ans += ''.join(inst[0])
            break
        step1, step2 = zip(*inst)
        step1 = sorted(set(step1))
        step2 = set(step2)
        for val in step1:
            if val not in step2:
                ans += val
                inst = [(s1,s2) for s1, s2 in inst if s1 != val]
                break
    print(ans)



if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))