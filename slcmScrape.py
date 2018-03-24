import requests
import smtplib
import threading
import sys
from bs4 import BeautifulSoup
path='slcmData.txt'
file = open(path,'w') 
 

opt=int(input('Individual search(0) or Group Search(1)? : '))
if opt==1:
	i=int(input('Enter Starting Roll number: '))
	limit=int(input('Enter number of ID needed: '))

	j=0
	print('REG NO','            ','NAME','               ','BLOCK','             ','COLLEGE','                          ','MESS DUES')
	print('------------------------------------------------------------------------------------------------------------')
	

	while j<limit:	
		
		link='http://sis.manipal.edu/HostelduesSLCM.aspx?roll='+str(i)
		page= requests.get(link)
		soup= BeautifulSoup(page.content, 'html.parser')
		name=soup.find_all(id="ctl00_ContentPlaceHolder1_lblname")[0].get_text()
		if(len(name)>0):
			block=soup.find_all(id="ctl00_ContentPlaceHolder1_lblblock")[0].get_text()
			college=soup.find_all(id='ctl00_ContentPlaceHolder1_LblInst2')[0].get_text()
			try:
				hosteldue=soup.find_all(id='ctl00_ContentPlaceHolder1_GridView5_ctl10_lbl_amtbalance5')[0].get_text()
			except IndexError:
				hosteldue='NOT FOUND'
			s1=str((25-len(name))*' ')
			s2=str((15-len      (block))*' ')
			info=str(str(i)+"  "+str(name)+str(s1)+str(block)+str(s2)+str(college)+"     "+hosteldue+'\n')
			file.write(info)
			print(info)
			j=j+1
		i=i+1

if opt==0:
		i=input('Enter Roll number: ')
		print(' ')
		link='http://sis.manipal.edu/HostelduesSLCM.aspx?roll='+str(i)
		page= requests.get(link)
		soup= BeautifulSoup(page.content, 'html.parser')
		name=soup.find_all(id="ctl00_ContentPlaceHolder1_lblname")[0].get_text()

		if(len(name)>0):
			block=soup.find_all(id="ctl00_ContentPlaceHolder1_lblblock")[0].get_text()
			college=soup.find_all(id='ctl00_ContentPlaceHolder1_LblInst2')[0].get_text()
			try:
				hosteldue=soup.find_all(id='ctl00_ContentPlaceHolder1_GridView5_ctl10_lbl_amtbalance5')[0].get_text()
			except IndexError:
				hosteldue='NOT FOUND'
			s1=str((25-len(name))*' ')
			s2=str((15-len      (block))*' ')	
			print("-----------------------------------------------------------------------------")
			print('NAME:',name)
			print('REG NO:', i)
			print('HOSTEL:', block)
			print('MESS DUES: Rs.',hosteldue)
			print("-----------------------------------------------------------------------------")
		else:
			print('NO STUDENT ON THIS ROLL NO.')
			print(' ')
 
file.close() 