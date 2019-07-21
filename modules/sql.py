import glob, sys, shutil, time
from modules import useful
from os import mkdir, remove, path, scandir, getcwd

def loadSQLFile(sFilePath, sFolderPath):
	if path.exists(sFolderPath):
		aFile = useful.lsFiles(sFolderPath)
		# aFile.reverse()
		aFile.sort()

		aFinalContent = []
		for sFile in aFile:
			sExtension = useful.getFileExtension(sFile)
			if sExtension == '.sql':
				sFileP = sFolderPath+'/'+sFile

				oFile = open(sFileP, "r")
				aContent = oFile.readlines()
				oFile.close()

				aContent.append('\n')
				aFinalContent = aFinalContent + aContent

		iCount = 0
		for sLine in aFinalContent:
			aFinalContent[iCount] = ' ' + sLine
			iCount = iCount + 1

		oFile = open(sFilePath, "w")
		oFile.writelines(aFinalContent)
		oFile.close()