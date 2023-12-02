import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename='data/sitka_weather_2018_simple.csv'
with open(filename)as f:
	reader=csv.reader(f)
	header_row=next(reader)
	#get date and high temperature from this file
	dates,high,lows=[],[],[]
	for index,column_header in enumerate(header_row):
		print(index,column_header)
	#get high temperature from this file
	highs=[]
	for row in reader:
		current_date=datetime.strptime(row[2],'%Y-%m-%d')
		high=int((row[5]))
		low=int(row[6])
		dates.append(current_date)
		highs.append(high)
		lows.append(low)
print(highs)
#plot high temperatures
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolors='blue',alpha=0.1)
#format plot
plt.title('daily high and low temperatures , 2018',fontsize=24)
plt.xlabel(' ',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('temperature(f)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()



