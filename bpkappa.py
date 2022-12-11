#!usr/bin/env python3
import pandas as pd
import numpy as np
ra1 = pd.read_excel('Excel for Reliability.xlsx', 1)
ra2 = pd.read_excel('Excel for Reliability.xlsx', 2)

def give_bpkappa(first, second):
    coff = 3
    dis = 0
    agree = 0
    for i in range(len(first)):
        if first[i] == second[i]:
            agree = agree + 1
        else:
            dis = dis + 1 
    return round(((agree/(agree + dis)) - (1/coff))/(1 - (1/coff)), 2)

def all_col_same(arr):
    for thing in arr:
        if thing == False:
            return False
    return True
    
assert all_col_same(ra1.columns == ra2.columns), "Different Column Names For The Two Sheets"    

bpkappa = {}
for col in ra1.columns:
    bpkappa[col] = (give_bpkappa(ra1[col], ra2[col]))
bpkappa
df = pd.DataFrame(bpkappa, index=[0])
df.to_excel('Codes with bpkappa.xlsx')

