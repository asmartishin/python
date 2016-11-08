#!/usr/bin/env python3

import base64
import binascii
import pickle
import json
import order

b = order.Order()

print(base64.b64encode(binascii.hexlify(pickle.dumps(b))))

a = pickle.loads(binascii.unhexlify(base64.b64decode(base64.b64encode(binascii.hexlify(pickle.dumps(b))))))

print(a.__dict__)
