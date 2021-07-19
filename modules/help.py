import glob, sys, shutil, time
from modules import useful
from os import mkdir, remove, path, scandir, getcwd

def showHelpFile():
	sFilePathInNode = './node_modules/processpy/HELP.txt'
	sFilePath = './HELP.txt'

	if path.isfile(sFilePathInNode):
		useful.readFileAndPrint(sFilePathInNode)
	else:
		useful.readFileAndPrint(sFilePath) 