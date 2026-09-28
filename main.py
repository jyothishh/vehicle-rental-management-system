from src.admin import AdminPanel
from src.customer import CustomerPanel

def main_display():
    print("###############################")
    print("Welcome to Jyothish Rentals")
    print("###############################")
    print("Choose an option : ")
    print("1.Admin Panel")
    print("2.Customer Panel")
    print("3.Exit")

def admin_display():
    print("###############################")
    print("Welcome to Admin panel")
    print("###############################")
    print("Choose an option : ")
    print("1.Add Vehicle")
    print("2.View Inventory")
    print("3.Exit Admin panel")

def customer_display():
    print("###############################")
    print("Welcome to the customer panel")
    print("###############################")
    print("Please choose an option :")
    print("1.Register Customer")
    print("2.View Available Vehicle")
    print("3.Rent a vehicle")
    print("4.Return a vehicle")
    print("5.Exit the customer panel")

def main():
    vehicles={}
    customer={}
    customer=CustomerPanel(customer,vehicles)
    admin=AdminPanel(vehicles)
    while True:
        main_display()
        user_choice=input("Enter your choice 1/2/3 : ")
        if user_choice =="1":
            while True:
                admin_display()
                admin_choice=input("Enter your choice 1/2/3 : ")
                if admin_choice == "1":
                    vid=input("Enter the vehicle ID: ")
                    vtype=input("Enter the Vehicle Type : ")
                    vmodel=input("Enter the Vehicle model : ")
                    vrent=input("Enter the Vehicle Rent : ")
                    admin.add_vehicle(vid,vtype,vmodel,vrent)
                elif admin_choice == "2":
                    print("Displaying all vehicles")
                    admin.view_inventory()
                elif admin_choice == "3":
                    print("Exiting Admin panel")
                    break
                else:
                    print("Invalid input")

        elif user_choice == "2":
            while True:
                customer_display()
                customer_choice=input("Enter your choice 1/2/3 : ")
                if customer_choice == "1":
                    cname=input("Enter customer name : ")
                    cid=input("Enter customer id : ")
                    cphone=input("Enter customer Phone number : ")
                    customer.register_customer(cid,cname,cphone)
                elif customer_choice == "2":
                    customer.view_vehicle()
                elif customer_choice == "3":
                    cid=input("Enter the customer id : ")
                    vid=input("Enter the vehicle id : ")
                    customer.rent_vehicle(cid,vid)
                elif customer_choice == "4":
                    print("Return a vehicle")
                elif customer_choice == "5":
                    print("Exiting the customer panel")
                    break
       
        elif user_choice == "3":
            print("Thankyou for using Jyothish Rentals")
            break
        else :
            print("Invalid Input")



if __name__ == "__main__":
    main()