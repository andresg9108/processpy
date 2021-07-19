#!/usr/bin/env python
import sys
from modules import useful
from modules import html
from modules import sql
from modules import rts
from modules import help

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