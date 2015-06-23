#------------------------------------------------------------------------------ 
# Filename: logger.py
#
# Purpose:
#
# Author:      pbillava
#
# Created:     12-02-2015
# Copyright:   (c) pbillava 2015
# Licence:     <your licence>
#------------------------------------------------------------------------------
import time

def logger(message):
	'''
	This module will log all message passed to it
	FILENAME: is file where log should wrote
	message: content should be wrote into log
	'''
	fileptr=open(FILENAME,'a')
	now=time.strftime("%d-%m-%y %H:%M:%S")	
	msg=now+':'+message.replace('\n',' ')
	print msg
	fileptr.write(msg+'\n')
	fileptr.close()


if __name__ == "__main__":
	FILENAME="mylog.txt"
	logger("log check \n log check2")
	logger("log check 3")





