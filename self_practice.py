import pandas as pd


def load_csv(filepath):
    data = []
    col = []
    checkcol = False
    with open(filepath) as f:
        for val in f.readlines():
            val = val.replace("\n", "")
            val = val.split(',')
            if checkcol is False:
                col = val
                checkcol = True
            else:
                data.append(val)
    df = pd.DataFrame(data=data, columns=col)
    return df


"""

1 - Load the CSV file into a variable - greenhouse_data
2 - Use the description function to understand how the data looks like
3 - Print its first 10 rows using head()
4 - Print its last 10 rows using tail()
5 - Check if there are any null values
7- Store the DataFrame to a CSV file named 'file2.csv'

"""

# 1 - Load the CSV file into a variable - greenhouse_data

greenhouse_data = pd.read_csv('./datasets/UNdata_Greenhouse_Gas.csv')

# 2 - Use the description function to understand how the data looks like

print(greenhouse_data.describe())

"""
              Year         Value
count  1204.000000  1.204000e+03
mean   2003.500000  5.280785e+05
std       8.081104  1.283749e+06
min    1990.000000  8.412655e+01
25%    1996.750000  3.093901e+04
50%    2003.500000  8.069707e+04
75%    2010.250000  4.392478e+05
max    2017.000000  7.369968e+06
"""

# 3 - Print its first 10 rows using head()

print(greenhouse_data.head(10))

"""
 Country or Area  Year          Value
0       Australia  2017  554126.561371
1       Australia  2016  546771.759767
2       Australia  2015  535173.674335
3       Australia  2014  524957.101167
4       Australia  2013  530433.518839
5       Australia  2012  540615.864772
6       Australia  2011  538280.611349
7       Australia  2010  537275.249361
8       Australia  2009  540913.370344
9       Australia  2008  537031.991695
"""

# 4 - Print its last 10 rows using tail()

print(greenhouse_data.tail(10))

"""
               Country or Area  Year         Value
1194  United States of America  1999  7.071461e+06
1195  United States of America  1998  7.032526e+06
1196  United States of America  1997  6.968462e+06
1197  United States of America  1996  6.907699e+06
1198  United States of America  1995  6.710067e+06
1199  United States of America  1994  6.624836e+06
1200  United States of America  1993  6.532070e+06
1201  United States of America  1992  6.424934e+06
1202  United States of America  1991  6.315615e+06
1203  United States of America  1990  6.371001e+06
"""

# 5 - Check if there are any null values

print(greenhouse_data.isnull().sum())

"""
               Country or Area  Year         Value
1194  United States of America  1999  7.071461e+06
1195  United States of America  1998  7.032526e+06
1196  United States of America  1997  6.968462e+06
1197  United States of America  1996  6.907699e+06
1198  United States of America  1995  6.710067e+06
1199  United States of America  1994  6.624836e+06
1200  United States of America  1993  6.532070e+06
1201  United States of America  1992  6.424934e+06
1202  United States of America  1991  6.315615e+06
1203  United States of America  1990  6.371001e+06
Country or Area    0
Year               0
Value              0
dtype: int64

No null values in any column
"""

# 7- Store the DataFrame to a CSV file named 'file2.csv'

greenhouse_data.to_csv('file2.csv')