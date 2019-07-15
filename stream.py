#!/usr/bin/python -tt
# Python Boiler Plate
# 
# Streaming Audio Selector
# This uses  VLC media player to play selected Online Audio Streams
# 2019 rkeepers
# SOV: 0.01


import sys
import subprocess
import os
import time

FNULL = open(os.devnull, 'w')

def main():
	choice = 'y'
	# kill any running vlc procs
	#subprocess.Popen(['killall', '-9', 'vlc'], stdout=FNULL, stderr=subprocess.STDOUT)
	
	# Menu
	print( """
	1) Suburbs of Goa
	2) Secret Agent
	3) Groove Salad
	4) Illinois Street Lounge
	5) NPR
	x) Exit
	""")
	while choice != '':	
		choice=raw_input('Choose the stream you would like to play : ')
		if choice=="1":
			stream = 'https://somafm.com/suburbsofgoa.pls &'
		elif choice=="2":
			stream = 'http://somafm.com/secretagent.pls &'
		elif choice=="3":
			stream = 'http://somafm.com/groovesalad.pls &'
		elif choice=="4":	
			stream = 'http://somafm.com/illstreet.pls &'		
		elif choice=="5":	
			stream = 'https://live.wostreaming.net/direct/kplu-newsjazzaac-64?source=link &'	
		elif choice=="x":
			sys.exit()
		elif choice =="":
			print(" No Choice... exiting")
			#subprocess.Popen(['killall', '-9', 'vlc'], stdout=FNULL, stderr=subprocess.STDOUT)
			sys.exit()	
		elif choice !="":
			print(" Invalid Choice .. exiting")
			sys.exit()	
		
		# kill any running vlc procs
		subprocess.Popen(['killall', '-9', 'vlc'], stdout=FNULL, stderr=subprocess.STDOUT)
		# pause before starting a new vlc proc
		time.sleep(0.5)

		# open our stream with vlc and supress output of system info	
		subprocess.Popen(['cvlc', stream], stdout=FNULL, stderr=subprocess.STDOUT)

	
	# back to main
	
		
	sys.exit()
	
	
	
	
if __name__ == '__main__':
  main()	
