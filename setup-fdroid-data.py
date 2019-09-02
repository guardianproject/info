#!/usr/bin/env python3

import json
import os
import sys
import yaml
from datetime import datetime
from fdroidserver import common
from fdroidserver import index


site_languages = set()


def get_localized_icon(app):
    if 'localized' in app \
       and 'en-US' in app['localized'] \
       and 'icon' in app['localized']['en-US']:
        return ('https://guardianproject.info/fdroid/repo/'
                + app['packageName'] + '/en-US/' + app['localized']['en-US']['icon'])
    return 'https://guardianproject.info/fdroid/repo/icons-480/' + app['icon']


def get_languages(app):
    ret = set()
    if 'localized' in app:
        languages = app['localized'].keys()
        for language in languages:
            if language in ('en', 'en-US', 'es-ES', 'es-US', 'fr-CA', 'fr-FR', 'no'):
                continue
            ret.add(language)
    site_languages.update(ret)
    return sorted(ret)


def write_app_page(app, languages, lang=None):
    if lang:
        filename = 'content/apps/%s.%s.md' % (app['packageName'], lang)
    else:
        filename = 'content/apps/%s.md' % app['packageName']
    with open(filename, 'w') as fp:
        fp.write('---\n')
        fp.write('title: ' + app['name'] + ' ' + '\n')
        if languages:
            fp.write('languages: ' + yaml.safe_dump(languages, width=sys.maxsize, default_flow_style=True))
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
        if 'localized' in app and lang in app['localized'] and 'summary' in app['localized'][lang]:
            subtitle = app['localized'][lang]['summary']
        if subtitle:
            d = {'subtitle': subtitle}
            fp.write(yaml.safe_dump(d, width=sys.maxsize, default_flow_style=False,
                                    encoding='utf-8', allow_unicode=True).decode())
        fp.write('icon: ' + get_localized_icon(app) + '\n')
        if app.get('sourceCode'):
            fp.write('sourceCode: ' + app['sourceCode'] + '\n')
        fp.write('blackfriday:\n  extensions:\n    - hardLineBreak\n')
        fp.write('tags:\n')
        fp.write('  - app\n')
        fp.write('  - ' + app['packageName'] + '\n')
        fp.write('  - ' + app['name'].lower() + '\n')
        fp.write('  - ' + app['license'] + '\n')
        if lang is None:
            fp.write('aliases:\n  - apps/' + app['name'].split(':')[0].lower() + '\n')
            fp.write('menu:\n  main:\n    parent: apps\n')
        fp.write('---\n\n')


fdroid_config = dict()
fdroid_config['jarsigner'] = 'jarsigner'
common.config = fdroid_config
index.config = fdroid_config

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
    languages = get_languages(app)
    write_app_page(app, languages)
    for language in languages:
        write_app_page(app, languages, language)

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

print('languages:\n  en: {weight: 1}')
for lang in sorted(site_languages):
    if not lang.startswith('en'):
        print('  %s: {weight: 2}' % lang)
