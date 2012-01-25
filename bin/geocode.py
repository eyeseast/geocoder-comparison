#!/usr/bin/env python
"""
Bulk geocode a set of addresses, outputting a csv.
This script is meant to test various geocoders. Data will be
overwritten on each run.
"""
import argparse
import csv
import geocoders
import os

DATA_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '../data'))

def geocode(file, geocoder):
    pass


if __name__ == "__main__":
    pass