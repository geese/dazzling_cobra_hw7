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
        a url for a csv file
    """
    with urlopen(url) as testFile:
        for line in testFile:
            print(line);



# Main function
def main():
    getMinivanTestFile('http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv')
    return


if __name__ == '__main__':
    # Call Main
    main()

    exit(0)










