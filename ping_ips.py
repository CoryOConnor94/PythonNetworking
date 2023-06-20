#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Script to read IPs from given csv or excel file, Ping IPs and output results to csv
Usage: ./ping_ips.py <csv file> || <Excel file>
"""
import os
import pandas as pd
import sys


def read_ips():
    """
    Read IPs from given file
    :return: List
    """

    if ".csv" in sys.argv[1]:
        csv_ips = pd.read_csv(sys.argv[1], usecols=["IP Address"]).squeeze()
        return csv_ips
    elif ".xlsx" in sys.argv[1]:
        excel_ips = pd.read_excel(sys.argv[1], usecols=["IP Address"], sheet_name=0).squeeze()
        return excel_ips
    else:
        print("Incorrect File Type. Must bbe .csv or .xlsx")


def ping_ips(ips):
    """
    Pings IPs from list and return results
    :param ips: List
    :return: List
    """
    results = []
    for ip in ips:
        response = os.popen(f"ping {ip} -n 1").read()
        if "Received = 1" and "Approximate" in response:
            result = "Success"
            results.append(result)
        else:
            result = "Failed"
            results.append(result)
        return results


def write_to_file(results, ips):
    """
    Create dataframe of ping results and write to csv file
    :param results: List of results of pings
    :param ips: List of IPs pinged
    :return: Dataframe of IPs and results
    """
    result_series = pd.Series(results)
    df_ping_results = pd.concat([ips, result_series], axis=1)
    df_ping_results.columns = ['IP Address', 'Result']
    df_ping_results.to_csv("ping_results.csv", index=False)


def main():
    ip_list = read_ips()
    ping_results = ping_ips(ip_list)
    write_to_file(ping_results, ip_list)


if __name__ == '__main__':
    main()
