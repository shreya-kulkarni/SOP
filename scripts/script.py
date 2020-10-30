import os.path
import pandas as pd
import sys
import copy
from sendmail import sendMail
 
ACB_BACKLOG_LIST = 'ACBBACKLOG.xls'
PENDING_BACKLOG = "Pending Backlog.xls"  

data = pd.read_excel('./data.xlsx')

def getGrade(idNumber, subject, catalog):

	found = False
	grade = "NA"
	for i in range (0, data.shape[0]):
		if ( data.iloc[i][1] == idNumber and data.iloc[i][6] == subject and data.iloc[i][7] == catalog ):
			found = True
			grade = data.iloc[i][9]

	if ( found == True ) :
		print( "Student has secured ", grade, "in ", subject, catalog  )

	else :
		print( "Student has not taken the course" )

def getCGPA(idNumber):

	gradeMapping = {'A':10,'A-':9,'B':8,'B-':7,'C':6,'C-':5,'D':4,'E':2}

	tot = 0
	units = 0
	found = False

	for i in range (0, data.shape[0]):
		if ( data.iloc[i][1] == idNumber ):
			found = True
			if ( data.iloc[i][9] == "NC" or data.iloc[i][9] == "Poor" or data.iloc[i][9] == "Good" 
				or data.iloc[i][9] == "W" or data.iloc[i][9]=="" or pd.isnull(data.iloc[i][9])):
				continue
			else :
				tot+=gradeMapping[data.iloc[i][9]]*data.iloc[i][8]
				units+=data.iloc[i][8]

	if ( found == False ) :
		print("Student not found")

	else :
		print( "CGPA : ", tot/units )


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

def checkPS(idNumber):
	
	flag1 = False
	flag2 = False
	grade1 = " "
	grade2 = " "

	for i in range (0, data.shape[0]):
		if ( data.iloc[i][1] == idNumber ):
			if ( data.iloc[i][5] == "PRACTICE SCHOOL I" ):
				flag1 = True		
				grade1 = data.iloc[i][9]
			if ( data.iloc[i][5] == "PRACTICE SCHOOL II" ):
				flag2 = True		
				grade2 = data.iloc[i][9]

	if ( flag1 == True ):
		print("Student has completed PS I with the grade ", grade1)

	if ( flag2 == True ):
		print("Student has completed PS II with the grade ", grade1)		

	if ( not flag1 and not flag2 ):
		print("No data found")

def main():

		id = (input('Enter the ID: '))
			#eval function to be added in py3
		print("For checking acb status type acb"+'\n')
		print("For checking backlogs status type backlogs"+'\n')
		print("For sending student mail enter send mail"+'\n')
		print("For checking PS status, type PS "+'\n')
		print("For checking CGPA, type CGPA"+'\n')
		print("For checking grade in a particular subject, type grade followed by concerned subject abbreviation and course code, for example : PHY F110"+'\n') 
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
			if(query=="grade"):
				subject = (input('Enter the subject: '))
				catalog = (input('Enter the catalog: '))
				getGrade(id,subject,catalog)
			if(query=="CGPA"):
				getCGPA(id)
			if(query=="PS"):
				checkPS(id)

	

if __name__ == '__main__':
	main()
