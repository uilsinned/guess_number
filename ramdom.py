#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入去猜
#猜對的話 印出 "終於猜對了"
#猜錯的話 要告訴他 比答案大/小

import random
password = random.randint(1, 100)
n = 0 #猜的次數
while True:
	n = n + 1
	p = input('請猜數字')
	if int(p) == password:
		print('正確,總共花了', n, "次")
		break
	else:
		if int(p) > password:
			print('太大囉')
		else:
			print('太小囉')
		print('這是你猜的第', n, '次')
