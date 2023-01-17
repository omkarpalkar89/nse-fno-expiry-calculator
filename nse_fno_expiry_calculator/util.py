import pendulum
from pendulum.date import Date
import logging

listOfNseHolidays = set([
Date(2023,1,26),
Date(2023,3,7),
Date(2023,3,22),
Date(2023,3,30),
Date(2023,4,4),
Date(2023,4,7),
Date(2023,4,14),
Date(2023,5,1),
Date(2023,5,5),
Date(2023,6,28),
Date(2023,8,15),
Date(2023,8,16),
Date(2023,9,19),
Date(2023,9,28),
Date(2023,10,2),
Date(2023,10,24),
Date(2023,11,14),
Date(2023,11,27),
Date(2023,12,25)
])

def getNearestWeeklyExpiryDate():
    expiryDate = None
    if(pendulum.now().date().day_of_week is pendulum.THURSDAY):
        expiryDate = pendulum.now()
    else:
        expiryDate = pendulum.now().next(pendulum.THURSDAY)
    return __considerHolidayList(expiryDate).date()


def getNextWeeklyExpiryDate():
    expiryDate = None
    if(pendulum.now().date().day_of_week is pendulum.THURSDAY):
        expiryDate = pendulum.now().next(pendulum.THURSDAY)
    else:
        expiryDate = pendulum.now().next(pendulum.THURSDAY).next(pendulum.THURSDAY)
    return __considerHolidayList(expiryDate).date()


def getNearestMonthlyExpiryDate():
    expiryDate = pendulum.now().last_of('month', pendulum.THURSDAY)
    if(pendulum.now().date() > expiryDate.date()):
        expiryDate = pendulum.now().add(months=1).last_of('month', pendulum.THURSDAY)
    return __considerHolidayList(expiryDate).date()


def getNextMonthlyExpiryDate():
    expiryDate = pendulum.now().last_of('month', pendulum.THURSDAY)
    if(pendulum.now().date() > expiryDate.date()):
        expiryDate = pendulum.now().add(months=2).last_of('month', pendulum.THURSDAY)
    else:
        expiryDate = pendulum.now().add(months=1).last_of('month', pendulum.THURSDAY)
    return __considerHolidayList(expiryDate).date()


# utility method to be used only by this module
def __considerHolidayList(expiryDate: Date):
    if(expiryDate.date() in listOfNseHolidays):
        return __considerHolidayList(expiryDate.subtract(days=1))
    else:
        return expiryDate


# print('today is '+str(pendulum.now().date()))
# print('nearest weekly exp is '+str(getNearestWeeklyExpiryDate()))
# print('next weekly exp is '+str(getNextWeeklyExpiryDate()))
# print('nearest monthly exp is '+str(getNearestMonthlyExpiryDate()))
# print('next month exp is '+str(getNextMonthlyExpiryDate()))