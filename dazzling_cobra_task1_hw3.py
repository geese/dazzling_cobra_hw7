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
            record_list.append(line_dc.split(','))
    return record_list


# Main function
def main():
    getMinivanTestFile('http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv')
    return


if __name__ == '__main__':
    # Call Main
    main()

    exit(0)










