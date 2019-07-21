#!/usr/bin/env python
import sys
from modules import useful
from modules import html
from modules import sql

sTemplateRoute = './pageTemplates'
sInitialRoute = './pages'
sFinalRoute = './web'
sFileLog = './processpy.log'
aIgnore = ['src']

sArgv = sys.argv[1]

if sArgv == '-html':
	html.deleteFilesOrDirectories(sFinalRoute, aIgnore)
	html.loadPagefiles(sTemplateRoute, sInitialRoute, sFinalRoute)
	html.loadLogs(sFileLog)

	print('OK')
elif sArgv == '-sql':
	sFilePath = sys.argv[2]
	sFolderPath = sys.argv[3]

	sql.loadSQLFile(sFilePath, sFolderPath)
	
	print('OK')
else:
	print('Incorrect command')