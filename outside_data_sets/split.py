import pandas as pd

in_csv = 'input1.csv'
number_lines = sum(1 for row in (open(in_csv)))

rowsize = 50000

for i in range(1, number_lines, rowsize):
    df = pd.read_csv(in_csv, header=None,nrows=rowsize,skiprows=i)
    out_csv = 'Data_set_' + str(i) + '.csv'
    df.to_csv(out_csv,index=False, header=False, mode='a', chunksize=rowsize)
