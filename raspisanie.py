# !! on linux only !!
import os
import urllib.request
import subprocess
import re
import csv
import datetime
import camelot
# -------------functions------------
def getCsv():#function from NET
	tables = camelot.read_pdf('rasp.pdf')
	tables
	# <TableList n=1>
	tables.export('foo.csv', f='csv', compress=True) # json, excel, html, sqlite
	tables[0]
	# <Table shape=(7, 7)>
	tables[0].parsing_report
	{
	    'accuracy': 99.02,
	    'whitespace': 12.24,
	    'order': 1,
	    'page': 1
	}
	tables[0].to_csv('rasp.csv') # to_json, to_excel, to_html, to_sqlite
	tables[0].df # get a pandas DataFrame!
def getUrl(line):
	i=0
	while(i<len(line)-8):
		if line[i]=='<' and line[i+1]=='a' and line[i+2]==' ' and line[i+3]=='h' and line[i+4]=='r' and line[i+5]=='e' and line[i+6]=='f' and line[i+7]=='=':
			i+=9
			res=''
			while(line[i]!='\"'):
				res+=line[i]
				i+=1
				if line[i]=='&' and line[i+1]=='a' and line[i+2]=='m' and line[i+3]=='p':
					break
		i+=1
	print(res)
	return res
#-----------------main----------------
now=int(input("Today (1) or Custom date (0)? "))
if now:
	now = datetime.datetime.now().strftime("%d.%m.%Y")
	print("Today: "+now)
else:
	now=input("Ent date in format 'DD.MM.YYYY : ")
link=urllib.request.urlopen('http://www.mgkit.ru/studentu/raspisanie-zanatij')
#go to url and open html file
print("step1")
lines = []
for line in link.readlines():
	if line.find(now.encode('utf-8')) != -1: # find files now date
		lines.append(line.decode('utf-8')) #save strings with links
for i in range(len(lines)):
	lines[i]=getUrl(lines[i]) # save oll lonks

# print('finded', len(lines), 'files. get 1-st')
# for i in range(len(lines)):
# 	print("link ", i+1, ines[i])

link.close()
if len(lines)==0:
	print("not found :( I use last save")
else:
	os.system('wget -O rasp.pdf '+'http://www.mgkit.ru'+lines[0]+' @') # get file 
print("step2")
print()
getCsv() #convert pdf to csv
# os.system('python3 pdf2table.py') #crated rasp.csv
mass=[]

findGroup=input("Введите номер группы: ")

with open('rasp.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        mass.append(row)
#save csv to mass[][] : 1st arg - line, 2nd arg - column
for i in range(len(mass)):
	for j in range(len(mass[i])):
		if re.search(r""+findGroup, mass[i][j])!=None and re.search(r"[0-9][0-9]:[0-9][0-9]", mass[i][0])!=None:
			print()
			print(mass[i][0])
			for k in range(4):
				print(mass[i+k][j])
# for i in range(len(mass)):
# 	print(mass[i], i)
#   (')
#   | |
#   | |
#   | |
# ( )_( )