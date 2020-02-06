import time


def Timer(timer):
	while True:
		minutes,seconds=divmod(timer,60)
		t = '{:02d}:{:02d}'.format(minutes,seconds)
		print(t, end = '\r')
		timer -= 1
		time.sleep(1)	
		if timer == 0:
			break

timer = int(input("Enter time in seconds: "))
print("Timer set for: ",timer,"seconds")
Timer(timer)
