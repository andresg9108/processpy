import glob, sys, shutil, time, os
from . import useful
from os import mkdir, remove, path, scandir, getcwd

def loadSQLFile(sFilePath, sFolderPath):
	sFilePath = sFilePath.replace(" ","").replace("\n","").replace("\t","")
	sFolderPath = sFolderPath.replace(" ","").replace("\n","").replace("\t","")
	sLastChar = sFolderPath[-1:]
	if sLastChar == '/':
		sFolderPath = sFolderPath[:-1]

	if path.exists(sFolderPath):
		aFile = []
		for root, dirs, files in os.walk(sFolderPath):
			dirs.sort()
			for name in sorted(files):
				if useful.getFileExtension(name) == '.sql':
					aFile.append(path.join(root, name))

		aFinalContent = []
		for sFileP in aFile:
			with open(sFileP, "r") as oFile:
				aContent = oFile.readlines()
			aContent.append('\n')
			aFinalContent += aContent

		aFinalContent = [' ' + line for line in aFinalContent]

		with open(sFilePath, "w") as oFile:
			oFile.writelines(aFinalContent)
