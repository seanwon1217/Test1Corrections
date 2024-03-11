#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 22:46:02 2024

@author: seanwon
"""

# PART 2

# Question 1

def count_unique_proteins(proteins):
    return len(set([protein.split('.')[0] for protein in proteins]))

# Question 2

def count_proteins(proteins):
    protein_counts = {}
    for protein in proteins:
        if protein.split('.')[0] in protein_counts.keys():
            protein_counts[protein.split('.')[0]] += 1
        else:
            protein_counts[protein.split('.')[0]] = 1
    return protein_counts

# Question 3

def merge_protein_counts(counts_1, counts_2):
    combined_counts = {}
    keys_1 = set(counts_1.keys())
    keys_2 = set(counts_2.keys())
    for key in keys_1 | keys_2:
        combined_counts[key] = (counts_1.get(key,0), counts_2.get(key, 0))
    return combined_counts


# PART 3

# Question 1

def dates_to_iso8601(dates_list):
    months = {'January': '01', 'February': '02', 'March': '03', 'April': '04',
              'May': '05', 'June': '06', 'July': '07', 'August': '08', 
              'September': '09', 'October': '10', 'November': '11',
              'December': '12'}
    iso_dates = []
    for date in dates_list:
        year = date.split(' ')[2]
        month = months[date.split(' ')[0]]
        if len(date.split(' ')[1]) == 3:
            day = date.split(' ')[1][0:2]
        else:
            day = '0' + date.split(' ')[1][0]
        iso_dates.append(year + '-' + month + '-' + day)
    return iso_dates

# Question 2

def sort_dates(dates_list):
    sorted_dates = {}
    iso_dates = dates_to_iso8601(dates_list)
    for i in range(len(iso_dates)):
        sorted_dates[iso_dates[i]] = dates_list[i]
    ret = []
    for date in sorted(sorted_dates):
        ret.append(sorted_dates[date])
    return ret

