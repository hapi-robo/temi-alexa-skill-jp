#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dialogflow intent to utterances

Extracts utterances from Dialogflow intent export file (.json)
and substitutes a single entity with a predefined SLOT_NAME value.

"""
import argparse
import json

ENTITY_NAME = "@sys.music-artist"
SLOT_NAME = "{noun}" 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('path', help='Dialogflow intent export (.json)')
    args = parser.parse_args()
    
    utterances = []

    with open(args.path) as f:
        data = json.load(f)
        for u in data['userSays']:

            sentence = ''
            for fragment in u['data']:
                
                # look for slot
                if "meta" in fragment:
                    if fragment['meta'] == ENTITY_NAME:
                        sentence += SLOT_NAME
                        # sentence += fragment['text']
                    else:
                        print("Unknown slot")
                
                # look for key utterance
                else:
                    sentence += fragment['text']

            utterances.append(sentence)

    # remove duplicates
    utterances = list(set(utterances))

    # print to console
    for utterance in utterances:
        print("\"{}\",".format(utterance))
