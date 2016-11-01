#!/usr/bin/env python3

import urllib.parse as urlparse
import sys
import base64

#for url in sys.stdin:
#	print(dict(urlparse.parse_qsl(urlparse.urlsplit(url).query)))

for flag in sys.stdin:
	try:
		sys.stdout.write(str(list(map(lambda x: base64.b64decode(bytes(x, 'utf-8')),flag.split(',')))))
	except Exception as e:
		sys.stderr.write(e)
