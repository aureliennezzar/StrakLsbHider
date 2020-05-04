#!/bin/python
# -*- coding: utf-8 -*-
#Name : sLhideR
#Author : By Str4k
#Date : 2018-2019
#V1.3.0

#=======================================================================

from init_functions import colch
def loadingbar(pc,color):
	colch("CYAN") ;print(sLh_logo+"\n\n\n")
	colch(color)
	if pc<=100 and pc>=98:
		print( "	     | ██████████████████████████████████████████████████ | [ {} % ]".format(pc))
	elif pc<98 and pc>=94:
		print( "	     | ████████████████████████████████████████████████   | [ {} % ]".format(pc))
	elif pc<94 and pc>=86:
		print( "	     | █████████████████████████████████████████████      | [ {} % ]".format(pc))
	elif pc<86 and pc>=80:
		print( "	     | ██████████████████████████████████████████         | [ {} % ]".format(pc))
	elif pc<80 and pc>=74:
		print( "	     | ███████████████████████████████████████            | [ {} % ]".format(pc))
	elif pc<74 and pc>=66:
		print( "	     | ████████████████████████████████████               | [ {} % ]".format(pc))
	elif pc<66 and pc>=60:
		print( "	     | █████████████████████████████████                  | [ {} % ]".format(pc))
	elif pc<60 and pc>=54:
		print( "	     | ██████████████████████████████                     | [ {} % ]".format(pc))
	elif pc<54  and pc>=48:
		print( "	     | ███████████████████████████                        | [ {} % ]".format(pc))
	elif pc<48  and pc>=42:
		print( "	     | ████████████████████████                           | [ {} % ]".format(pc))
	elif pc<42  and pc>=36:
		print( "	     | █████████████████████                              | [ {} % ]".format(pc))
	elif pc<36  and pc>=30:
		print( "	     | ██████████████████                                 | [ {} % ]".format(pc))
	elif pc<30 and pc>=24:
		print( "	     | ███████████████                                    | [ {} % ]".format(pc))
	elif pc<24  and pc>=18:
		print( "	     | ████████████                                       | [ {} % ]".format(pc))
	elif pc<18  and pc>=12:
		print( "	     | █████████                                          | [ {} % ]".format(pc))
	elif pc<12 and pc>=6:
		print( "	     | ██████                                             | [ {} % ]".format(pc))
	elif pc<6 and pc>=3:
		print( "	     | ███                                                | [ {} % ]".format(pc))
	elif pc<3:
		print( "	     |                                                    | [ {} % ]".format(pc))
	colch("NC");print("\n")