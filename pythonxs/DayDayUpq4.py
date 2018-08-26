#DayDayUpq4.py
def dayUP(df):
<<<<<<< HEAD
    dayup =1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup =dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup 
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是{:.3f}".format(dayfactor))
=======
    dayup = 1
    for i in range(365):
        if i %7 in [6,0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是:{:.3f}".format(dayfactor))
>>>>>>> f4cb1ea8b6fda3e22eab3e76c6d75de93eca18a9
