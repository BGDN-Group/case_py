#!/usr/bin/python3

K = int(input("Enter number : "))

if K == 1:
	print("Bad!")
	raise SystemExit
elif K == 2:
	print("unsatisfactory!")
	raise SystemExit
elif K == 3:
	print("satisfactorily!")
	raise SystemExit
elif K == 4:
	print("Good!")
	raise SystemExit
elif K == 5:
	print("Excellent!")
	raise SystemExit
else:
	print("Error!")
	raise SystemExit