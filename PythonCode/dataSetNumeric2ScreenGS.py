"""
This script checks for the screen name that are in the dataSet of tweets2009-06.txt. Takes the screen name and store it in the dictionary screenNameDataSet.  numeric2screen has 2 columns. The first column is the userNumber  and the second column is the screen name. 

I AM WORKING JUST WITH THE FIRST 1000000 LINES
----------------------
keep getting this error
Traceback (most recent call last):
  File "dataSetAndnumeric2screen.py", line 30, in <module>
    wfile.write(screenName[1])
IndexError: list index out of range

when I run these lines
  if line[0] == 'U':
        screenName = line[1]
        screenName = screenName.split('http://twitter.com/')
		wfile.write(screenName[1])
---->it was because the U line of the tweets2009-06.txt is not complete that was why I got that errror
----> indexError I fixed by using operator module	
		
-----------------------------

"""
import operator
# Load stop words into a stopWords dictionary

###############################GETTING SCREENNAMES###################################
###Getting the screenNames from the dataset,writing to a file and storing them in the dataSetScreenName dictionary

dataSetScreenName = {}
dataSetFile = open('sampleTweets2009-06.txt')#file that contains the data set are
wfile = open('outputScreenNameTry.txt', 'w')
lineNum=0

#just reads the 1000000 lines
while dataSetFile and lineNum < 1000000:
	lineNum+=1
	if operator.mod(lineNum,1000000) == 0:
		print lineNum
		
	line = dataSetFile.readline()
    #Stop if line is empty
	if len(line) == 0:
		break
    #Split line by tabs
	line = line.split('\t')

	# It is checking the U line which has the user's screenName of the dataset
	if line[0] == 'U':
		screenName = line[1]
		screenName=str(line[1])
		if len(screenName)>=20:# this line is unnessesary because all U lines have http://twitter.com/
			screenName = screenName.split('http://twitter.com/')
			screenName=str(screenName[1])
			screenName=screenName.split('\n')
        	
        	#screenNames are written in the outputScreenName.txt file
			wfile.write(screenName[0])
			wfile.write('\n')
			
			#screenName[0] is converted to be a string
			screenName=str(screenName[0])
        	
        	#store the screenName just once in the dataSetScreenName
        	if screenName not in dataSetScreenName:
				dataSetScreenName[screenName] = 1
      
print dataSetScreenName
wfile.close()
dataSetFile.close()
############################################################################################## 
#####################PUTTING TOGETHER SCREENNAME & USERID###################################	
numeric2screenFile = open('sampleMyScreen2Name.txt')
dataSetWithNumerID= open('outputDataSetWithNumberIDTry.txt','w')
while numeric2screenFile and lineNum < 1000000:
	#reading just the first 1000000 lines
	lineNum+=1
	#reads a line	
	line = numeric2screenFile.readline()
    #Stop if line is empty
	if len(line) == 0:
		break
    #Split line by tabs
	line = line.split()
	
	if line[1] in dataSetScreenName:
		dataSetScreenName[line[1]]=line[0]
		#line[0] has the ID number and line[1] has the screen name 
		dataSetWithNumerID.write('%s %s' %(line[0],line[1]))
		dataSetWithNumerID.write('\n')
      
#print 'new datasetwirhscreenname', dataSetScreenName
numeric2screenFile.close()
dataSetWithNumerID.close()

############################################################################################## 
     

     
     
     
     
     
     
     
     
     
     


