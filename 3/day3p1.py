#!/usr/bin/python3 -tt
import pandas as pd
import numpy as np

def main():
    tempList = []
    header = ['id','left','top','wide','tall']
    with open('input.sdx', 'r+') as ifile:
        for line in ifile:
            x = line[:-1].split(' ')
            del x[1]
            x[0]=[int(x[0][1:])]
            x[1]=x[1][:-1]
            x[1] = x[1].split(',')
            x[2] = x[2].split('x')
            x = [int(y) for z in x for y in z]
            tempList.append(x)
        df = pd.DataFrame(tempList,columns=header)
        df['max width'] = df['left'] + df['wide']
        df['max len'] = df['top'] + df['tall']
        cloth = pd.DataFrame(0,index=np.arange(df['max len'].max()+1), columns=np.arange(df['max width'].max()+1))
        for row in df.itertuples():
            cloth.loc[row.top:(row.top+row.tall-1),row.left:(row.left+row.wide-1)]+=1
        print(cloth[cloth>1].count().sum())
        
            


    

if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))