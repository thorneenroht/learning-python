print("Hello");

counter = 0
while(counter < 101):
	
	if counter % 15 == 0:
		print("fizzbuzz");
	elif counter % 3 == 0:
		print("fizz");
	elif counter % 5 == 0:
		print("buzz");
	else:
		print counter

	counter = counter + 1

