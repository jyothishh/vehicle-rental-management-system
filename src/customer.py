from .admin import AdminPanel

vehicles={}
customer={}
class CustomerPanel:
    

    def __init__(self,customer,vehicles):
        self.customer=customer
        self.vehicles=vehicles
        self.admin=AdminPanel(vehicles)
    def register_customer(self,cid,cname,cphone):
        self.customer[cid]={
            "customer id":cid,
            "customer name":cname,
            "customer phone no":cphone,
            "Rented Vehicle":"None"
        }
        print(f"Customer registered successfully,{cname},{cphone}")
        

    def view_vehicle(self):
        print("Cars available ")
        self.admin.view_inventory()
        for vid,data in self.vehicles.items():
             if data["vehiclestatus"]=="Available":
                status="Available"
             else:
                status="Rented" 


    def rent_vehicle(self,cid,vid):
        if cid not in self.customer:
            print("Customer does not exist!")
            return

        if vid not in self.vehicles:
            print("Vehicle ID not found!")
            return

        if self.vehicles[vid]["vehiclestatus"]!="Available":
            print(" Vehicle already rented!")
            return

        self.vehicles[vid]["vehiclestatus"]="Rented"
        self.customer[cid]["Rented vehicle"]=vid
        print(f"{self.customer[cid]["customer name"]} rented {self.vehicles[vid]["vehiclemodel"]} ({self.vehicles[vid]["vehicletype"]})")

    def return_vehicle(self,cid):
        if cid not in self.customer:
            print("Customer does not exist!")
            return
        rented=self.customer["Rented Vehicle"]=None
        if not rented:
            print("No vehicle rented by this customer.")
        self.vehicles["Rented"]["vehiclestatus"]="Available"
        print(f"{self.customers[cid]['name']} returned {self.vehicles[rented]['vehiclemodel']} ({self.vehicles[rented]['vehicletype']})")
        self.customer[cid]["Rented vehicle"]=None

if __name__ == "__main__":
    customer=CustomerPanel(customer,vehicles)
    customer.register_customer("Jyothish",3656200001)
    customer.view_vehicle()
