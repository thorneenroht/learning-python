def diff21(n):
	if n > 21:
		sum = n - 21
		return sum * 2
	else:
		return 21 - n


def sum_double(a, b):
	if a == b:
		return (a + b)* 2
	else:
		return a + b



def monkey_trouble(a , b):
	if a == b:
		return True
	else:
		return False

def sleepIn(weekday, vacation):
	if weekday == False and vacation == False:
		return True
	elif weekday == True and vacation == False:
		return False
	elif weekday == False and vacation == True:
		return True

print(sleepIn(False, True))
print(sleepIn(True, False))
print(sleepIn(False, False))


print(monkey_trouble(True, True))
print(monkey_trouble(False,False))
print(monkey_trouble(True,False))

print(sum_double(1,2))
print(sum_double(3,2))
print(sum_double(2,2))


print(diff21(10))
print(diff21(21))
print(diff21(25))