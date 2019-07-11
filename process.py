#!/usr/bin/env python
import sys
from modules import useful
from modules import html

sTemplateRoute = './pageTemplates'
sInitialRoute = './pages'
sFinalRoute = './web'
sFileLog = './manyp.log'
aIgnore = ['src']

sArgv = sys.argv[1]

if sArgv == '-test':
	useful.test()
elif sArgv == '-l':
	html.deleteFilesOrDirectories(sFinalRoute, aIgnore)
	html.loadPagefiles(sTemplateRoute, sInitialRoute, sFinalRoute)
	html.loadLogs(sFileLog)

	print('OK')
else:
	print('Incorrect command')