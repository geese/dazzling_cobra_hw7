#!/usr/bin/env python3
"""
Translate a decimal zipcode into a barcode.
Args:
    User will be asked to enter a zipcode.
Returns:
    Barcode format of user input zipcode.
"""
import sys


barcode_table = {1:'00011', 2:'00101',3:'00110', 4:'01001', 5:'01010', 
        6:'01100', 7:'10001', 8:'10010', 9:'10100', 0:'11000'}


def printDigit():
    """
    Take zipcode from user input than prepare it for printing in barcode format.
    Args: None
    Returns:
        zipcode
    """
    zip = list(input("Please input a zip code: "))
    i = 0
    for word in zip:
        zip[i] = int(zip[i])
        i += 1
    chksum = sum(zip)
    if chksum % 10 != 0:
        rem = chksum % 10
        zip.append(10 - rem)
    else:
        zip.append(0)
    zipString = ''
    for digit in zip:
        zipString += str(digit)
    print('zip: {}, check digit: {}'.format(zipString[0:-1], zipString[-1:]))
    return zip


def printBarCode(zipCode):
    """
    Prints decimal zipcode and check value as a barcode
    using psuedo-binary. 
    Output Format:
        | xxxxx xxxxx xxxxx xxxxx xxxxx xxxxx |
        where x = either "|" = 1 or ":" = 0
    Args:
        Decimal zipcode with check number
    Returns:
        6 decimal digits expressed in psuedo-binary barcode
    """
    zip = printDigit(zipCode)
    barcode = '|'
    for digit in zip:
        for bit in barcode_table[digit]:
            barcode += ':' if bit == '0' else '|'
    barcode += '|'
    print(barcode)


#main function
def main():
    """
    Test function
    """
    zip = input("Please input a zip code: ")
    printBarCode(zip)


if __name__ == "__main__":
    #Call Main
    main()

    exit(0)
