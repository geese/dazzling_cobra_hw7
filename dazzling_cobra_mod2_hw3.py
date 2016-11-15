#!/usr/bin/env python3
"""

"""
import sys
from urllib.request import urlopen
from dazzling_cobra_mod1_hw3 import ctrl

def getMinivanTestFile(url):
    """
    opens url and reads in a csv file of minivan testing records
    Args:
        A url for a csv file
    Returns: 
        A list of records from the csv file.  
        Each list element (record) is a list of input values.
    """
    record_list = []
    with urlopen(url) as testFile:
        for line in testFile:
            line_dc = line.decode('utf-8').strip('\n')
            record_list.append(line_dc.split(',')[1:])
    return record_list


def makeInputValuesDicts(record_list):
    # separate the header values from the input values
    header_record = record_list.pop(0)
    values_dicts = []

    for record in record_list:
        value_dict = {}
        index = 0
        for value in record:
            value_dict[header_record[index].strip(' ')] = value.strip(' ')
            index += 1
        values_dicts.append(value_dict)
    return values_dicts


def printRecords(values_dicts):
    for i in range(0,len(values_dicts)):
        print("Reading Record {}:".format(i+1))
        print("Left dashboard switch (0 or 1): {}".format(values_dicts[i]['LD']))
        print("Right dashboard switch (0 or 1): {}".format(values_dicts[i]['RD']))
        print("Child lock switch (0 or 1): {}".format(values_dicts[i]['CL']))
        print("Master unlock switch (0 or 1): {}".format(values_dicts[i]['ML']))
        print("Left inside handle (0 or 1): {}".format(values_dicts[i]['LI']))
        print("Left outside handle (0 or 1): {}".format(values_dicts[i]['LO']))
        print("Right inside handle (0 or 1): {}".format(values_dicts[i]['RI']))
        print("Right outside handle (0 or 1): {}".format(values_dicts[i]['RO']))
        print("Gear shift position (P, N, D, 1, 2, 3 or R): {}".format(values_dicts[i]['GS']))
        print(ctrl(values_dicts[i]))
        print("\n")


# Main function
def main():
    records = getMinivanTestFile('http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv')
    dicts = makeInputValuesDicts(records)
    printRecords(dicts)
    return


if __name__ == '__main__':
    # Call Main
    main()

    exit(0)










