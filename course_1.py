import pandas as pd
import numpy as np

print(pd.__version__)  # 2.1.0

# create a serie

data = pd.Series([2.3, 33, 45, 49.3])
print(data)

"""
0     2.3
1    33.0
2    45.0
3    49.3
dtype: float64
"""
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(type(data))  # <class 'pandas.core.series.Series'>

# access the values of the series

print(data.values)  # [0.25 0.5  0.75 1.  ]

# access the indexes of the data serie

print(data.index)  # RangeIndex(start=0, stop=4, step=1)

# access the values of the data serie through the indexes

print(data[0])  # 0.25
print(data[1])  # 0.5

print(data[1:3])

"""
1    0.50
2    0.75
dtype: float64
"""

# numpy array

"""
Numpy Array has an implicitly defined integer index used to access the values.
The Pandas `Series` has an explicitly defined `index` associated with the values.


This explicit index definition gives the Series object additional capabilities.
The index does not need an integer value mandatory, but can consist of values of
any desired type, as we can see in the following example:
"""

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
print(data)

"""
a    0.25
b    0.50
c    0.75
d    1.00
dtype: float64
"""

print(data['b'])  # 0.5

# use non contiguous indexes

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=[2, 5, 3, 7])
print(data)

"""
2    0.25
5    0.50
3    0.75
7    1.00
dtype: float64
"""

# Series as specialized dictionaries

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}


# transform the dictionary into a pandas series
population = pd.Series(population_dict)

print(population['California'])  # 38332521

# Unlike a dictionary, the ``Series`` also supports array-style
# operations such as slicing:

print(population['California':'Illinois'])

"""
California    38332521
Texas         26448193
New York      19651127
Florida       19552860
Illinois      12882135
dtype: int64
"""

# Pandas DataFrame


"""
A ``DataFrame`` is an analog of a two-dimensional array with both flexible row indices
and flexible column names.
Just as you might think of a two-dimensional array as an ordered sequence of aligned 
one-dimensional columns, you can think of a ``DataFrame`` as a sequence of aligned 
``Series`` objects.
Here, by "aligned" we mean that they share the same index.

To demonstrate this, let's first construct a new ``Series`` listing the area of each
of the five states discussed in the previous section:

"""

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
print(area)

"""
California    423967
Texas         695662
New York      141297
Florida       170312
Illinois      149995
dtype: int64
"""

# create a dataframe with the series area_dict and population

states = pd.DataFrame({'population': population,
                       'area': area})
print(states)

"""
            population    area
California    38332521  423967
Texas         26448193  695662
New York      19651127  141297
Florida       19552860  170312
Illinois      12882135  149995
"""

# a dataframe has the index attribute

print(states.index)

# Index(['California', 'Texas', 'New York', 'Florida', 'Illinois'], dtype='object')

# the columns attribute

print(states.columns)
# Index(['population', 'area'], dtype='object')


"""
There are some functions and attributes that allow us to observe basic information 
about the data stored in a `DataFrame` object:

1. `DataFrame.head()` -> returns the content of the first 5 rows, by default
2. `DataFrame.tail()` -> returns the content of the last 5 rows, by default
3. `DataFrame.shape` -> returns a tuple of the form (num_rows, num_columns)
4. `DataFrame.columns` -> returns the name of the columns
5. `DataFrame.index` -> returns the index of the rows

Using `` `data.head ()` `` and `` `data.tail ()` `` we can see the content of the data.
"""

# the first 2 rows
print(states.head(2))

"""
            population    area
California    38332521  423967
Texas         26448193  695662
"""

# the last 2 rows
print(states.tail(2))

"""
          population    area
Florida     19552860  170312
Illinois    12882135  149995
"""

# Pandas `Index` Object
# like a numpy array

ind = pd.Index([2, 3, 5, 7, 11])
print(ind)  # Index([2, 3, 5, 7, 11], dtype='int64')

"""
One difference between ``Index`` objects and `Numpy` arrays is that
indices are **immutable**. That is, they cannot be modified via the
normal means, which will cause an error
"""

# some common attributes between index and numpy array

print(' Size:', ind.size, '\n',
      'Shape:', ind.shape, '\n',
      'Dimension:', ind.ndim, '\n',
      'Data type:', ind.dtype)

"""
Index([2, 3, 5, 7, 11], dtype='int64')
 Size: 5
 Shape: (5,)
 Dimension: 1
 Data type: int64
"""

#  Indexers: loc, iloc for `Series`

data = pd.Series(['Hello', 'DPhi', 'world'], index=['a', 'b', 'c'])

# .loc attribute ( explicit indexing)
print(data.loc['a'])  # Hello

# slicing
print(data.loc['a':'c'])
"""
a    Hello
b     DPhi
c    world
dtype: object
"""

# .iloc[]
print(data.iloc[1])
print(data.iloc[1:3])

"""
    
Exercise 1

Consider the following lists:
```
lst1 = [1, 2, 3, 5, 8]
lst2 = [8, 5, 3, 2, 1]
```

1. Create and display two individual `Series` objects `s1` and `s2` from the data available on each list.


2. Perform the following operations with the two series (element-wise):
    1. Add `s1` and s2 and store the result in a new variable `s3_add`
    2. Subtract `s2` from `s1` and store the result in a new variable `s3_sub`
    3. Multiply `s1` and `s2` and store the result in a new variable `s3_mul`
    4. Divide `s1` by `s2` and store the result in a new variable `s3_div`
    
"""

lst1 = [1, 2, 3, 5, 8]
lst2 = [8, 5, 3, 2, 1]

# 1. Create and display two individual `Series` objects `s1` and `s2`
# from the data available on each list.

s1 = pd.Series(lst1)
s2 = pd.Series(lst2)
print(s1)
print(s2)

#  2.1. Add `s1` and s2 and store the result in a new variable `s3_add`
s3_add = s1 + s2
print(s3_add)

"""
0    9
1    7
2    6
3    7
4    9
dtype: int64
"""

# 2.2. Subtract `s2` from `s1` and store the result in a new variable `s3_sub`
s3_sub = s2 - s1
print(s3_sub)

"""
0    7
1    3
2    0
3   -3
4   -7
dtype: int64
"""

# 2.3. Multiply `s1` and `s2` and store the result in a new variable `s3_mul`
s3_mul = s1 * s2
print(s3_mul)

"""
0     8
1    10
2     9
3    10
4     8
dtype: int64
"""

"""
Exercise 2

Consider the following `Series` object:
```
0    45000
1    37872
2    57923
3    68979
4    78934
5    69897
6    56701
Name: Amazon_Reviews, dtype: int64
```
1. Create and display the `Amazon_Reviews` Series.

2. Get the last three values from `Amazon_Reviews` using negative indexing.
"""
# 1. Create and display the `Amazon_Reviews` Series.
Amazon_Reviews = pd.Series([45000, 37872, 57923, 68979, 78934, 69897, 56701])
print(Amazon_Reviews)
"""
0    45000
1    37872
2    57923
3    68979
4    78934
5    69897
6    56701
dtype: int64
"""

# 2. Get the last three values from `Amazon_Reviews` using negative indexing.
print(Amazon_Reviews[-1:-4:-1])

"""
6    56701
5    69897
4    78934
dtype: int64

or
"""
print(Amazon_Reviews[-3::])
"""
4    78934
5    69897
6    56701
dtype: int64
"""

"""
Exercise 3

Consider the following dictionary which is relating the area in sq units of some USA states: 
```
    area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
```

1. Create a `Series` using the given dictionary
2. Extract areas for 'Texas', 'New York',  and 'Florida' from the created series
"""
# 1. Create a `Series` using the given dictionary
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
areas = pd.Series(area_dict)

# 2. Extract areas for 'Texas', 'New York',  and 'Florida' from the created series
print(areas[['Texas', 'New York', 'Florida']])

"""
Texas       695662
New York    141297
Florida     170312
dtype: int64
"""

# Data Selection in `DataFrame`

area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area': area, 'pop': pop})

print(data)

"""
              area       pop
California  423967  38332521
Texas       695662  26448193
New York    141297  19651127
Florida     170312  19552860
Illinois    149995  12882135


The individual ``Series`` that make up the columns of the ``DataFrame``
can be accessed via dictionary-style indexing of the column name:
"""

print(data['pop'])

"""
California    38332521
Texas         26448193
New York      19651127
Florida       19552860
Illinois      12882135
Name: pop, dtype: int64

We can also access with attribute style notation:
"""

print(data.area)

"""
California    423967
Texas         695662
New York      141297
Florida       170312
Illinois      149995
Name: area, dtype: int64


Modify the dataframe by creating a new column from the two other
"""

data['density'] = data['pop'] / data.area
print(data)
"""
              area       pop     density
California  423967  38332521   90.413926
Texas       695662  26448193   38.018740
New York    141297  19651127  139.076746
Florida     170312  19552860  114.806121
Illinois    149995  12882135   85.883763
"""

print(data.values)
"""
[[4.23967000e+05 3.83325210e+07 9.04139261e+01]
 [6.95662000e+05 2.64481930e+07 3.80187404e+01]
 [1.41297000e+05 1.96511270e+07 1.39076746e+02]
 [1.70312000e+05 1.95528600e+07 1.14806121e+02]
 [1.49995000e+05 1.28821350e+07 8.58837628e+01]]
"""

print(data.loc[:'Florida', :'pop'])

"""
              area       pop
California  423967  38332521
Texas       695662  26448193
New York    141297  19651127
Florida     170312  19552860
"""

print(data.iloc[:3, :2])

"""
Exercise 4

Consider below DPhi Bootcamp's information about different batches:

```
Total_Candidates = {'absolute_beginners': 785, 'beginners': 825, 'intermediat_advanced': 602} # this is true data
Active_Candidates = {'absolute_beginners': 500, 'beginners': 425, 'intermediat_advanced': 300}  # this is hypothetical data
```
    
1. Create a Pandas `DataFrame` using above information (name your Dataframe as `DPhi`)
2. Get all the columns in DPhi.
3. Get the information of total candidates present in each batches using dictionary-style 
    indexing.
4. Find the number of candidates for each batches who are not active and add this 
    information to the dataframe DPhi.
5. Also, find the percent of candidates that are active in each batches and add this
    information to the `DPhi` dataframe (hint: $percent = (active / total)* 100$)
6. Get all the batches where percentage of active candidates are greater than 60%
"""

Total_Candidates = {'absolute_beginners': 785, 'beginners': 825,
                    'intermediat_advanced': 602}  # this is true data
Active_Candidates = {'absolute_beginners': 500, 'beginners': 425,
                     'intermediat_advanced': 300}  # this is hypothetical data

# 1. Create a Pandas `DataFrame` using above information (name your Dataframe as `DPhi`)

DPhi = pd.DataFrame({'total_candidates': pd.Series(
    Total_Candidates), 'active_candidates': pd.Series(Active_Candidates)})

print(DPhi)

"""
                      total_candidates  active_candidates
absolute_beginners                 785                500
beginners                          825                425
intermediat_advanced               602                300
"""

# 2. Get all the columns in DPhi.
print(DPhi.columns) # Index(['total_candidates', 'active_candidates'], dtype='object')

# 3. Get the information of total candidates present in each batches using 
# dictionary-style indexing.
print(DPhi['total_candidates'])
"""
absolute_beginners      785
beginners               825
intermediat_advanced    602
Name: total_candidates, dtype: int64
"""

# 4. Find the number of candidates for each batches who are not active and add this 
#    information to the dataframe DPhi.

DPhi['non_active_candidates'] = DPhi.total_candidates - DPhi.active_candidates
print(DPhi)

"""
                      total_candidates  active_candidates  non_active_candidates
absolute_beginners                 785                500                    285
beginners                          825                425                    400
intermediat_advanced               602                300                    302
"""

# 5. Also, find the percent of candidates that are active in each batches and add this
#   information to the `DPhi` dataframe (hint: $percent = (active / total)* 100$)
DPhi['percent_active'] = (DPhi.active_candidates / DPhi.total_candidates)* 100

print(DPhi)

"""
                      total_candidates  active_candidates  non_active_candidates  percent_active
absolute_beginners                 785                500                    285       63.694268
beginners                          825                425                    400       51.515152
intermediat_advanced               602                300                    302       49.833887
"""

# 6. Get all the batches where percentage of active candidates are greater than 60%
print(DPhi['percent_active'] > 60)
"""
absolute_beginners       True
beginners               False
intermediat_advanced    False
Name: percent_active, dtype: bool
"""

print(DPhi[DPhi['percent_active'] > 60])

"""
                    total_candidates  active_candidates  non_active_candidates  percent_active
absolute_beginners               785                500                    285       63.694268
"""

# Subsetting a DataFrame

# Subsetting a `DataFrame` is a way of filtering which allows to extract portions of
# interest. Subsetting can be done using comparison operators and logical operators 
# inside a pair of square brackets `[]` as shown in the following:

print(data[data['density'] > 100])
"""
            area       pop     density
New York  141297  19651127  139.076746
Florida   170312  19552860  114.806121
"""

print(data['density'] > 100)
"""
California    False
Texas         False
New York       True
Florida        True
Illinois      False
Name: density, dtype: bool
"""

print(data[(data['density'] > 100) & (data['area'] < 150000)])

"""
            area       pop     density
New York  141297  19651127  139.076746
"""

print(data[(data['density'] < 90) | (data['density'] > 120)])

"""
            area       pop     density
Texas     695662  26448193   38.018740
New York  141297  19651127  139.076746
Illinois  149995  12882135   85.883763
"""

# Data Wrangling
# 1   - structure
# 2   - clean
# 3   - enrich

print(pd.Series([1, np.nan, 2, None]))
"""
0    1.0
1    NaN
2    2.0
3    NaN
dtype: float64
"""

"""
5.2. Operations on Missing Values

There are several useful methods for detecting, removing, and replacing missing values
in Pandas data structures:

- ``isnull()``: generates a boolean mask indicating missing values
- ``notnull()``: generates a boolean mask of non-missing values. Is the opposite of 
    ``isnull()``.
- ``dropna()``: returns a filtered version of the data, without missing values.
- ``fillna()``: returns a copy of the data with missing values filled or imputed 
    with a desired strategy.

Let's review some examples of the first two functions `isnull()` and `notnull()`:
"""
data = pd.Series([1, np.nan, 'hello', None])
print(data)
"""
0        1
1      NaN
2    hello
3     None
dtype: object
"""


# mask of null values
print(data.isnull())
"""
0    False
1     True
2    False
3     True
dtype: bool
"""
# mask of not null values
print(data.notnull())
"""
0     True
1    False
2     True
3    False
dtype: bool
"""

# fileter no missing values but the dataframe id not modified
print(data[data.notnull()])
"""
0        1
2    hello
dtype: object
"""
# remove missing values
print(data.dropna())

"""
0        1
2    hello
dtype: object
"""
# More Options

df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])
print(df)
"""
     0    1  2
0  1.0  NaN  2
1  2.0  3.0  5
2  NaN  4.0  6
"""

# More option
# drop all columns with missing values

print(df.dropna(axis='columns'))
"""
   2
0  2
1  5
2  6
"""
# to avoid throwing good data with the NaN values, use the how or thresh parameters

"""
df = pd.DataFrame([[1,      np.nan, 2, np.nan],
                   [2,      3,      5, np.nan],
                   [np.nan, 4,      6, np.nan]])
df
"""

df = pd.DataFrame([[1,      np.nan, 2, np.nan],
                   [2,      3,      5, np.nan],
                   [np.nan, 4,      6, np.nan]])
print(df)

"""
     0    1  2   3
0  1.0  NaN  2 NaN
1  2.0  3.0  5 NaN
2  NaN  4.0  6 NaN
"""
print(df.dropna(axis='columns', how='all'))
"""
     0    1  2
0  1.0  NaN  2
1  2.0  3.0  5
2  NaN  4.0  6
"""
print(df.dropna(axis='columns', thresh=0))

# Treatment for missing values

data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
print(data)
"""
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
"""

# replace the missing values of the series with 0

print(data.fillna(0))
"""
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
"""
# We can specify a forward-fill to propagate the previous value forward:

print(data.ffill())
"""
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
"""
# backward-fill to propagate the next value backward

print(data.bfill())
"""
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
"""

"""
For ``DataFrame`` objects the options are similar, but we can also specify an
``axis`` along which the fills take place:
"""
print(df)

"""
     0    1  2   3
0  1.0  NaN  2 NaN
1  2.0  3.0  5 NaN
2  NaN  4.0  6 NaN
"""

# along the columns
print(df.ffill(axis=1))
"""
     0    1    2    3
0  1.0  1.0  2.0  2.0
1  2.0  3.0  5.0  5.0
2  NaN  4.0  6.0  6.0
"""

# along the rows
print(df.ffill(axis=0))
"""
     0    1  2   3
0  1.0  NaN  2 NaN
1  2.0  3.0  5 NaN
2  2.0  4.0  6 NaN
"""

# `Pandas` String Operations

"""
When a `Pandas` object stores string data, `Pandas` provides certain operations
to facilitate its manipulation.
"""

data = ['peter', 'Paul', 'MARY', 'gUIDO']
[s.capitalize() for s in data]

print(data) # can't capitalize but no error
names = pd.Series(data)
print(names)
# capitalize
names = names.str.capitalize()
print(names)
"""
0    Peter
1     Paul
2     Mary
3    Guido
dtype: object
"""
# more methods on strings in dataframe
# note that we access strings through the str attribute of the dataframe
monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam',
                   'Eric Idle', 'Terry Jones', 'Michael Palin'])
print(monte)
"""
0    Graham Chapman
1       John Cleese
2     Terry Gilliam
3         Eric Idle
4       Terry Jones
5     Michael Palin
dtype: object
"""
print(monte.str.lower())
"""
0    graham chapman
1       john cleese
2     terry gilliam
3         eric idle
4       terry jones
5     michael palin
dtype: object
"""
# calculate the lentghs of strings
print(monte.str.len())
"""
0    14
1    11
2    13
3     9
4    11
5    13
dtype: int64
"""
# Parse values to string and calculates a mask of string values starting by 'J'
print(monte.str.startswith('J'))
"""
0    False
1     True
2    False
3    False
4    False
5    False
dtype: bool
"""

## concat series : pd.conca()

ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
print(pd.concat([ser1, ser2], axis=0))

"""
1    A
2    B
3    C
4    D
5    E
6    F
dtype: object
"""
print(pd.concat([ser1, ser2], axis=1))

"""
     0    1
1    A  NaN
2    B  NaN
3    C  NaN
4  NaN    D
5  NaN    E
6  NaN    F




Now let's look at a function defined by us, which allows us to evidence the data of 
multiple `DataFrame` objects. It is not necessary for now to have a complete 
understanding of the following function. What is important at this time is knowing 
how to use it.
"""

class Display(object):
    """Display HTML representation of multiple objects"""
    
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)
        
        
"""
create a `DataFrame` quickly using *Dictionary Comprehension*. This function transforms
an input string into a square array that is later converted to a `DataFrame` where the 
column names are each of the characters in the string
"""

def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)



# example DataFrame
print(make_df('ABC', range(3)))

"""
    A   B   C
0  A0  B0  C0
1  A1  B1  C1
2  A2  B2  C2
"""

# concatenate higher-order object like dataframes
df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
print(Display('df1', 'df2', 'pd.concat([df1, df2])'))

"""
df1
    A   B
1  A1  B1
2  A2  B2

df2
    A   B
3  A3  B3
4  A4  B4

pd.concat([df1, df2])
    A   B
1  A1  B1
2  A2  B2
3  A3  B3
4  A4  B4
"""


df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
print(Display('df3', 'df4', "pd.concat([df3, df4], axis=1)"))

"""
df3
    A   B
0  A0  B0
1  A1  B1

df4
    C   D
0  C0  D0
1  C1  D1

pd.concat([df3, df4], axis=1)
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
"""