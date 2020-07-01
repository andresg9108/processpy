import glob, sys, shutil, time
from os import mkdir, remove, path, scandir, getcwd

def deleteFileOrDirectory(sRoute):
	if not path.isfile(sRoute):
		shutil.rmtree(sRoute)
	else:
		remove(sRoute)

def lsDirectories(sRoute = getcwd()):
    return [oFile.name for oFile in scandir(sRoute) if not oFile.is_file()]

def lsFiles(sRoute = getcwd()):
    return [oFile.name for oFile in scandir(sRoute) if oFile.is_file()]

def lsAll(sRoute = getcwd()):
    return [oFile.name for oFile in scandir(sRoute)]

def getFileExtension(sFileName):
	sExtension = path.splitext(sFileName)[1]
	return sExtension

def readFileAndPrint(sFileName):
	oFile = open(sFileName, "r")
	aContent = oFile.readlines()
	oFile.close()
	
	for sLine in aContent:
		print(sLine)