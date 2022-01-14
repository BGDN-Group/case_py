#!/usr/bin/python3

date = str(input("Enter date: "))

if date == '1':
	print("Today is Monday!")
	raise SystemExit
elif date == '2':
	print("Today is Tuesday!")
	raise SystemExit
elif date == '3':
	print("Today is Wednesday!")
	raise SystemExit
elif date == '4':
	print("Today is Thursday!")
	raise SystemExit
elif date == "5":
	print("Today is Friday!")
	raise SystemExit
elif date == "6":
	print("Today is Saturday!")
	raise SystemExit
elif date == "7":
	print("Today is Sunday!")
	raise SystemExit
else:
	print("Error!")
	raise SystemExit