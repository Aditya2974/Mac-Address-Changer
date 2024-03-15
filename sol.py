import subprocess
import string
import random
import re


# generating and returning a new mac-address
def get_random_mac_address():
    """Get and return a MAC address in the format of Linux"""
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    
    # the second character must be 0,2,4,6,8,A,C,or,E
    
    mac = ""
    
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    


    