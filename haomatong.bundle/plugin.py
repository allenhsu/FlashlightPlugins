# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys, os, re
import urllib2
import json

def results(parsed, original_query):
    number = parsed.get('number', '')
    number = re.sub(r'[^0-9]', '', number)
    if not number:
        return {}
    url = 'http://data.haoma.sogou.com/vrapi/query_number.php?number=%s&type=json&callback=show' % number
    response = urllib2.urlopen(url).read()
    matches = re.findall(r'{[^}]*}', response)
    title = 'Unknown number'
    if matches:
        result = json.loads(matches[0])
        error_code = result.get('errorCode', 0)
        amount = int(result.get('Amount', 0))
        num_info = result.get('NumInfo')
        info = num_info.split(u'：')
        if len(info) > 1:
            if amount > 0:
                title = '%s (%s, %d reports)' % (info[0], info[1], amount)
            else:
                title = '%s (%s)' % (info[0], info[1])
        else:
            title = '%s' % (num_info)
    return {
        "title": title,
    }
