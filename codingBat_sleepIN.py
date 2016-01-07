
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
