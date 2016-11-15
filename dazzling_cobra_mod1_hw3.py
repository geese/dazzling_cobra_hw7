#!/usr/bin/env python3
"""
"""




def ctrl(values_dict):
    result = ""
    v = values_dict
    
    if v['GS'] not in ['P','N','D','1','2','3','R']:
        return "Invalid Record: Both doors stay closed."

    if v['ML'] == '1': # master unlock is activated
        if v['GS'] == 'P': # gear shift is in Park
            if v['CL'] == '0': # child lock is NOT activated       
                if v['RI'] == '1' or v['RO'] == '1' or v['RD'] == '1':
                    if v['LI'] == '1' or v['LO'] == '1' or v['LD'] == '1':
                        return "Both doors open."
                    else:
                        return "Right door opens."
                else:  # all right door switches are 0
                    if v['LI'] == '1' or v['LO'] == '1' or v['LD'] == '1':
                        return "Left door opens."
                    else:
                        return "Neither door opens."
            else: # child lock is activated
                if v['RO'] == '1' or v['RD'] == '1':
                    if v['LO'] == '1' or v['LD'] == '1':
                        return "Both doors open."
                    else:
                        return "Right door opens."
                else: # all non-inside right door switches are 0
                    if v['LO'] == '1' or v['LD'] == '1':
                        return "Left door opens."
                    else:
                        return "Neither door opens."
        else: # gear shift is not in Park
            return "Neither door opens."
    else: # master unlock is NOT activated
        return "Neither door opens."
                    


    


# Main function
def main():
    return


if __name__ == '__main__':
    # Call Main
    main()

    exit(0)










