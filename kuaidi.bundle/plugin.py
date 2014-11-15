# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys, os, re
import urllib2
import json
import random

def results(parsed, original_query):
    number = parsed.get('number', '')
    number = re.sub(r'[^0-9]', '', number)
    if not number:
        return {}
    url = 'http://www.kuaidi100.com/autonumber/auto?num=%s' % number
    response = urllib2.urlopen(url).read()
    prediction = json.loads(response)
    if not prediction or type(prediction) != type([]):
        return {}
    comCode = prediction[0]['comCode']
    url = 'http://www.kuaidi100.com/query?type=%(comCode)s&postid=%(number)s&id=1&valicode=&temp=%(temp)s' % dict(comCode=comCode, number=number, temp=random.random())
    response = urllib2.urlopen(url).read()
    result = json.loads(response)
    data = result.get('data')
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
    ul, li {
        list-style: none;
    }
    li {
        font-size: 15px;
        color: #888;
        padding: 3px 0;
    }
    .time {
        font-size: 12px;
        color: #aaa;
    }
    .context {
        font-size: 15px;
        color: #444;
    }
    .current .context {
        font-weight: bold;
        color: #444;
    }
    </style>
    '''
    content = '<ul>'
    last_status = ''
    i = 0
    for item in data:
        if not last_status:
            last_status = item.get('context', '')
        content = content + '<li class="%s"><p class="time">%s</p><p class="context">%s</p></li>' % ('current' if i == 0 else '', item.get('time'), item.get('context'))
        i += 1
    content = content + '</ul>'
    html = u'<div class="body"><div class="content"><h1 class="number">%(number)s</h1><div class="data">%(content)s</div></div></div>' % dict(number=number, content=content)
    return {
        "title": last_status,
        "html": '%s%s' % (style, html),
    }
