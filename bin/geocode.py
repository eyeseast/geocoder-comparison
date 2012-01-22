#!/usr/bin/env python
"""
Bulk geocode a set of addresses, outputting a csv.
This script is meant to test various geocoders. Data will be
overwritten on each run.
"""
import argparse
from geopy import geocoders

GEOCODERS = {
    'google': geocoders.Google(),
    'geocoderdotus': geocoders.GeocoderDotUs()
}

def geocode(file, geocoder):
    pass


if __name__ == "__main__":
    pass