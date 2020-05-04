#!/bin/python
# -*- coding: utf-8 -*-
#Name : sLhideR
#Author : By Str4k
#Date : 2018-2019
#V1.3.0

#=======================================================================

# -------------SCREEN/COLOR FUNCTIONS---------------------SCREEN/COLOR FUNCTIONS-----------SCREEN/COLOR FUNCTIONS
# -------------SCREEN/COLOR FUNCTIONS---------------------SCREEN/COLOR FUNCTIONS-----------SCREEN/COLOR FUNCTIONS

def winch(x,y):
	lin,col = x,y ; os.system("printf '\\e[8;{0};{1}t'".format(lin,col))
def colch(color):
	if color =="RED":
		os.system("RED='\033[0;31m'; printf ${RED}")
	elif color =="GREEN":
		os.system("GREEN='\033[1;32m'; printf ${GREEN}")
	elif color =="BLUE":
		os.system("BLUE='\033[0;34m'; printf ${BLUE}")
	elif color =="CYAN":
		os.system("CYAN='\033[1;36m'; printf ${CYAN}")
	elif color=="YELLOW":
		os.system("YELLOW='\033[1;33m' ; printf ${YELLOW}")
	elif color=="NC":
		os.system("NC='\033[0m' ; printf ${NC}")
	else:
		os.system("OC='\033[{0}m' ; printf ${{OC}}".format(color))

# -------------HELP WINDOW FUNCTIONS---------------------HELP WINDOW FUNCTIONS-----------HELP WINDOW FUNCTIONS
# -------------HELP WINDOW FUNCTIONS---------------------HELP WINDOW FUNCTIONS-----------HELP WINDOW FUNCTIONS

def helping():
	os.system("clear")
	colch("BLUE");print("[HELP] Strak's Lsb Hider                                                     v1.3.0")
	colch("CYAN"); print(sLh_logo);colch("BLUE")
	print("""
Usage:  ./sLh.py [options]
	*Optional""")
	colch("NC")
	print("""
 Embedding options : 
	-e DATA IMAGE *o:OUTPUT	 Embed file in an image
	-d IMAGE *o:OUTPUT	 Extract file from an image

 Dependent options :
	-p         		 Use passwords ' With -e, -d and -add'
	-ran[x,y]		 Use random image (instead of IMAGE while using -e)
	-in			 Input data. (instead of DATA while using -e)
	-r			 Read output without creating files (only with -d)
	-py			 Execute output as python code (only with -d)

 Console options : 
	-exp IMAGE *o:OUTPUT	 Create automatic decode file
	-add IMAGE		 Add line to an encoded image
	-h			 Show this message
""")
	winch(29,84)





# -------------HELPFUL FUNCTIONS---------------------HELPFUL FUNCTIONS-----------HELPFUL FUNCTIONS
# -------------HELPFUL FUNCTIONS---------------------HELPFUL FUNCTIONS-----------HELPFUL FUNCTIONS

def slh_exit(n):
	os.system("clear")
	colch("RED")
	if n ==1: print("[!] Error, more arguments needed, try -h to display the help window.")
	elif n ==2: print("[!] Error, wrong argument(s) {}, try -h to display the help window.".format(sys.argv[1:]))
	elif n ==3: print("[!] Error , coordonates expected...(ex: ' -ran[x,y] ' )")
	elif n ==4: print("[!] Error, nothing found !")
	else: 
		print(n)
	colch("NC");exit()
def bin2as(n):
	return binascii.unhexlify('%x' % int('0b' + '{}'.format(n), 2))
def as2bin(n):
	return "".join([format(ord(char),'#010b')[2:] for char in n])