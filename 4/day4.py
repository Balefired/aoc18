#!/usr/bin/python3 -tt
import re
import pandas as pd
import numpy as np
import operator

def main():
    header = ['day', 'time', 'status']
    df = pd.DataFrame(columns=header)
    with open('input.sdx', 'r+') as ifile:
        for line in ifile: 
            x = re.split(r'\] | +', line[6:-1])
            df.loc[len(df)] = [x[0], x[1], x[3]]
    df['month'], df['day'] = df['day'].str.split('-').str
    df.sort_values(by=['month', 'day','time'],inplace=True)
    df.reset_index(drop=True, inplace=True)
    df['time_s'] = df['time'].shift(-1)
    df.fillna(value='00:60', inplace=True)
    df['time_s'] = df.apply(lambda row: '00:60' if row['time_s'][:2] == '23' else row['time_s'], axis=1)
    df['sleep'] = df.apply(lambda row: (1+int(row['time_s'][3:]) - int(row['time'][3:])) if 'asleep' == row['status'] else 0, axis = 1)
    df['assign'] = df.apply(lambda row: row['status'] if '#' in row['status'] else np.nan, axis=1)
    df.fillna(method='ffill', inplace=True)
    counts = {}
    for row in df.itertuples():
        if row.status == 'asleep':
            if row.assign in counts:
                counts[row.assign] += row.sleep
            else:
                counts[row.assign] = row.sleep

    sleeper = max(counts.items(), key=operator.itemgetter(1))[0]
    df2 = df[df['assign'] == sleeper]
    answer = df2.loc[df2['sleep'].idxmax()]
    print(int(answer.assign[1:])*answer.sleep)
              

    

if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))