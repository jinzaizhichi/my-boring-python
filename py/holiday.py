# TODO:
# 1. get time from server
# 2. use array


import datetime,time,os,platform,sys

oss = platform.system()

if len(sys.argv) == 2:
	print('Sleep time: ' + sys.argv[1] + 's')
	jtime = float(sys.argv[1])
else:
	print('Sleep time: ' + str(0.05) + 's')
	print('You can use time.py <sleep_time> to set sleep time.')
	jtime = 0.05
	time.sleep(2)

while True :
	now_time = datetime.datetime.now()
	summer_holiday = datetime.datetime(2016,8,31,14,30)
	mid_f = datetime.datetime(2016,9,15)
	country_f = datetime.datetime.strptime(2016,10,1)
	open_f = datetime.datetime(2017,1,1)
	print('距离暑假结束只剩下')
	print ((summer_holiday-now_time).days)
	print('距离16年中秋节还有')
	print ((mid_f-now_time).days)
	print('距离16年国庆还有')
	print ((country_f-now_time).days)
	print('距离17年元旦还有')
	print ((open_f-now_time).days)
	time.sleep(jtime)
	if oss == "Windows":
		os.system('cls')
	else:
		os.system('clear')
	
                            
