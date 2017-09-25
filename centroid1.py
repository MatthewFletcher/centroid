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
import matplotlib.pyplot as plt
#####################################################
#                  Setup     						#
#####################################################

#Set empty list for coordinates
lat,lon =[],[]

#Importing csv data 
with open("Alabama.csv", "r") as AlabamaFile:
	AlabamaReader = csv.reader(AlabamaFile)
	Alabamalist = []

	#Import data as float instead of string
	for row in AlabamaReader:
		#While the rows have data, AKA length not equal to zero. 
		if len(row) != 0: 
			lat.append(100 * (180 + float(row[0])) / 360)
			lon.append(100 * (90 - float(row[1])) / 180)

#Close file as importing is done
AlabamaFile.close

#print (lat)

 
#The coordinates used in the above file are GPS coordinates. 
#When plotted as x,y coordinates, it results in a skewed value for the state
#Therefore, this next step uses the Equidistant Cylindrical Projection type map
#This will attempt to turn the coordinates into an approximation

#Equations used
#x = (total width of image in px) * (180 + latitude) / 360
#y = (total height of image in px) * (90 - longitude) / 180



#Plot data 
plt.plot(lat,lon, "o")
plt.show()
