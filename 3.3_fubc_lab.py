
#########################################################
# FUNCTIONS
#########################################################
def IsYearLeap(year):
    if (year % 4 == 0):
        return True
    return False

def DaysInMonth(year, month):
    if (IsYearLeap(year)):
        mont_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        mont_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return mont_days[month-1]

def DayOfYear(year,month,day):
    result_day = 0
    for m in range(1,month):
        result_day += DaysInMonth(year, month-1)
    result_day += day
    return result_day

#########################################################
print('-'*10,' 1st')
testdata = [1900, 2000, 2016, 1987]
testresults = [False, True, True, False]

for i in range(len(testdata)):
    yr = testdata[i]
    print(yr,"->",end="")
    result = IsYearLeap(yr)

if result == testresults[i]:
    print("OK")
else:
    print("Failed")

#########################################################
print('-'*10,' 2nd')
testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
    yr = testyears[i]
    mo = testmonths[i]
    print(yr,mo,"->",end="")
    result = DaysInMonth(yr,mo)
if result == testresults[i]:
    print("OK")
else:
    print("Failed")

#########################################################
print('-'*10,' 3rd')
print(DayOfYear(2000,12,31))