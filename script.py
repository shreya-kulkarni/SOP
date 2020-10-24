import os.path
import pandas as pd
import sys
import copy
from sendmail import sendMail

ACB_BACKLOG_LIST = 'ACBBACKLOG.xls'
PENDING_BACKLOG = "Pending Backlog.xls"  

def checkstatus(id):
	ACB = pd.read_excel(ACB_BACKLOG_LIST)
	flag=0
	for i in range(len(ACB['Campus ID'])):
		print (ACB['Campus ID'][i])
		if(ACB['Campus ID'][i]==id):
			flag=flag+1
		
	if(flag):
		print("The given student is ACB candidate")
	else:
		print("The student is a normal candidate")

def getBacklogs(id):
	#print ("*")
	course=[]
	BACK=pd.read_excel(PENDING_BACKLOG)
	#course={}
	for i in range(len(BACK['Campus ID'])):
		if(BACK['Campus ID'][i]==id):
			course.append((BACK['Course ID'],BACK['Course Name']))

	
	#print (len(course))
	for i in range(len(course)):
		print (course[i][0]+" "+course[i][1])

def main():

		id = (input('Enter the ID: '))
			#eval function to be added in py3
		print("For checking acb status type acb"+'\n');
		print("For checking backlogs status type backlogs"+'\n');
		print ("For sending student mail enter send mail")
		#id="2018A1PS0002G"
		if(True):
			query = (input())
			#if(query=="done"):
				#break
			if(query=="backlogs"):
				getBacklogs(id)
			if(query=="acb"):
				checkstatus(id)
			if(query=="sendmail"):
				sendMail("soptestmailacb@gmail.com")

	

if __name__ == '__main__':
	main()
