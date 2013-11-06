"""
This script checks for the screen name that are in the dataSet of tweets2009-06.txt. Takes the screen name and store it in the dictionary screenNameDataSet.  numeric2screen has 2 columns. The first column is the userNumber  and the second column is the screen name. 

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
		if len(screenName)>=20:
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

     


