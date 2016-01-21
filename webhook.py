#!/usr/bin/env python2.7

import os, sys, json
from cgi import parse_header
try:
  cl, _ = parse_header(os.environ['Content-Length'])
except:
  cl = 44434;

data = sys.stdin.read(int(cl))
myjson = json.loads(data)

print json.dumps(myjson, sort_keys=True, indent=4, separators=(',', ': '))
