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
    style = u'''
    <style>
    * {
        padding: 0;
        margin: 0;
    }
    html, body, body > div {
        margin: 0;
        width: 100%;
        height: 100%;
        font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial;
        line-height: 1.2;
    }
    h1, h2, h3, h4, h5 {
        font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "HiraginoSansGB-W6", "Hiragino Sans GB W6";
    }
    h1 {
        font-size: 32px;
    }
    h1.number {
        border-bottom: #ddd 1px solid;
        padding: 0px 0px 10px 0px;
        margin: 0px 0px 10px 0px;
        color: #444;
    }
    h3 {
        font-size: 15px;
        color: #888;
    }
    div.content {
        padding: 15px;
    }
    </style>
    '''
    html = u'<div class="body"><div class="content"><h1 class="number">%(number)s</h1><h3>%(title)s</h3></div></div>' % dict(number=number, title=title)
    return {
        "title": title,
        "html": '%s%s' % (style, html),
    }
