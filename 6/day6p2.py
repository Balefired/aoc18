#!/usr/bin/python3 -tt
from scipy.spatial.distance import cdist
import re
from operator import itemgetter
import numpy as np
import pandas as pd
from collections import Counter
import operator


def main():
    coords = []
    with open('input.sdx', 'r') as ifile:
        for line in ifile:
            t = re.findall(r'\d+',line)
            t = [int(x) for x in t]
            coords.append(tuple(t))
        
        maxX = max(coords,key=itemgetter(0))[0]
        maxY = max(coords,key=itemgetter(1))[1]
        df = pd.DataFrame(np.nan,index=np.arange(maxY+1), columns=np.arange(maxX+1))
        for index, row in df.iterrows():
            col = row.name
            for i,v in row.iteritems():
                check = cdist([(i,col)],coords,'cityblock')[0]
                if sum(check) < 10000:
                    df[i][col] = 1
                else:
                    df[i][col] = 0

        print(df.values.sum())


        
        



if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))