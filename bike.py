

class RentBike:
    
    def __init__(self,totalbikes=0):

        self.totalbikes = totalbikes

    def show_bikes(self):

        print("We have currently {} bikes available to rent.".format(self.totalbikes))
        return self.totalbikes

    def hourlyRent(self, n):

        if n <= 0:
            print("Error! Number of bikes should be positive!")
            return None
        
        elif n > self.totalbikes:
            print("Sorry! We have currently {} bikes available to rent.".format(self.totalbikes))
            return None
        
        else:
            hours  = input("How many hours would you like to rent?  ")
            try:
                hours = int(hours)
            except ValueError:
                print("Error! It is not a positive integer!")
                return -1

            if hours < 1:
                print("Error! Number of hours should be greater than zero!")
                return -1
            else:
                self.totalbikes -= n
                print("You will be charged $5 for each hour per bike.")
            return hours     
     
    def dailyRent(self, n):

        if n <= 0:
            print("Error! Number of bikes should be positive!")
            return None

        elif n > self.totalbikes:
            print("Sorry! We have currently {} bikes available.".format(self.totalbikes))
            return None
    
        else:
            days  = input("How many days would you like to rent?  ")
            try:
                days = int(days)
            except ValueError:
                print("Error! It is not a positive integer!")
                return -1

            if days < 1:
                print("Error! Number of days should be greater than zero!")
                return -1
            else:
                self.totalbikes -= n
                print("You will be charged $20 for each day per bike.")
            return days




           
    def weeklyRent(self, n):

        if n <= 0:
            print("Error! Number of bikes should be positive!")
            return None

        elif n > self.totalbikes:
            print("Sorry! We have currently {} bikes available to rent.".format(self.totalbikes))
            return None        
        
        else:
            weeks  = input("How many weeks would you like to rent?  ")
            try:
                weeks = int(weeks)
            except ValueError:
                print("Error! It is not a positive integer!")
                return -1

            if weeks < 1:
                print("Error! Number of weeks should be greater than zero!")
                return -1
            else:
                self.totalbikes -= n
                print("You will be charged $60 for each week per bike.")
            return weeks
    

    
    def returnBike(self, request):

        rentalTime, option, numOfBikes = request
        bill = 0

        if rentalTime and option and numOfBikes:
            self.totalbikes += numOfBikes
        
            # hourly
            if option == 2:
                bill = rentalTime * 5 * numOfBikes
                
            # daily
            elif option == 3:
                bill = rentalTime * 20 * numOfBikes
                
            # weekly
            elif option == 4:
                bill = rentalTime * 60 * numOfBikes
            
               
            if (3 <= numOfBikes <= 5):
                print("You receive 50% discount")
                bill = bill * 0.5


            print("Your bill is: ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a bike?")
            return None



class Customer:

    def __init__(self):
        
        self.bikes = 0
        self.option = 0
        self.rentalTime = 0
        self.bill = 0

    
    def requestBike(self):
     
        bikes = input("How many bikes would you like to rent?  ")
        try:
            bikes = int(bikes)
        except ValueError:
            print("Error! That's not a positive integer!")
            return -1

        if bikes < 1:
            print("Error! Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes
     
    def returnBike(self):

        if self.option and self.rentalTime and self.bikes:
            return self.rentalTime, self.option, self.bikes  
        else:
            return 0,0,0
