#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
                            ##Size and Reads##
""""Reads JSON text file from HIVE"""
################################################################################
import os, json, csv

json_file = "/Users/hadleyking/Downloads/contigs.json"
#______________________________________________________________________________#
def readJSON( file ):
    """loads a json file"""
    genomes = {}
    with open(file) as data_file:
        data = json.load(data_file)
    span = len(data)
    print span
    tot_size = 0
    tot_records = 0 
    for i in data:
        size, records = i['name'], i['rec-count']
        print size, records
        # tot_size += size
        # tot_records += records
    print tot_size, tot_records
    return data

#______________________________________________________________________________#
def main ():
    newList = []
    genomes = readJSON(json_file)
#______________________________________________________________________________#
if __name__ == '__main__': main()