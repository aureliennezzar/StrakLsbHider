#!/bin/python
# -*- coding: utf-8 -*-
#Name : sLhideR
#Author : By Str4k
#Date : 2018-2019
#V1.3.0

#=======================================================================

try: 
	from PIL import Image
except:
	print("[!] Fatal Error, module 'PIL' is missing !")
import getpass, binascii, base64, os, time, sys, math, random



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
def get_imginfos():
	if mode_imgran:
		im = imagename
	else:
		im = Image.open(imagename)
	pix = im.load()
	cols, lines = im.size
	dtsize = cols * lines
	return im, pix, cols, lines, dtsize
def crypt_string(data,opass,mode):
	key =""
	nkey, count = 0,0
	data, dkey = list(data), list(bin2as(opass))
	for i in range(len(dkey)):
		try:
			int(dkey[i])/2
			key+=dkey[i]
		except:
			key+=str(ord(dkey[i]))
	key = list(key)
	for i in range(len(data)):
		mval = ord(data[i])
		kval= int(key[count])
		if mode:
			data[i] = chr(abs(mval-kval))
		else:
			data[i] = chr(abs(mval+kval))
		count+=1
		if count == len(key)-1:
			count = 0
	return "".join(data)








# -------------MAIN FUNCTION---------------------MAIN FUNCTION-----------MAIN FUNCTION
# -------------MAIN FUNCTION---------------------MAIN FUNCTION-----------MAIN FUNCTION
# -------------MAIN FUNCTION---------------------MAIN FUNCTION-----------MAIN FUNCTION

def main():
	global imagename, filetohide, outputname, mode_py, mode_read, mode_secured, mode_add, mode_imgran, password
	outputname = ""
	
	#BASIC

	if "-h" in sys.argv or "-help" in sys.argv or "--help" in sys.argv:
		helping() ; exit()

	#HIDE DATA
	if len(sys.argv)<3:
			slh_exit(1)
	try:
		if "-e" in sys.argv:
			if "-" in sys.argv[sys.argv.index("-e")+2] and len(sys.argv[sys.argv.index("-e")+2])<=4 and sys.argv[sys.argv.index("-e")+2][:4] != "-ran": slh_exit(2)
		if "-d" in sys.argv:
			if "-" in sys.argv[sys.argv.index("-d")+1] and len(sys.argv[sys.argv.index("-d")+1])<=4: slh_exit(2)
	except:
		slh_exit(2)
	if "-in" in sys.argv and "-e" not in sys.argv: slh_exit(2)
	if "-e" in sys.argv and len(sys.argv)==3: slh_exit(1)
	if "-e" in sys.argv and "-d" in sys.argv: slh_exit(2)
	if "-e" in sys.argv and "-r" in sys.argv: slh_exit(2)
	if "-e" in sys.argv and "-py" in sys.argv: slh_exit(2)
	if "-e" in sys.argv and "-exp" in sys.argv: slh_exit(2)
	if "-d" in sys.argv and "-exp" in sys.argv: slh_exit(2)
	if "-d" in sys.argv and "-in" in sys.argv: slh_exit(2)
	if "-add" in sys.argv and "-exp" in sys.argv: slh_exit(2)
	if "-add" in sys.argv and "-e" in sys.argv: slh_exit(2)
	if "-add" in sys.argv and "-d" in sys.argv: slh_exit(2)
	if "-py" in sys.argv and "-r" in sys.argv: slh_exit(2)
	if "-p" in sys.argv:
		colch("YELLOW") ;  password = as2bin(getpass.getpass('\n Enter password $')) ; colch("NC")

	if "-e" in sys.argv:
		colch("YELLOW") ; secans =  raw_input("\n[*] Secured process ? (y/n) $ "); colch("NC")
		if secans=="y": mode_secured = True
		if sys.argv[sys.argv.index("-e")+1]=="-in": 
			filetohide = True
		else:
			filetohide = sys.argv[sys.argv.index("-e")+1]
		try:
			if sys.argv[sys.argv.index("-e")+3][:2]== "o:":
				outputname = sys.argv[sys.argv.index("-e")+3][2:]
			else:
				outputname = defop_image
		except:
			outputname = defop_image
		if sys.argv[sys.argv.index("-e")+2][:4] =="-ran":
			mode_imgran = True
		else:
			imagename = sys.argv[sys.argv.index("-e")+2]
		embed()

	if "-d" in sys.argv:
		colch("YELLOW") ; secans =  raw_input("\n[*] Secured process ? (y/n) $ "); colch("NC")
		if secans=="y": mode_secured = True
		imagename = sys.argv[sys.argv.index("-d")+1]
		if "-r" in sys.argv:
			mode_read = True
		elif "-py" in sys.argv:
			mode_py = True
		else:
			try:
				if sys.argv[sys.argv.index("-d")+2][:2]== "o:":
					outputname = sys.argv[sys.argv.index("-d")+2][2:]
				else:
					outputname = defop_text
			except:
				outputname = defop_text
		getdata()

	#EXPORT
	if "-exp" in sys.argv:
		pswd1,pswd2,secureopt, moreopt, moreopt1="", "", "", "", ""
		os.system("clear")
		try:
			if sys.argv[sys.argv.index("-exp")+2][:2]== "o:":
				outputname = sys.argv[sys.argv.index("-exp")+2][2:]
			else:
				outputname = True
				slh_exit("")
		except:
			if outputname:
				slh_exit(2)
			else:
				outputname = defop_shell
		colch("YELLOW")
		if raw_input("[*] Read data ? (y/n) $ ")=="y": moreopt="-r"
		elif raw_input("[*] Execute python code ? (y/n) $ ")=="y":
			moreopt="-py"
		else:
			if raw_input("[*] Output file ? (y/n) $ ")=="y": moreopt1="o:"+raw_input("[*] Write output name wanted $ ")
		if raw_input("[*] Pass ? (y/n) $ ")=="y":
			pswd="-p"
		imagename = "'{}'".format(sys.argv[2])
		f = open(outputname, "w")
		f.write("""
#!/bin/bash
./sLh.py -d {0} {1} {3} {2}""".format(imagename,moreopt1, moreopt,pswd))
		f.close()
		os.system('chmod a+x {}'.format(outputname))
		colch("GREEN");print("\n[*]Shell created! saved as {}".format(outputname));colch("GREEN");exit()
	#ADD LINE
	if "-add" in sys.argv:
		colch("YELLOW") ; secans =  raw_input("\n[*] Secured process ? (y/n) $ "); colch("NC")
		if secans=="y": mode_secured = True
		imagename = sys.argv[sys.argv.index("-add")+1]
		mode_add = True
		getdata()
	slh_exit(2)









# -------------EMBED UTILITIES---------------------EMBED UTILITIES-----------EMBED UTILITIES
# -------------EMBED UTILITIES---------------------EMBED UTILITIES-----------EMBED UTILITIES

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

def dopix(coorx,coory):
	opx = "[!] Process done, output saved as {}".format(outputname)
	newR = int("{0}{1}{2}".format(str(bin(pix[coorx,coory][0])[2:]).zfill(8)[:6],file_txt[0],file_txt[1]),2);file_txt.pop(0);file_txt.pop(0) 
	if not len(file_txt): 
		pix[coorx,coory] = newR, int(pix[coorx,coory][1]), int(pix[coorx,coory][2]) #Create new pixel
		os.system("clear"); colch("GREEN");print(opx); colch("NC");loadingbar(100,"GREEN");colch("GREEN"); im.save(outputname) ; colch("NC");exit()
	newG = int("{0}{1}{2}".format(str(bin(pix[coorx,coory][1])[2:]).zfill(8)[:6],file_txt[0],file_txt[1]),2);file_txt.pop(0);file_txt.pop(0) 
	if not len(file_txt): 
		pix[coorx,coory] =  newR, newG, int(pix[coorx,coory][2]) #Create new pixel
		os.system("clear"); colch("GREEN");print(opx); colch("NC");loadingbar(100,"GREEN");colch("GREEN"); im.save(outputname) ; colch("NC");exit()
	newB = int("{0}{1}{2}".format(str(bin(pix[coorx,coory][2])[2:]).zfill(8)[:6],file_txt[0],file_txt[1]),2);file_txt.pop(0);file_txt.pop(0) 
	pix[coorx,coory] = newR, newG, newB #Create new pixel
	if not len(file_txt):
		os.system("clear"); colch("GREEN");print(opx); colch("NC");loadingbar(100,"GREEN");colch("GREEN"); im.save(outputname) ; colch("NC");exit()





# -------------EMBED FUNCTION---------------------EMBED FUNCTION-----------EMBED FUNCTION
# -------------EMBED FUNCTION---------------------EMBED FUNCTION-----------EMBED FUNCTION

def embed():
	global im, pix,file_txt, outputname, imagename
	winch(15,84); os.system("clear"); print("[*] Loading...\n")

	if filetohide == True or mode_add:
		winch(40,84)
		file_str=""
		edit_list = False
		edit_del = False
		i = 0
		while True:
			os.system("clear"); colch('CYAN');print("[INPUT] Strak's Lsb Hider                             [!h1/!del/!end/!abort/!help]"); colch('NC')
			i+=1
			print(file_str)
			if edit_list:
				file_add=raw_input(" {}. ".format(i))
			else:
				file_add=raw_input("")
			if file_add == "!end":
				os.system("clear")
				break
			elif file_add == "!h1":
				i = 0
				file_add=raw_input("\n[TITLE] : ")
				file_str+="\n\n{}\n".format(file_add)
			elif file_add == "!abort":
				slh_exit("[!] Aborting...")
			elif file_add == "!list":
				edit_list = not edit_list
				i = 0
			elif file_add == "!del":
				if i==1 and edit_list:
					edit_list = 0
				edit_del = True
				i-=2
				file_str = file_str.split("\n")
				file_str.pop(-1)
				for line in range(len(file_str)):
					if line != 0:
						file_str[line] = "\n"+file_str[line]
				file_str = "".join(file_str)
			elif file_add == "!help":
				i-=1
				colch('RED');print("\n !h1 : add title \n !del : Delete previous line \n !list : start/end list \n !end : Finish process\n !abort : Abort process\n"); colch('NC')
				raw_input("To continue, press ENTER...")
			elif edit_list:
				file_str+="\n {0}. {1}".format(i,file_add)
			else: file_str+="\n"+ file_add
	else:
		file_str = open(filetohide, "r").readlines()
	if mode_add:
		outputname = imagename
		file_str = "{0}\n{1}".format(sLhDecoder(steg),file_str)
	#ENCODAGE
	if mode_secured:
		file_str = as2bin(base64.b64encode(''.join(reversed(crypt_string(''.join(file_str)+bin2as(password),password,True)))))
		file_txt = list("".join(file_str)+pass_bal)
		len_file_txt = len(file_txt)
	else:
		file_str = as2bin(''.join(file_str))
		file_txt = list("".join(file_str)+pass_bal)
		len_file_txt = len(file_txt)
	#Image Random
	if mode_imgran:
		if len(sys.argv[sys.argv.index("-e")+2])<3: slh_exit(3)
		if sys.argv[sys.argv.index("-e")+2][4:]=="[a]":
			coor = 0
			while True:
				coor+=1
				var = coor * coor
				if var>=len_file_txt+5:
					coor = coor,coor
					break
		else:
			coor = sys.argv[sys.argv.index("-e")+2][5:-1].split(",")
		try:
			int(coor[0])+1;int(coor[1])+1
		except:
			slh_exit(3)
		x,y = int(coor[0]),int(coor[1])
		imagename = Image.new("RGB", (x,y))
		pix = imagename.load()
		colch("YELLOW") ;print("[*] Creating image..."); colch("NC") 
		for y in range(imagename.size[1]):
			for x in range(imagename.size[0]):
				pix[x,y] = random.choice(range(0,255)),random.choice(range(0,255)),random.choice(range(0,255))

	#Getting image infos
	im, pix, cols, lines, dtsize = get_imginfos()

	if len_file_txt>dtsize*3*2 - len(pass_bal):
		slh_exit("[!] Error : Data too big( {0} bits ) > Image( {1} bits ) ".format(len(file_txt),dtsize*3*2 - len(balise)))
	if mode_secured:
		count=0
		while True:
			os.system("clear")
			colch("BLUE");print("[*] Embedding... (secured mode)"); colch("NC")
			loadingbar(abs(100-(len(file_txt)*100/len_file_txt)),"BLUE")
		#first line
			for x in range(count, cols-count):
				dopix(x,0+count)
		#line right going down
			for y in range(1+count,lines-count):
				dopix(cols-1-count,y)
		#line under going left
			for x in range(cols-2-count, 0+count, -1):
				dopix(x,lines-1-count)
		#line left going up
			for y in range(lines-1-count, 0+count, -1):
				dopix(0+count,y)
			count+=1
	else:
		for y in range(0, lines):
			os.system("clear")
			colch("BLUE");print("[*] Embedding..."); colch("NC")
			loadingbar(abs(100-(len(file_txt)*100/len_file_txt)),"BLUE")
			for x in range(0, cols):
				dopix(x,y)








# -------------DECODE UTILITIES---------------------DECODE UTILITIES-----------DECODE UTILITIES
# -------------DECODE UTILITIES---------------------DECODE UTILITIES-----------DECODE UTILITIES
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




# -------------DECODE FUNCTION---------------------DECODE FUNCTION-----------DECODE FUNCTION
# -------------DECODE FUNCTION---------------------DECODE FUNCTION-----------DECODE FUNCTION
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















# -------------START FUNCTION---------------------START FUNCTION-----------START FUNCTION
# -------------START FUNCTION---------------------START FUNCTION-----------START FUNCTION
if (__name__ == "__main__"):
	os.system("clear")
	password , balise = as2bin("<PaSsWoRd>"), as2bin("<sLh>") ; pass_bal = password+balise
	mode_read, mode_py, mode_secured,mode_add, filetohide, mode_imgran = False, False, False, False, False, False
	defop_text, defop_image, defop_shell  = "output-sLh.txt", "image-sLh.png" , "export-sLh.sh"
	sLh_logo = """

                           _     _     _     _      ____  
                       ___| |   | |__ (_) __| | ___|  _ \\ 
                      / __| |   | '_ \\| |/ _` |/ _ \\ |_) |
                      \\__ \\ |___| | | | | (_| |  __/  _ < 
                      |___/_____|_| |_|_|\\__,_|\\___|_| \\_\\    v1"""
	main()



#COLOR HELP

#	Black        0;30     Dark Gray     1;30
#Red          0;31     Light Red     1;31
#Green        0;32     Light Green   1;32
#Brown/Orange 0;33     Yellow        1;33
#Blue         0;34     Light Blue    1;34
#Purple       0;35     Light Purple  1;35
#Cyan         0;36     Light Cyan    1;36
#Light Gray   0;37     White         1;37