#!/usr/bin/env python3
"""Automates ifconfig command, parses result for MTU value of given interface
Usage: chmod +x to make executable
Usage Example: ./find_mtu.py <interface name>
"""

import sys
import pexpect


def run_ifconfig(interface):
    """Automates ifconfig command on given interface and returns resulting bytes"""
    if_config_command = pexpect.spawn(f"ifconfig -s {interface}")
    result = if_config_command.expect([pexpect.EOF, pexpect.TIMEOUT])
    interface_data = result.before
    return interface_data


def find_mtu(int_data):
    """Decodes given bytes, creates dictionary of data and parses for MTU value"""
    decoded_data_list = int_data.decode().split()
    list_of_keys = decoded_data_list[:len(decoded_data_list)//2]
    list_of_values = decoded_data_list[len(decoded_data_list)//2:]
    int_data_dict = dict(zip(list_of_keys, list_of_values))
    print(f"{int_data_dict['Iface']} has {int_data_dict['MTU']} bytes")


def main():
    try:
        interface_data = run_ifconfig(sys.argv[1])
        find_mtu(interface_data)
    except IndexError:
        print("IndexError\nUsage: ./find_mtu.py <Interface name>")
        exit()


if __name__ == "__main__":
    main()
