#!/usr/bin/env python
import sys
from modules import useful
from modules import html
from modules import sql
from modules import rts
from os import mkdir, remove, path, scandir, getcwd

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
		if path.isfile('./node_modules/processpy/HELP.txt'):
			useful.readFileAndPrint('./node_modules/processpy/HELP.txt')
		else:
			useful.readFileAndPrint('./HELP.txt')
	else:
		raise Exception("Incorrect command: " + sArgv)
except Exception as e:
	print('[Error] Use the "python process.py -help" command to get help. ' + str(e))
else:
	print('[OK] Everything has gone well.')
finally:
	print('Ending.')