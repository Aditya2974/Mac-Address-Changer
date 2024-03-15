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
    
    return mac.strip(":")

def get_current_mac_address(iface,new_mac_address):

    # disabled the network interface:
    subprocess.check_output(f"ifconfig {iface} down",shell=True)

    # Change the MAC
    subprocess.check_output(f"ifconfig {iface} hw ether {new_mac_address}",shell=True)

    #enabling the network interface again
    subprocess.check_output(f"ifconfig {iface} up",shell=True)


def pt():
    print("Hello")