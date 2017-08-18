from datetime import timedelta,date

#date durations used to calculate number of Sundays
week = timedelta(days=7)
dayDuration = timedelta(days=1)
begin = date(1901,1,1)
day = begin
end = date(2000,12,31)

#find first Sunday after begin 
while(day.weekday() != 6):
	day = day + dayDuration

count = 0

#loops through every sunday between begin and end
while(day < end):
	#sunday begins on first of month
	if(day.day == 1):
		count += 1
	day += week

print(count)

