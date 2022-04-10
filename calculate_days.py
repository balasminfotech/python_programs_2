from datetime import date
f_date = date(2019, 5, 20)
l_date = date(2022, 4, 9)
calc=l_date-f_date
weeks =calc/7
months=calc/30
years=calc/365
print("years: "+ str(years))
print("weeks: "+ str(weeks))
print("months: "+ str(months))
print("Days" +str(calc.days))