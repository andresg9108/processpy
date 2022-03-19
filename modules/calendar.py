from datetime import datetime
import calendar

def printCalendar(sDate = ''):
	# datetime.today().strftime('%Y-%m-%d')
	iYear = int(datetime.today().strftime('%Y'))
	iMonth = int(datetime.today().strftime('%m'))

	if sDate != '':
		aDate = sDate.split('-')
		iYear = int(aDate[0])

		if len(aDate) > 1:
			iMonth = int(aDate[1])

	print(calendar.month(iYear, iMonth))