#!/bin/sh -ex
#
# check for broken links
# apt-get install -qy locales zlib1g-dev gettext po4a linkchecker bundler unzip python3 rsync python3-babel

if [ -z "$1" ]; then
    url="https://guardianproject.info"
else
    url="$1"
fi

linkchecker "$url" \
	    --config="$(dirname $0)/../.linkcheckerrc" \
	    --ignore-url ".*/packages/[b-z].*" \
	    --ignore-url "/F-Droid\.apk(\.asc)?$"
