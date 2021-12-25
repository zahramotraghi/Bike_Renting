
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



from Loading import Ui_Loading
from User_input import Ui_User_input
from Hourly_Rent import Ui_Hourly_Rent
from Daily_Rent import  Ui_Daily_Rent
from Weekly_Rent import Ui_Weekly_Rent
from Return_Show import Ui_Return_Show

totalBikes = 200
Counter = 30
rentedBikes = 0
availableBikes = 0
rentedHours = 0
rentedDays = 0
rentedWeeks = 0
bill = 0
opH = False
opD = False
opW = False

# --------------------------------------------------------
class RootLoading(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Loading()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(50)
        self.show()


    def progress(self):
        global Counter
        self.ui.progressBar.setValue(Counter) 

        if Counter > 100:
            self.timer.stop()

            self.User1 = RootUserInput()
            self.User1.show()
            self.close()

        Counter += 1

# --------------------------------------------------------
class RootUserInput(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_User_input()
        self.ui.setupUi(self)
        self.tbikes = totalBikes
 
        self.ui.radioButton_1.toggled.connect(self.op1_func)
        self.ui.radioButton_2.toggled.connect(self.op2_func)
        self.ui.radioButton_3.toggled.connect(self.op3_func)
        self.ui.radioButton_4.toggled.connect(self.op4_func)
        self.ui.radioButton_5.toggled.connect(self.op5_func)
        self.show()
     

    def op1_func(self):
        if self.ui.radioButton_1.isChecked()==True:
           self.ui.label_m1.setText("We have currently {} bikes available to rent.".format(self.tbikes)) 


    def op2_func(self):
        self.Hourly1 = RootHourly()
        self.Hourly1.show()
        self.close()
 

    def op3_func(self):
        self.Daily1 = RootDaily()
        self.Daily1.show()
        self.close()


    def op4_func(self):
        self.Weekly1 = RootWeekly()
        self.Weekly1.show()
        self.close()


    def op5_func(self):
        if self.ui.radioButton_5.isChecked()==True:
           self.ui.label_m1.setText("You have not rented a bike yet!") 


# --------------------------------------------------------
class RootHourly(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Hourly_Rent()
        self.ui.setupUi(self)    
      
        self.ui.label_m1.setText("How many bikes would you like to rent?  ")
        self.ui.label_m2.setText("How many hours would you like to rent?  ")

        self.clickFunc()


    def clickFunc(self) :
        self.ui.pushButton_confirm.clicked.connect(self.get_input)


    def get_input(self) :
        bnumbers =  self.ui.lineEdit_1.text().strip()
        hnumbers =  self.ui.lineEdit_2.text().strip()

        global opH
        opH = True

        if bnumbers is None or bnumbers == '' or not bnumbers :
           QMessageBox.about(self, 'Error', 'Enter the  number of bikes!')
           return None

        if int(bnumbers) < 1 :
            QMessageBox.about(self, 'Error', 'Number of bikes should be greater than zero! ')
            return None

        if int(bnumbers) > totalBikes :
            QMessageBox.about(self, 'Error', 'Number of available bikes is: {}'.format(totalBikes))
            return None    

        if hnumbers is None or hnumbers == '' or not hnumbers :
           QMessageBox.about(self, 'Error', 'Enter the  number of hours!')
           return None

        if int(hnumbers) < 1 :
            QMessageBox.about(self, 'Error', 'Number of hours should be greater than zero!')
            return None

        global rentedBikes
        rentedBikes = int(bnumbers)

        global rentedHours
        rentedHours = int(hnumbers)

        self.Return_Show1 = RootReturn_Show()
        self.Return_Show1.show()
        self.close()


# --------------------------------------------------------
class RootDaily(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Daily_Rent()
        self.ui.setupUi(self)    
      
        self.ui.label_m1.setText("How many bikes would you like to rent?  ")
        self.ui.label_m2.setText("How many days would you like to rent?  ")

        self.clickFunc()


    def clickFunc(self) :
        self.ui.pushButton_confirm.clicked.connect(self.get_input)


    def get_input(self) :
        bnumbers =  self.ui.lineEdit_1.text().strip()
        dnumbers =  self.ui.lineEdit_2.text().strip()

        global opD
        opD = True

        if bnumbers is None or bnumbers == '' or not bnumbers :
           QMessageBox.about(self, 'Error', 'Enter the  number of bikes!')
           return None

        if int(bnumbers) < 1 :
            QMessageBox.about(self, 'Error', 'Number of bikes should be greater than zero! ')
            return None

        if int(bnumbers) > totalBikes :
            QMessageBox.about(self, 'Error', 'Number of available bikes is: {}'.format(totalBikes))
            return None  

        if dnumbers is None or dnumbers == '' or not dnumbers :
           QMessageBox.about(self, 'Error', 'Enter the  number of days!')
           return None

        if int(dnumbers) < 1 :
            QMessageBox.about(self, 'Error', 'Number of days should be greater than zero!')
            return None

        global rentedBikes
        rentedBikes = int(bnumbers)

        global rentedDays
        rentedDays = int(dnumbers)

        self.Return_Show1 = RootReturn_Show()
        self.Return_Show1.show()
        self.close()


# --------------------------------------------------------
class RootWeekly(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Weekly_Rent()
        self.ui.setupUi(self)    
      
        self.ui.label_m1.setText("How many bikes would you like to rent?  ")
        self.ui.label_m2.setText("How many weeks would you like to rent?  ")

        self.clickFunc()


    def clickFunc(self) :
        self.ui.pushButton_confirm.clicked.connect(self.get_input)


    def get_input(self) :
        bnumbers = self.ui.lineEdit_1.text().strip()
        wnumbers = self.ui.lineEdit_2.text().strip()

        global opW
        opW = True

        if bnumbers is None or bnumbers == '' or not bnumbers :
           QMessageBox.about(self, 'Error', 'Enter the  number of bikes!')
           return None

        if int(bnumbers) < 1 :
            QMessageBox.about(self, 'Error', 'Number of bikes should be greater than zero! ')
            return None

        if int(bnumbers) > totalBikes :
            QMessageBox.about(self, 'Error', 'Number of available bikes is: {}'.format(totalBikes))
            return None  

        if wnumbers is None or wnumbers == '' or not wnumbers :
           QMessageBox.about(self, 'Error', 'Enter the  number of weeks!')
           return None

        if int(wnumbers) < 1 :
            QMessageBox.about(self, 'Error', 'Number of weeks should be greater than zero!')
            return None

        global rentedBikes
        rentedBikes = int(bnumbers)

        global rentedWeeks
        rentedWeeks = int(wnumbers)

        self.Return_Show1 = RootReturn_Show()
        self.Return_Show1.show()
        self.close()


# --------------------------------------------------------     
class RootReturn_Show(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Return_Show()
        self.ui.setupUi(self)   
        self.tbikes = totalBikes 
        self.rentedbikes = rentedBikes
        self.availablebikes = availableBikes
        self.bill = bill
        
        self.availablebikes = self.tbikes -  self.rentedbikes

        self.ui.radioButton_1.toggled.connect(self.op1_func)
        self.ui.radioButton_5.toggled.connect(self.op5_func)    


    def op1_func(self):
        if self.ui.radioButton_1.isChecked()==True:
           self.ui.label_m1.setText("We have currently {} bikes available to rent.".format(self.availablebikes))
           self.ui.label_m2.setText("")
           self.ui.label_m3.setText("") 


    def op5_func(self):   
        self.availablebikes = self.tbikes
        self.ui.label_m1.setText("Thank you for using Bike Rental System.")
        
        if opH:
            self.bill = rentedHours * 5 * rentedBikes
            str = ("(%s Bikes for %s Hours):  "%(rentedBikes,rentedHours))

        if opD:
            self.bill = rentedDays * 20 * rentedBikes
            str = ("(%s Bikes for %s Days):  "%(rentedBikes,rentedDays))

        if opW:
            self.bill = rentedWeeks * 60 * rentedBikes  
            str = ("(%s Bikes for %s Weeks):  "%(rentedBikes,rentedWeeks))     

        if (3 <= rentedBikes):

            self.bill = self.bill * 0.5
            self.ui.label_m2.setText("%50 discount for renting more than 2 bikes!")
            self.ui.label_m3.setText(str + "Your bill is: ${}".format(self.bill))
        else:
            self.ui.label_m2.setText(str + "Your bill is: ${}".format(self.bill))



# --------------------------------------------------------
if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)  
    Root = RootLoading()
    sys.exit(app.exec_())