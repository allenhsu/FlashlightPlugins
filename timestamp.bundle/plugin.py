#!/usr/bin/python

import sys, urllib, os, time, datetime

def results(parsed, original_query):
    timestamp = int(parsed.get('timestamp', time.time()))
    date = datetime.datetime.fromtimestamp(timestamp)
    timestring = date.strftime('%Y-%m-%d %H:%M:%S')
    return {
        "title": '%s (%d)' % (timestring, timestamp),
    }
