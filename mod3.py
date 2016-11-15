"""
Translate a decimal zipcode into a barcode.
Args:
    User will be asked to enter a zipcode.
Returns:
    Barcode format of user input zipcode.
"""
#!/usr/bin/env python3
import sys

def zipcode():
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
    print(zip)


#main function
def main():
    """
    Test function
    """
    zipcode()
    zipcode()
    zipcode()


if __name__ == "__main__":
    #Call Main
    main()

    exit(0)

