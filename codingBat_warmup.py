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

def parrot_trouble(b, time):
	if (time < 7 or time > 20) and b == True:
		return True
	else:
		return False

def makes10(a, b):
	if a == 10 or b == 10 or (a + b) == 10:
		return True
	else:
		return False

print(makes10(9, 10))
print(makes10(9, 9)) 
print(makes10(1, 9)) 

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))

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