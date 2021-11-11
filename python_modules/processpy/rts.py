import glob, sys, shutil, time
from python_modules.processpy import useful
from os import mkdir, remove, path, scandir, getcwd

def LoadNewTextString(sFolderPath, sSearchText, sReplaceText):
	sLastChar = sFolderPath[-1:]
	if sLastChar == '/':
		sFolderPath = sFolderPath[:-1]

	aFiles = useful.lsFiles(sFolderPath)

	for sFile in aFiles:
		sFile = sFolderPath + '/' + sFile
		aContent = useful.getFileContent(sFile)

		iCount = 0
		for sLine in aContent:
			aContent[iCount] = sLine.replace(sSearchText, sReplaceText)
			iCount = iCount + 1

		oFile = open(sFile, "w")
		oFile.writelines(aContent)
		oFile.close()

	aFolderPath = useful.lsDirectories(sFolderPath)
	
	for sFolder in aFolderPath:
		sNewFolderPath = sFolderPath+'/'+sFolder

		LoadNewTextString(sNewFolderPath, sSearchText, sReplaceText)