# import pandas as pd

# read_file=pd.read_excel("card_family_data.xlsx")

# read_file.to_csv('Test.csv',index=False);
import csv
from functools import cmp_to_key

family_list=[]
family_list_header=[]
RELATIONS_SORTING_ORDER = ['स्वयं', 'पत्नी', 'बेटी', 'बेटा', 'पिता', 'माँ']
RELATION_COL = 4

with open('Test.csv','r',encoding='utf-8') as f:
    reader=csv.reader(f)

    for line in reader:
        family_list.append(line);

family_list_header=family_list.pop(0);

def compare(v1,v2):
    res=-1
    for i in range(len(RELATIONS_SORTING_ORDER)):
        if v1[RELATION_COL]==RELATIONS_SORTING_ORDER[i]:
            break;
        elif v2[RELATION_COL]==RELATIONS_SORTING_ORDER[i]:
            res=1;
            break;
    return res;

family_list.sort(key=cmp_to_key(compare))
print(family_list_header)
print(family_list)

