#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import marshal
import pylzma

if sys.version_info.major != 2:
	print('Python 2.X is required to unmarshal code object')
	sys.exit(0)

from uncompyle6.main import decompile

def decode_pupyrat(filename):
	data = None
	with open(filename, 'rb') as f:
		data = f.read()

	index = data.find(b'\x5d\x00\x00\x80\x00\x00')
	if not index:
		print("LZMA signature not found, skipped")
		return
	
	data = pylzma.decompress(data[index:])
	tmp  = marshal.loads(data)
	decompile(2.7, tmp, sys.stdout, showast=False)

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('Usage: main.py FILE1 FILE2 ...')
		sys.exit(0)

	for filename in sys.argv[1:]:
		decode_pupyrat(filename)

