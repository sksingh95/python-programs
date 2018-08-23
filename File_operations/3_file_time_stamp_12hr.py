#!/usr/bin/env python
import time

def main():
	cur_time = time.strftime("%d_%m_%Y_%I_%M_%S_%p")
	
	file = open("log_" + cur_time + ".txt", "w")
	
	file.write("log line .....\n")
	
	file.close()



if __name__ == "__main__":
	main()
