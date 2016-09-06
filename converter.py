#!/usr/bin/env python

from sys import argv
from os import path
from types import *

import argparse
import logging
import json
import csv
import re

krogerStr = ["kroger", "dillons", "fredmeyer", "frys", "qualityfoodcenters", "ralphs", "citymarket", "food4less", "foodsco", "gerbes", "jayc", "kingscoopers", \
"paylesssupermarket", "harristeeter", "iwireless", "kwikshop", "littmanjewlers", "loafnjug", "quikstop", "thelittleclinic", "tomthumb", "turkeyhill", "fredmeyerjewlers"]

def aboutKroger(body, subreddit):
    # Kroger, Dillons, FredMeyer, Fry's, Quality Food Centers, Ralphs, Smith's, Baker's, City Market, Food 4 Less, Foods Co., Gerbes, JayC, KING Scoopers,
    # Owen's, Pay Less Super Market, Harris Teeter, i Wireless, Kwik Shop, Littman Jewelers, Loaf 'N Jug, QuikStop, The Little Clinic, TomThumb, TurkeyHill, Fred Meyer Jewlers
    body = re.sub('[^a-zA-Z0-9-_*]', '', body).lower()
    subreddit = re.sub('[^a-zA-Z0-9-_*]', '', subreddit).lower()
    for store in krogerStr:
        if re.findall(store, body) or re.findall(store, subreddit):
            return True
    return False

def main():

    parser = argparse.ArgumentParser(
        description='Convert json file to csv'
    )

    parser.add_argument(
        '-i',
        '--input_file',
        dest='input_file',
        default=None,
        required=True,
        help='Source json file (mandatory)'
    )
    parser.add_argument(
        '-o',
        '--output_file',
        dest='output_file',
        default=None,
        required=True,
        help='Destination csv file (mandatory)'
    )

    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file + args.input_file[5:len(args.input_file) - 4] + ".csv"

    json_data = []
    data = None
    write_header = True
    item_keys = []

    with open(input_file) as json_file:
        json_data = json_file.read()

    try:
        data = json.loads(json_data)
    except Exception as e:
        raise e

    with open(output_file, 'wb') as csv_file:
        writer = csv.writer(csv_file)

        for item in data:
            if not aboutKroger(item["body"], item["subreddit"]):
                continue

            item_values = []
            for key in item:
                if write_header:
                    item_keys.append(key)

                value = item.get(key, '')
                if isinstance(value, StringTypes):
                    item_values.append([key, value.encode('utf-8')])
                else:
                    item_values.append([key, value])

            if write_header:
                item_keys = sorted(item_keys, key=lambda x: x)
                writer.writerow(item_keys)
                write_header = False

            item_values = sorted(item_values, key=lambda x: x[0])
            item_vals = []

            for item in item_values:
                item_vals.append(item[1])
            writer.writerow(item_vals)

if __name__ == "__main__":
    main()
