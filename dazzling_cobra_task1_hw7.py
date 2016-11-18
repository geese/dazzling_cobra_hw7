#!/usr/bin/env python3
"""
Ugh, where to start...
"""
import sys
from urllib.request import urlopen


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
            value_dict[header_record[index]] = value
            index += 1
        values_dicts.append(value_dict)
    return values_dicts


# Main function
def main():
    records = getMinivanTestFile('http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv')
    dicts = makeInputValuesDicts(records)
    print(dicts)
    return


if __name__ == '__main__':
    # Call Main
    main()

    exit(0)










