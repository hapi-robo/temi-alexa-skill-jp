#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dialogflow intent to entities

Extracts entities from Dialogflow intent export file (.json)

"""
import argparse
import json

ENTITY_NAME = "@sys.any"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('path', help='Dialogflow intent export (.json)')
    args = parser.parse_args()
    
    entities = []

    with open(args.path) as f:
        data = json.load(f)
        for u in data['userSays']:

            for fragment in u['data']:
                
                # look for slot
                if "meta" in fragment:
                    if fragment['meta'] == ENTITY_NAME:
                        entities.append(fragment['text'])
                    else:
                        print("Unknown slot")

    # remove duplicates
    entities = list(set(entities))

    # print to console
    for entity in entities:
        print("{")
        print("\t\"name\": {")
        print("\t\t\"value\": \"{}\"".format(entity))
        print("\t}")
        print("},")
