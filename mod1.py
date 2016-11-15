"""
Module to control the sliding doors on a van.
Args:
    Input ctrl containing values for ctrl{}
Returns:
    Whether the left right both or no doors opened based on input file.
"""
#!/usr/bin/env python3
import sys

def ctrl(values_dict):
    """
    Module to control the sliding doors on a van.
    Args:
        Input ctrl containing values for ctrl{}
    Returns:
        Whether the left right both or no doors opened based on input file.
    """
    #v = { "LD":0, "RD":0, "CL":0, "ML":0, "LI":0, "LO":0, "RI":0, "RO":0, "GS":"0" }
    v = values_dict
    
    if v['GS'] not in ['P','N','D','1','2','3','R']:
        return "Invalid Record: Both doors stay closed."
    
    #Check to see if master lock is enabled and vehicle is in park
    if v{"ML"} == 1 or v{"GS"} != "P":
        print("Neither Door Opens.")
    #Doors open without child lock
    elif v{"CL"} == 0:
        if (v{"LD"} == 1 or v{"LI"} == 1 or v{"LO"} == 1) and (v{"RD"} == 1 or v{"RI"} == 1 or v{"RO"} == 1):
            print("Both Doors Open.")
        elif (v{"RD"} == 1 or v{"RI"} == 1 or v{"RO"} == 1) and (v{"LD"} == 0 or v{"LI"} == 0 or v{"LO"} == 0):
            print("Right Door Opens.")
        elif (v{"LD"} == 1 or v{"LI"} == 1 or v{"LO"} == 1) and (v{"RD"} == 0 or v{"RI"} == 0 or v{"RO"} == 0):
            print("Left Door Opens.")
        else:
            print("Neither Door Opens.")
    #doos open with child lock
    elif v{"CL"} == 1:
        if (v{"LD"} == 1 or v{"LO"} == 1) and (v{"RD"} == 1 or v{"RO"} == 1):
            print("Both Doors Open.")
        elif (v{"RD"} == 1 or v{"RO"} == 1) and (v{"LD"} == 0 or v{"LO"} == 0):
            print("Right Door Opens.")
        elif (v{"LD"} == 1 or v{"LO"} == 1) and (v{"RD"} == 0 or v{"RO"} == 0) :
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

