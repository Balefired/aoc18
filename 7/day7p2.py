#!/usr/bin/python3 -tt

def main():
    ordSub = 4
    inst = []
    ans = ''
    with open('input.sdx', 'r+') as ifile:
        for line in ifile:
            x = line.split()
            inst.append((x[1],x[7]))
    
    workers = [[],[]]
    time = 0

    while True:
        
        print(time)
        print(inst)
        if len(inst) > 1:
            step1, step2 = zip(*inst)
            step1 = sorted(set(step1))
            print(step1)
            step2 = set(step2)
        elif len(inst) == 0:
            break
        else:
            step1 = [inst[0][0]]
            step2 = [inst[0][1]]
        if len(workers[0]) < 5:
            for val in step1:
                if val not in step2 and val not in workers[0]:
                    workers[0].append(val)
                    workers[1].append(ord(val)-ordSub)
        
        time += 1
        workers[1] = [x-1 for x in workers[1]]
        '''if len(inst) == 1:
            print(inst[0][1])
            break'''
        print(workers)
        for idx, val in enumerate(workers[1]):
            if val == 0:
                workers[1].pop(idx)
                if len(inst) > 1:
                    inst = [(s1,s2) for s1, s2 in inst if s1 != workers[0][idx]]
                elif inst[0][1] != 0:
                    inst = [(inst[0][1],0)]
                else:
                    inst=[]
                workers[0].pop(idx)
            

    '''while True:
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
                break'''
    print(ans)



if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))