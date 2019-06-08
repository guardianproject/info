#!/usr/bin/env python3

import json
import os
from datetime import datetime
from fdroidserver import common
from fdroidserver import index


config = dict()
config['jarsigner'] = 'jarsigner'
common.config = config
index.config = config

headers = {'User-Agent': 'F-Droid'}
timeout = 60

repo_name = 'F-Droid'
fingerprint = ''

repo_url = 'https://guardianproject.info/fdroid/repo'
archive_url = 'https://guardianproject.info/fdroid/archive'
fdroid_url = 'https://f-droid.org/repo'

fingerprint = 'B7C2EEFD8DAC7806AF67DFCD92EB18126BC08312A7F2D6F3862E46013C7A6135'

data, etag = index.download_repo_index(repo_url + '?fingerprint=' + fingerprint)

appsdict = dict()
for app in data['apps']:
    appsdict[app['packageName']] = app
    with open('content/apps/%s.md' % app['packageName'], 'w') as fp:
        fp.write('---\n')
        fp.write('title: ' + app['name'] + ' ' + '\n')
        subtitle = app.get('summary')
        lastUpdated = app.get('lastUpdated')
        if lastUpdated:
            ts = int(lastUpdated) / 1000
            fp.write('date: ' + datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') + ' ' + '\n')
        fp.write('packageName: ' + app['packageName'] + '\n')
        if 'localized' in app and 'en-US' in app['localized']:
            if 'featureGraphic' in app['localized']['en-US']:
               fp.write('#bigimg: [{"src": "' + 'https://guardianproject.info/fdroid/repo/'
                        + app['packageName'] + '/en-US/'
                        + app['localized']['en-US']['featureGraphic'] + '"},]\n')
            if 'summary' in app['localized']['en-US']:
                subtitle = app['localized']['en-US']['summary']
        if subtitle:
            fp.write('subtitle: ' + subtitle + '\n')
        fp.write('icon: https://guardianproject.info/fdroid/repo/icons-480/' + app['icon'] + '\n')
        if app.get('sourceCode'):
            fp.write('sourceCode: ' + app['sourceCode'] + '\n')
        fp.write('blackfriday:\n  extensions:\n    - hardLineBreak\n')
        fp.write('tags:\n')
        fp.write('  - app\n')
        fp.write('  - ' + app['packageName'] + '\n')
        fp.write('  - ' + app['name'].lower() + '\n')
        fp.write('  - ' + app['license'] + '\n')
        fp.write('aliases:\n  - apps/' + app['name'].split(':')[0].lower() + '\n')
        fp.write('menu:\n  main:\n    parent: apps\n')
        fp.write('---\n\n')

data['apps'] = appsdict
with open('data/repo.json', 'w') as fp:
    json.dump(data, fp, indent=2, sort_keys=True)

archive, etag = index.download_repo_index(archive_url + '?fingerprint=' + fingerprint)

activePackageNames = appsdict.keys()
newarchive = dict()
newarchive['apps'] = []
newarchive['packages'] = dict()
for app in archive['apps']:
    if app['packageName'] not in activePackageNames:
        newarchive['apps'].append(app)

for packageName, packageList in archive['packages'].items():
    if packageName not in activePackageNames:
        newarchive['packages'][packageName] = packageList

with open('data/archive.json', 'w') as fp:
    json.dump(newarchive, fp, indent=2, sort_keys=True)
