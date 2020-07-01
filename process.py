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

try:
	sArgv = sys.argv[1]

	if sArgv == '-help':
		print('Help.');
	elif sArgv == '-html':
		html.deleteFilesOrDirectories(sFinalRoute, aIgnore)
		html.loadPagefiles(sTemplateRoute, sInitialRoute, sFinalRoute)
		html.loadLogs(sFileLog)
	elif sArgv == '-sql':
		sFilePath = sys.argv[2]
		sFolderPath = sys.argv[3]
		sql.loadSQLFile(sFilePath, sFolderPath)
	else:
		raise Exception("Incorrect command: " + sArgv)
except Exception as e:
	print('[Error] Use the -help command to get help. ' + str(e))
else:
	print('[OK] Everything has gone well.')
finally:
	print('Ending.')