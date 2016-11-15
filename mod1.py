"""
Module to control the sliding doors on a van.
Args:
    Input ctrl containing values for ctrl{}
Returns:
    Whether the left right both or no doors opened based on input file.
"""
#!/usr/bin/env python3
import sys

def ctrl(file):
    """
    Module to control the sliding doors on a van.
    Args:
        Input ctrl containing values for ctrl{}
    Returns:
        Whether the left right both or no doors opened based on input file.
    """
    ctrl = { "LD":0, "RD":0, "CL":0, "ML":0, "LI":0, "LO":0, "RI":0, "RO":0, "GS":"0" }
    
    #Check to see if master lock is enabled and vehicle is in park
    if ctrl{"ML"} == 1 or ctrl{"GS"} != "P":
        print("Neither Door Opens.")
    #Doors open without child lock
    elif ctrl{"CL"} == 0:
        if (ctrl{"LD"} == 1 or ctrl{"LI"} == 1 or ctrl{"LO"} == 1) and (ctrl{"RD"} == 1 or ctrl{"RI"} == 1 or ctrl{"RO"} == 1):
            print("Both Doors Open.")
        elif (ctrl{"RD"} == 1 or ctrl{"RI"} == 1 or ctrl{"RO"} == 1) and (ctrl{"LD"} == 0 or ctrl{"LI"} == 0 or ctrl{"LO"} == 0):
            print("Right Door Opens.")
        elif (ctrl{"LD"} == 1 or ctrl{"LI"} == 1 or ctrl{"LO"} == 1) and (ctrl{"RD"} == 0 or ctrl{"RI"} == 0 or ctrl{"RO"} == 0):
            print("Left Door Opens.")
        else:
            print("Neither Door Opens.")
    #doos open with child lock
    elif ctrl{"CL"} == 1:
        if (ctrl{"LD"} == 1 or ctrl{"LO"} == 1) and (ctrl{"RD"} == 1 or ctrl{"RO"} == 1):
            print("Both Doors Open.")
        elif (ctrl{"RD"} == 1 or ctrl{"RO"} == 1) and (ctrl{"LD"} == 0 or ctrl{"LO"} == 0):
            print("Right Door Opens.")
        elif (ctrl{"LD"} == 1 or ctrl{"LO"} == 1) and (ctrl{"RD"} == 0 or ctrl{"RO"} == 0) :
            print("Left Door Opens.")
        else:
            print("Neither Door Opens.")



#main function
def main():
    """
    Test function
    """
    pass


if __name__ == "__main__":
    #Call Main
    main()

    exit(0)

