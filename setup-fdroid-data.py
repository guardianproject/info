#!/usr/bin/env python3

import fdroidserver
import json
import sys
import unicodedata
import yaml
from datetime import datetime


site_languages = set()

def get_app_name(app):
    name = app.get('name')
    if name:
        return name
    name = app.get('localized', {}).get('en-US', {}).get('name')
    if name:
        return name
    return app['packageName']


def get_localized_icon(app):
    if 'localized' in app \
       and 'en-US' in app['localized'] \
       and 'icon' in app['localized']['en-US']:
        return ('https://guardianproject.info/fdroid/repo/'
                + app['packageName'] + '/en-US/' + app['localized']['en-US']['icon'])
    icon = app.get('icon')
    if icon:
        return 'https://guardianproject.info/fdroid/repo/icons-480/' + icon
    else:
        return 'https://guardianproject.info/ic_repo_app_default.png'  # placeholder


def write_app_page(app, languages, lang=None):
    if lang:
        filename = 'content/apps/%s.%s.md' % (app['packageName'], lang)
    else:
        filename = 'content/apps/%s.md' % app['packageName']
    with open(filename, 'w') as fp:
        fp.write('---\n')
        d = {'title': get_app_name(app)}
        fp.write(yaml.safe_dump(d, width=sys.maxsize, default_flow_style=False,
                                encoding='utf-8', allow_unicode=True).decode())
        if languages:
            fp.write('languages: '
                     + yaml.safe_dump(sorted(languages), width=sys.maxsize, default_flow_style=True))
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
        fp.write('  - ' + app['license'] + '\n')
        normalized_name = unicodedata.normalize('NFD', get_app_name(app).split(':')[0])\
                                      .encode('ascii', 'ignore')\
                                      .decode()\
                                      .lower()
        fp.write('  - ' + normalized_name + '\n')
        if lang is None:
            fp.write('aliases:\n  - apps/' + normalized_name + '\n')
            fp.write('menu:\n  main:\n    parent: apps\n')
        fp.write('---\n\n')


fdroid_config = dict()
fdroid_config['jarsigner'] = 'jarsigner'
fdroidserver.common.config = fdroid_config

headers = {'User-Agent': 'F-Droid'}
timeout = 60

repo_name = 'F-Droid'
fingerprint = ''

repo_url = 'https://guardianproject.info/fdroid/repo'
archive_url = 'https://guardianproject.info/fdroid/archive'
fdroid_url = 'https://f-droid.org/repo'

fingerprint = 'B7C2EEFD8DAC7806AF67DFCD92EB18126BC08312A7F2D6F3862E46013C7A6135'

data, etag = fdroidserver.download_repo_index_v1(repo_url + '?fingerprint=' + fingerprint)

appsdict = dict()
apps = list(data['apps'])
for app in apps:
    if app['packageName'] == 'org.article19.circulo':
        # remove Circulo until it has localized description in the fdroid repo
        continue
    languages = set()
    if 'localized' in app:
        for language in list(app['localized'].keys()):
            if language in ('en', 'en-US'):
                continue
            if len(language) > 3 and language != 'pt-BR' and not language.startswith('zh'):
                if '-' in language:
                    l, _ = language.split('-')
                elif '_' in language:
                    l, _ = language.split('_')
                else:
                    continue
                if l in languages:
                    continue
                app['localized'] = app['localized'].copy()
                app['localized'][l] = app['localized'][language]
                language = l
            if language == 'no':
                continue  # "no" is obsolete and conflicts with YAML true values
            if '-' in language or '_' in language:
                continue  # the script/Hugo setup can't handle these yet
            languages.add(language)
    site_languages.update(languages)
    appsdict[app['packageName']] = app
    write_app_page(app, languages)
    for language in languages:
        write_app_page(app, languages, language)

data['apps'] = appsdict
with open('data/repo.json', 'w') as fp:
    json.dump(data, fp, indent=2, sort_keys=True)

archive, etag = fdroidserver.download_repo_index_v1(archive_url + '?fingerprint=' + fingerprint)

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
    if not lang.startswith('en') and lang != 'pt-PT':
        print('  %s: {weight: 2}' % lang)
