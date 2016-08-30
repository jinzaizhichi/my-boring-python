import datetime,time,os

while 1<2 :
	a = datetime.datetime.now()
	b = datetime.datetime.strptime('2016-08-31  14:00:00', '%Y-%m-%d %H:%M:%S')
	c = datetime.datetime.strptime('2016-09-15  00:00:00', '%Y-%m-%d %H:%M:%S')
	d = datetime.datetime.strptime('2016-10-01  00:00:00', '%Y-%m-%d %H:%M:%S')
	e = datetime.datetime.strptime('2017-01-01  00:00:00', '%Y-%m-%d %H:%M:%S')
	print('距离暑假结束只剩下')
	print (b-a)
	print('距离16年中秋节还有')
	print (c-a)
	print('距离16年国庆还有')
	print (d-a)
	print('距离17年元旦还有')
	print (e-a)
	time.sleep(0.05)
	os.system('clear')
                            
