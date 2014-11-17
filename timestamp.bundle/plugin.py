#!/usr/bin/python

import sys, urllib, os, time, datetime

def results(parsed, original_query):
    timestamp = int(parsed.get('timestamp', time.time()))
    date = datetime.datetime.fromtimestamp(timestamp)
    timestring = date.strftime('%Y-%m-%d %H:%M:%S')
    htmlstring = u'<div><h3>%(timestring)s</h3><h3>%(timestamp)d</h3></div>' % dict(timestring=timestring, timestamp=timestamp)
    return {
        "title": '%s (%d)' % (timestring, timestamp),
        "html": htmlstring,
    }
