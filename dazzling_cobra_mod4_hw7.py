#!/usr/bin/env python3
"""
A program which takes zipcodes from an input file and converts the zipcodes
into a barcode
Displays the zipcode, the check digit, and the barcode
"""
import sys
import dazzling_cobra_mod3_hw7 as dazzle
from urllib.request import urlopen

def help():
    """
    The usage is: dazzling_cobra_mod4_hw3
    """

def getZipCodes(url):
    """
    Decodes the information passed in by the url and strips the newline
    Args:
        A url which links to an input file
    Returns:
        Stripped/Decoded values
    """
    theZips = []
    with urlopen(url) as theZipCodes:
        for line in theZipCodes:
            line_dc = line.decode('utf-8').strip('\n')
            theZips.append(line_dc)
    return theZips








# Main function
def main():
    """
    Takes the input file from the url and formats it into a bar code
    using an imported function named dazzling_cobra_mod3_hw
    Prints out the zipcode read from the input file, the check digit,
    and also the bar code based off of the zipcode
    """
    zipList = getZipCodes('http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt')
    for zip in zipList:
        nzip = list(zip)
        i = 0
        for word in nzip: 
            nzip[i] = int(nzip[i])
            i += 1
        chksum = sum(nzip)
        if chksum % 10 != 0:
            rem = chksum % 10
            nzip.append(10 - rem)
        else:
            nzip.append(0)
        print("Please input a zip code: ",zip)
        dazzle.printBarCode(nzip)
    return


if __name__ == '__main__':
    # Call Main
    main()
    
    exit(0)
