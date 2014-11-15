# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys, os, re
import urllib
import urllib2
import json
import random

def results(parsed, original_query):
    keyword = parsed.get('~keyword', '').strip()
    if not keyword:
        return {}
    url = 'http://movie.douban.com/j/subject_suggest?q=%s' % urllib.quote(keyword)
    response = urllib2.urlopen(url).read()
    candidates = json.loads(response)
    if not candidates or type(candidates) != type([]):
        return {}
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
        border-bottom: #ddd 1px solid;
        padding: 0px 0px 10px 0px;
        margin: 0px 0px 10px 0px;
        color: #444;
    }
    li.movie a h3 {
        font-size: 18px;
        color: #444;
        padding: 5px 0 0 0;
    }
    div.content {
        padding: 15px;
    }
    ul, li {
        list-style: none;
    }
    li.movie {
        font-size: 15px;
        color: #888;
        padding: 5px 0;
        width: 100%;
        overflow: auto;
        border-bottom: #ddd 1px dotted;
        cursor: pointer;
    }
    li.movie .text {
        margin-left: 42px;
    }
    li.movie h3 .year {
        color: #888;
        font-weight: normal;
    }
    li.movie a {
        color: #37a;
        text-decoration: underline;
    }
    li.movie .subtitle {
        font-size: 15px;
        color: #888;
    }
    li.movie img.thumbnail {
        width: 32px;
        float: left;
        margin-right: 10px;
    }
    </style>
    '''
    content = u'<ul>'
    template = u'<li class="movie"><img src="{img}" class="thumbnail" /><div class="text"><h3 class="title"><a href="{url}">{title}</a> <span class="year">{year}</span></h3><p class="subtitle">{subtitle}</p></div></li>'
    first_url = None
    first_title = None
    for item in candidates:
        title = item.get('title', '')
        subtitle = item.get('sub_title', '')
        year = item.get('year', '')
        year = '(%s)' % year if year else ''
        item_type = item.get('type', '')
        img = item.get('img', '')
        url = item.get('url', '')
        episode = 0
        if not first_url or not first_title:
            first_url = url
            first_title = title
        try:
            episode = int(item.get('episode') or 0)
        except ValueError:
            episode = 0
        content = content + template.format(title=title, subtitle=subtitle, year=year, img=img, url=url, episode=episode)
    content = content + u'</ul>'
    html = u'<div class="body" onmouseover="this.backgroundColor = \'#ddd\'"><div class="content"><h1 class="keyword">%(keyword)s</h1><div class="data">%(content)s</div></div></div>' % dict(keyword=keyword.decode('utf-8'), content=content)
    return {
        "title": u'豆瓣搜索 "%s"（回车打开 "%s"）' % (keyword.decode('utf-8'), first_title),
        "html": u'%s%s' % (style, html),
        "run_args": [first_url],
        "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
        "webview_links_open_in_browser": True,
    }

def run(url):
    if url:
        os.system('open "{0}"'.format(url))
