# A POPUP ALERT NOTIFICATION PROGRAM USING PYQT5
import sys
import time
from PyQt5.QtCore import * #QtCore module contains non-GUI functionality for working with file and directory etc.
from PyQt5.QtWidgets import *
from playsound import playsound # alerting the person with music 

app = QApplication(sys.argv) #sys.srgs are command line arguments

due = input("Enter Time for Alert : ")
message = input("Enter Message for Alert : ")

try:
	hours, mins = due.split(":")
	due = QTime(int(hours), int(mins))
	if not due.isValid():
		raise ValueError
except ValueError:
	message = "Time entered is not a valid time"

while QTime.currentTime() < due:
	pass

label = QLabel("<font color=red size=72><b>" + message + "</b></font>")	
label.setWindowFlags(Qt.SplashScreen)
label.show() #show the window
playsound("/home/lalit/Downloads/service-bell_daniel_simion.mp3")
QTimer.singleShot(6000, app.quit)
sys.exit(app.exec_())