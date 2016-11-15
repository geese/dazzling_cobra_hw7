#!/usr/bin/env python3
"""

"""
import sys
import dazzling_cobra_mod3_hw3 as dazzle
from urllib.request import urlopen


def getZipCodes(url):
    theZips = []
    with urlopen(url) as theZipCodes:
        for line in theZipCodes:
            line_dc = line.decode('utf-8').strip('\n')
            theZips.append(line_dc)
    return theZips








# Main function
def main():
    zips = getZipCodes('http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt')
    for zip in zips:
        dazzle.printBarCode(zip)
        print('\n')
    return


if __name__ == '__main__':
    # Call Main
    main()
    
    exit(0)










