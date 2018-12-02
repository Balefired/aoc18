#!/usr/bin/python3 -tt

def main():
    x = 0
    xlist=[]
    flag = True
    while flag:
        with open('input.sdx', 'r+') as ifile:
            for line in ifile: 
                x += int(line)
                if x not in xlist: 
                    xlist.append(x)
                elif x in xlist:
                    flag = False 
                    break

    print(x)

if __name__ == '__main__':
    main()