
class Customer:
    def __init__(self, lname, CustomerID, PhoneNumber):
        self.lname = lname
        self.CustomerID = CustomerID
        self.PhoneNumber = PhoneNumber

    def display(self):
        print("The customer's last name is: " & self.lname)
        print("The customer's ID is: " & self.CustomerID)
        print("The customer's Phone Number is: " & self.PhoneNumber)



class Rental:
    def __init__(self, RentID, CustomerID, SkisRent, SnowboardsRent, RentLength):
        self.RentID = RentID
        self.CustomerID = CustomerID
        self.SkisRent = SkisRent
        self.SnowboardsRent = SnowboardsRent
        self.RentLength = RentLength
    
    def display(self):
        print("The rental ID is: " & self.RentID)
        print("The customer ID is: " & self.CustomerID)
        print("The # of Skis Rented is: " & self.SkisRent)
        print("The # of Snowboards Rented is: " & self.SnowboardsRent)
        print("The # of Hours Rented for is: " & self.RentLength)



class Shop:
    def __init__(self, InventorySkis, InventorySnowboards, CustomerList, RentalList, TotalIncome):
        self.InventorySkis = InventorySkis
        self.InventorySnowboards = InventorySnowboards
        self.CustomerList = CustomerList
        self.RentalList = RentalList
        self.TotalIncome = TotalIncome

    def setupinventory(self, setSkis, setSnowboards):
        self.InventorySkis = setSkis
        self.InventorySnowboards = setSnowboards

    def addcustomer(self):
        #makes a new customer object

    def addrental(self):
        #makes a new rental object
    def findcustomer(self, CustomerIDtoFind):
        for Customer in CustomerList:
            if Customer.CustomerID == CustomerIDtoFind:
                return Customer
        return None

    def findrental(self, RentalIDtoFind):
        for Rental in RentalList:
            if Rental.RentID == RentalIDtoFind:
                return Rental
        return None

    def completerental(self):
        #completes current rental

    def findcustomerrental(self):
        #finds the customer's rental