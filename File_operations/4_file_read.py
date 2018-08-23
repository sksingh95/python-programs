#!/usr/bin/env python
import time

file_name = "list.txt"
line_list = []

def main():
	with open(file_name, "r") as file:
		for line in file:
			line = line.rstrip("\n")	# Remove last "Enter" char
			print(line)
			line_list.append(line)	# Store each line of file in list

	print("\n\nPrinting List....\n")
	print(line_list)



if __name__ == "__main__":
	main()
