import tushare as ts #import tushare API
import datetime
today = datetime.date.today().isoweekday() #fetch date of today
print(today)
todaydate = datetime.date.today()
print(todaydate)
code = open("1.txt", "r")

pro = ts.pro_api('08b18fbf08a12be74774d57c798486d4599cd271b805a61806d01308') #login to tushare
df = pro.daily(ts_code=code.read(), start_date='20230111', end_date='todaydate') #fetch stock prices
 
file = open('ass.txt', mode='w') #output stock prices to ass.txt for main module to read
for i in range(len(df)):
    s = str(df.close[i]) 
    file.write(s + ' \n')
    print(s)
file.close()

