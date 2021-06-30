import glob, sys, shutil, time
from modules import useful
from os import mkdir, remove, path, scandir, getcwd

def loadAdditionalFilesAndFolders(sTemplateRoute):
	if not path.exists(sTemplateRoute):
		mkdir(sTemplateRoute)
		oFile = open(sTemplateRoute+'/index.html', "w")
		oFile.writelines(['<!--index.html-->'])
		oFile.close()

def getTemplateContent(sTemplateRoute, sInitialRouteHead):
	sFile = 'index.html'
	sKey = '<!--Route:'
	aContentHead = getFileContent(sInitialRouteHead)
	iQuantityContentHead = len(aContentHead)

	if iQuantityContentHead > 0:
		sFileHead = aContentHead[0]
		sFileHead = sFileHead.replace(" ","").replace("\n","")
		sKeyHead = sFileHead[:10]

		if sKey == sKeyHead:
			sFileHead = sFileHead.replace("<!--Route:","").replace("-->","")
			sFile = sFileHead

	sTemplateRoute = sTemplateRoute+'/'+sFile

	aContentIndex = getFileContent(sTemplateRoute)

	return aContentIndex

def loadLogs(sFileLog):
	if not path.isfile(sFileLog):
		oFile = open(sFileLog, "w")
		oFile.write('Logs')
		oFile.close()
	else:
		oFile = open(sFileLog, "r")
		aContent = oFile.readlines()
		oFile.close()

		iCount = 0
		for sLine in aContent:
			iCount = iCount + 1

		if iCount > 99:
			oFile = open(sFileLog, "w")
			oFile.write('Logs')
			oFile.close()

	oFile = open(sFileLog, "a")
	sDate = time.strftime('%d/%m/%y')
	sHour = time.strftime('%H:%M:%S')
	oFile.write('\n')
	oFile.write(sDate+' '+sHour+' (Python [OK])')
	oFile.close()

def loadPagefiles(sTemplateRoute, sInitialRoute, sFinalRoute):
	sHead = 'head.html'
	sBody = 'body.html'
	sIndex = 'index.html'

	if not path.exists(sInitialRoute):
		mkdir(sInitialRoute)
	if not path.exists(sFinalRoute):
		mkdir(sFinalRoute)

	if not path.isfile(sInitialRoute+'/'+sHead):
		oFile = open(sInitialRoute+'/'+sHead,"w")
		oFile.close()
	if not path.isfile(sInitialRoute+'/'+sBody):
		oFile = open(sInitialRoute+'/'+sBody,"w")
		oFile.close()

	aContentIndex = getTemplateContent(sTemplateRoute, sInitialRoute+'/'+sHead)
	aContentHead = getFileContent(sInitialRoute+'/'+sHead)
	aContentBody = getFileContent(sInitialRoute+'/'+sBody)
	sRouteRoot = getRoot(sFinalRoute)

	iCount = 0
	for sLine in aContentIndex:
		if(sLine.replace(" ","").replace("\n","").replace("\t","") == "<!--headHTML-->"):
			sLine = ''
			for sLine2 in aContentHead:
				sLine = sLine + sLine2
			sLine = sLine + '\n'
		elif(sLine.replace(" ","").replace("\n","").replace("\t","") == "<!--bodyHTML-->"):
			sLine = ''
			for sLine2 in aContentBody:
				sLine = sLine + sLine2
			sLine = sLine + '\n'

		aContentIndex[iCount] = sLine
		iCount = iCount + 1

	iCount = 0
	for sLine in aContentIndex:
		sLine = sLine.replace("<<DIR>>", sRouteRoot)
		if sRouteRoot == './':
			sLine = sLine.replace("<<ROOT-DIR>>", '../')
		else:
			sLine = sLine.replace("<<ROOT-DIR>>", sRouteRoot+'../')

		aContentIndex[iCount] = sLine
		iCount = iCount + 1

	oFile = open(sFinalRoute+'/'+sIndex, "w")
	oFile.writelines(aContentIndex)
	oFile.close()

	aInitialRoute = useful.lsDirectories(sInitialRoute)
	for sRoute in aInitialRoute:
		sSonInitialRoute = sInitialRoute+'/'+sRoute
		sSonFinalRoute = sFinalRoute+'/'+sRoute

		loadPagefiles(sTemplateRoute, sSonInitialRoute, sSonFinalRoute)

def getRoot(sRoute):
	sRoute = sRoute.replace("./","")
	sRouteRoot = ''
	for sR in sRoute:
		if(sR == "/"):
			sRouteRoot = sRouteRoot + "../"
	if sRouteRoot == '':
		return './'
	return sRouteRoot

def getFileContent(sRoute):
	aContent = []
	if path.isfile(sRoute):
		oFile = open(sRoute, "r")
		aContent = oFile.readlines()
		oFile.close()
	return aContent

def deleteFilesOrDirectories(sRoute, aIgnore = []):
	if path.exists(sRoute):
		aSonRoute = useful.lsAll(sRoute)
		for sSonRoute in aSonRoute:
			bRemove = 1
			for sIgnore in aIgnore:
				if sSonRoute == sIgnore:
					bRemove = 0
			if bRemove == 1:
				useful.deleteFileOrDirectory(sRoute+'/'+sSonRoute)