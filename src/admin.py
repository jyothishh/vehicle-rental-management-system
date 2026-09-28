vehicles={}

class AdminPanel:

    def __init__(self,vehicles):
        self.vehicles=vehicles

    def add_vehicle(self,vid,vtype,vmodel,vrent):
        self.vehicles[vid]={

            "vehicleid": vid,
            "vehicletype": vtype,
            "vehiclemodel": vmodel,
            "vehiclerent" : vrent,
            "vehiclestatus": "Available"
        }
        print(f"Vehicle added successfully.{vid}:{vtype}")


    def view_inventory(self):
        for vehicle,data in self.vehicles.items():
            print(f"{vehicle}:Type: {data["vehicletype"]}, Brand: {data["vehiclemodel"]}, Rent: {data["vehiclerent"]}")


if __name__ == "__main__":
    vehicles={}
    admin=AdminPanel(vehicles)
    admin.add_vehicle("KA01HW9089","Bike","Scooty",800)
    admin.add_vehicle("KA02HE9090","Car","Thar",2800)
    admin.view_inventory()
