#edit2

from bike import RentBike, Customer

def main():
    shop = RentBike(200)
    customer = Customer()

    while True:
        print("""
        1. Show available bikes
        2. Hourly rent: $5
        3. Daily  rent: $20
        4. Weekly rent: $60
        5. Return a bike
        6. Exit
        """)
        
        choice = input("Enter choice:  ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It is not an int!")
            continue
        
        if choice == 1:
            shop.show_bikes()
        
        elif choice == 2:
            customer.rentalTime = shop.hourlyRent(customer.requestBike())
            customer.option = 2

        elif choice == 3:
            customer.rentalTime = shop.dailyRent(customer.requestBike())
            customer.option = 3

        elif choice == 4:
            customer.rentalTime = shop.weeklyRent(customer.requestBike())
            customer.option = 4

        elif choice == 5:
            customer.bill = shop.returnBike(customer.returnBike())
            customer.option, customer.rentalTime, customer.bikes = 0,0,0        
        elif choice == 6:
            break
        else:
            print("Error. Please enter number between 1-6 ")        


if __name__=="__main__":
    main()