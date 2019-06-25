#!/usr/bin/env python
import sys
from settings import useful

sArgv = sys.argv[1]

if sArgv == '-test':
	useful.test()
else:
	print('Incorrect command')