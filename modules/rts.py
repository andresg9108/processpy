import glob, sys, shutil, time
from modules import useful
from os import mkdir, remove, path, scandir, getcwd

def LoadNewTextString(sFolderPath, sSearchText, sReplaceText):
	aFolderPath = useful.lsDirectories(sFolderPath)
	
	for sFolder in aFolderPath:
		sNewFolderPath = sFolderPath+'/'+sFolder
		aFiles = useful.lsFiles(sNewFolderPath)

		print(sNewFolderPath)
		for sFile in aFiles:
			print('- '+sFile)

		LoadNewTextString(sNewFolderPath, sSearchText, sReplaceText)