#!/bin/python
# -*- coding: utf-8 -*-
#Name : sLhideR
#Author : By Str4k
#Date : 2018-2019
#V1.3.0

#=======================================================================

from init_functions import colch,winch,bin2as,slh_exit
from main import get_imginfos,crypt_string
import os
def sLhDecoder(data):
	if mode_secured:
		try:
			data = crypt_string(reversed(base64.b64decode(bin2as("".join(data[:-len(pass_bal)])))),password,False)
			if "".join(data[-len(bin2as(password)):]) != bin2as(password): slh_exit(4)
			return data[:-len(bin2as(password))]
		except:
			slh_exit(4)
	else:
		return bin2as("".join(data[:-len(pass_bal)]))

def steg_detec():
	global linetoadd
	if steg[-len(pass_bal):] == pass_bal :
		os.system('clear') ; sLhDecoder(steg) #test pass err
		if mode_add:
			embed()
		elif mode_py: 
			colch("GREEN");print("\n[!] File found ! \n[*] Executing...\n\n");colch("NC")
			eval(compile(sLhDecoder(steg),'<string>','exec')) ; exit()
		elif mode_read:
				colch("GREEN");print("\n[!] File found ! \n[*] Reading...\n\n") ; colch("NC");print(sLhDecoder(steg))
				colch("RED");ans = raw_input("\n\n ENTER to exit...");colch("NC")
				os.system("clear");exit()
		else:
			f = open("{0}".format(outputname), "w"); f.write(sLhDecoder(steg));f.close()
			colch("GREEN");print("\n[!] File found ! [*] Saved as {}".format(outputname)); colch("NC");exit()

def getdata():
	global im, steg
	winch(15,84); os.system("clear"); colch("BLUE"); print("[*] Embedding... (secured mode)"); colch("NC")

	im, pix, cols, lines, dtsize = get_imginfos()
	steg = ''
	if mode_secured==True:
		count, pixnum =0,0
		while True:
			if pixnum==cols*lines: break
		#first line
			for x in range(count, cols-count):
				pixnum+=1
				for c in range(0,3):
					steg+= str(bin(pix[x,0+count][c])[2:]).zfill(8)[-2:]
					steg_detec()
		#line right going down
			for y in range(1+count,lines-count):
				pixnum+=1
				for c in range(0,3):
					steg+= str(bin(pix[cols-1-count,y][c])[2:]).zfill(8)[-2:]
					steg_detec()
		#line under going left
			for x in range(cols-2-count, 0+count, -1):
				pixnum+=1
				for c in range(0,3):
					steg+= str(bin(pix[x,lines-1-count][c])[2:]).zfill(8)[-2:]
					steg_detec()
		#line left going up
			for y in range(lines-1-count, 0+count, -1):
				pixnum+=1
				for c in range(0,3):
					steg+= str(bin(pix[0+count,y][c])[2:]).zfill(8)[-2:]
					steg_detec()
			count+=1
	else:
		for y in range(0, lines):
			for x in range(0, cols):
				for c in range(0,3):
					steg+= str(bin(pix[x,y][c])[2:]).zfill(8)[-2:]
					steg_detec()
	slh_exit(4)
