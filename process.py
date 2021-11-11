#!/usr/bin/env python
import sys
from python_modules.processpy import useful
from python_modules.processpy import html
from python_modules.processpy import sql
from python_modules.processpy import rts
from python_modules.processpy import help

sTemplateRoute = './pageTemplates'
sInitialRoute = './pages'
sFinalRoute = './web'
sFileLog = './processpy.log'
aIgnore = ['src']

try:
	sArgv = sys.argv[1]

	if sArgv == '-html':
		html.deleteFilesOrDirectories(sFinalRoute, aIgnore)
		html.loadPagefiles(sTemplateRoute, sInitialRoute, sFinalRoute)
		html.loadAdditionalFilesAndFolders(sTemplateRoute)
		html.loadLogs(sFileLog)
	elif sArgv == '-sql':
		sFilePath = sys.argv[2]
		sFolderPath = sys.argv[3]
		sql.loadSQLFile(sFilePath, sFolderPath)
	elif sArgv == '-rts':
		sFolderPath = sys.argv[2]
		sSearchText = sys.argv[3]
		sReplaceText = sys.argv[4]
		rts.LoadNewTextString(sFolderPath, sSearchText, sReplaceText)
	elif sArgv == '-help':
		help.showHelpFile()
	else:
		raise Exception("Incorrect command: " + sArgv)
except Exception as e:
	print('[Error] Use the "python process.py -help" command to get help. ' + str(e))
else:
	print('[OK] Everything has gone well.')
finally:
	print('Ending.')