"""
"""
#!/usr/bin/env python3
import sys

def ctrl():
    file = { "LD":0, "RD":0, "CL":0, "ML":0, "LI":0, "LO":0, "RI":0, "RO":0, "GS":"0" }
    
    #Check to see if master lock is enabled and vehicle is in park
    if file{"ML"} == 1 or file{"GS"} != "P":
        print("Neither Door Opens.")
    #Doors open without child lock
    elif file{"CL"} == 0:
        if (file{"LD"} == 1 or file{"LI"} == 1 or file{"LO"} == 1) and (file{"RD"} == 1 or file{"RI"} == 1 or file{"RO"} == 1):
            print("Both Doors Open.")
        elif (file{"RD"} == 1 or file{"RI"} == 1 or file{"RO"} == 1) and (file{"LD"} == 0 or file{"LI"} == 0 or file{"LO"} == 0):
            print("Right Door Opens.")
        elif (file{"LD"} == 1 or file{"LI"} == 1 or file{"LO"} == 1) and (file{"RD"} == 0 or file{"RI"} == 0 or file{"RO"} == 0):
            print("Left Door Opens.")
        else:
            print("Neither Door Opens.")
    #doos open with child lock
    elif file{"CL"} == 1:
        if (file{"LD"} == 1 or file{"LO"} == 1) and (file{"RD"} == 1 or file{"RO"} == 1):
            print("Both Doors Open.")
        elif (file{"RD"} == 1 or file{"RO"} == 1) and (file{"LD"} == 0 or file{"LO"} == 0):
            print("Right Door Opens.")
        elif (file{"LD"} == 1 or file{"LO"} == 1) and (file{"RD"} == 0 or file{"RO"} == 0) :
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

