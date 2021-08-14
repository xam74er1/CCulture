from datetime import date

import pandas as pd


def diff_days(csv_contents: str) -> int:
    df = pd.DataFrame([x.split(';') for x in str.split('\n')])
    print (df);
    df['Date'] = pd.to_datetime(df['Date'])
    column = df['Date'];
    max_value = column.max()
    min_value = column.min()
    return (max_value - min_value).dt.days;

#load csv_contents into a dataframe -- (b) converte the collom 'date' into date -- (c) find the earliest and the oldest date -- (d) give the difference in day bettewen the oldest and the earliest date


import itertools
from typing import List


def count_arrangements(sizes: List[int]) -> int:
    if len(sizes) < 2:
        return 0
    # calculate how many arrangements will be when the first bucket is equal to the second
    total = 0
    for i in range(1, len(sizes)):
        total += (i + 1) * (len(sizes) - i)
    # calculate how many arrangements will be when the first bucket is bigger than the second
    for permutation in itertools.permutations(sizes):
        if permutation[0] > permutation[1]:
            total += 1
    return total


# Examples


'''
Compte le nombre de valleure unique dans la liste 
'''


def count_unique_ways(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    total = 0
    # calculate how many arrangements will be when the first bucket is equal to the second
    for i in range(1, len(nums)):
        total += (i + 1) * (len(nums) - i)
    # calculate how many arrangements will be when the first bucket is bigger than the second
    for permutation in itertools.permutations(nums):
        if permutation[0] > permutation[1]:
            total += 1
    return total


print(count_arrangements(count_unique_ways([1, 3, 1])))
print(count_arrangements([1, 2]))