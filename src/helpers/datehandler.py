from datetime import datetime, timedelta

date_format = "%Y-%m-%d"

def convertTextDate(dateToConvert):
    return datetime.strptime(dateToConvert,date_format)

def layngaycuoithang(date):
    month = date.month
    year = date.year
    if month == 12:
        month -= 12
        year += 1
    return date.replace(year=year,day=1, month=month+1) - timedelta(days=1)

def layngaydauthang(date):
    return date.replace(day=1)

def convertDateToText(dateToConvert):
    return datetime.strftime(dateToConvert,date_format)

def luithang(date):
    month = date.month
    year = date.year
    if month < 2:
        month += 12
        year -= 1
    return date.replace(year=year,day=1, month=month-1)

def current_toString():
    datetoconvert = datetime.now()
    return datetoconvert.strftime("%Y%m%d_%H%M%S")

