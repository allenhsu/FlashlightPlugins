# -*- coding: utf-8 -*-
#!/usr/bin/python

import json, urllib,urllib2, os

def getURL(parsed):
    q = parsed['~query'] if '~query' in parsed else "";
    q = q.lower().strip();
    q = "" if q == "daily" else q;
    # print q;
    q = "date/"+q if q!="" and q[0].isdigit() else q;
    url = "http://youzhihu.com/"+format(urllib.quote(q))
    # print url;
    return url;

def results(parsed, original_query):
    html = ""
    try:
        url = getURL(parsed)
        html = """<script>
                setTimeout(function() {
                     window.location = %s;
                }, 500); // throttle a little
                </script>
                """ % (json.dumps(url))

    except:
        error_file = open('error.html')
        html = error_file.read().decode('utf-8')
        error_file.close()
    # print html

    return {
        "title": "知乎",
        "html": html,
    }

# results({"~query":"20140822"},{});