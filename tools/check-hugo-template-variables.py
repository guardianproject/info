#!/usr/bin/env python3

import glob
import json
import re

source = dict()
with open('i18n/en.json') as fp:
    for i in json.load(fp):
        matches = re.findall(r'{{ \.[^ ]+ }}', i['translation'])
        if matches:
            k = i['id']
            if k not in source:
                source[k] = []
            for var in matches:
                source[k].append(var)

#import pprint; pprint.pprint(source)

errors = 0
for f in glob.glob('i18n/*.json'):
    with open(f) as fp:
        translations = json.load(fp)
    for t in translations:
        k = t['id'] 
        if k in source:
            for v in source[k]:
                if v not in t['translation']:
                    print(f, k, 'missing', v)
                    errors += 1
    
exit(errors)
