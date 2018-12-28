import datetime
i = datetime.datetime.now()
targetDay = i.date()  #将输入的日期格式化成标准的日期
print(targetDay)
dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)  #减去上一年最后一天
totalCount = datetime.date(targetDay.year, 12, 31) - datetime.date(targetDay.year - 1, 12, 31)  #减去上一年最后一天
print(dayCount.days, totalCount.days, dayCount.days/totalCount.days)