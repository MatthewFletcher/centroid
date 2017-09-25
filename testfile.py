#    _     _      _     _      _     _      _     _      _     _      _     _
#   (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)
#    / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \
#  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__
# (_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)
#    || O ||      || O ||      || O ||      || O ||      || O ||      || O ||
#  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._
# (.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)
#  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'

###########################################################################
#   Author:  Matt Fletcher                                                #
#      PID:  None                                                         #
#    Class:  MAE273 Statics 	                                          #
#  Helpers:  None                                                         #
#                                                                         #
#  Program:  Centroid of Polygon Calculator                               #
# Due Date:                                                               #
#                                                                         #
# Language:  Python 2.7.6                                                 #
#      IDE:  Python in Terminal                                           #
#                                                                         #
# Purpose:   Given GPS data for the sides of a shape, calculates the      #
#            centroid of the state.                                       #
#                                                                         #
#   "Bugs":  None                                                         #
#   "Undocumented features": None.                                        #
###########################################################################



#####################################################
#                     Imports						#
#####################################################
import csv

#####################################################
#                  Setup     						#
#####################################################



#Importing csv data 
with open("sampledata.csv", "r") as sampledataFile:
	sampledataReader = csv.reader(sampledataFile)
	sampledatalist = []

	for row in sampledataReader:
		if len(row) != 0: 
			sampledatalist = sampledatalist + [row]

sampledataFile.close
print (sampledatalist)
