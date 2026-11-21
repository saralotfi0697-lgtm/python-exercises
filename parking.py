class Owner:
    def __init__(self,owner_id,full_name,national_id,phone_number):
        self.owner_id=owner_id
        self.full_name=full_name
        self.national_id=national_id
        self.phone_number=phone_number
    def show_info(self):
        return(f'Owner_id:{self.owner_id}\nFull_name:{self.full_name}\nNational_id:{self.national_id}\nPhone_number:{self.phone_number}')
class Vehicle:
    def __init__(self,vehicle_id,plate_number,brand,model,color,vehicle_type,owner):
        self.vehicle_id=vehicle_id
        self.plate_number=plate_number
        self.brand=brand
        self.model=model
        self.color=color
        self.vehicle_type=vehicle_type
        self.owner=owner
    def show_info(self):
        return(f'Vehicle_id:{self.vehicle_id}\nPlate_number:{self.plate_number}\nBrand:{self.brand}\nModel:{self.model}\nColor:{self.color}\nVehicle_type:{self.vehicle_type}\nOwner:{self.owner.full_name}')
class Car(Vehicle):
    def __init__(self, vehicle_id, plate_number, brand, model, color, vehicle_type, owner,car_type,gearbox,fuel_type):
        super().__init__(vehicle_id, plate_number, brand, model, color, vehicle_type, owner)
        self.car_type=car_type
        self.gearbox=gearbox
        self.fuel_type=fuel_type
    def show_info(self):
        return (super().show_info() + f'\nCar_type:{self.car_type}'
                                      f'\nGearbox:{self.gearbox}'
                                      f'\nFuel_type:{self.fuel_type}')
class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, plate_number, brand, model, color, vehicle_type, owner,engine_capacity,motorcycle_type):
        super().__init__(vehicle_id, plate_number, brand, model, color, vehicle_type, owner)
        self.engine_capacity=engine_capacity
        self.motorcycle_type=motorcycle_type
    def show_info(self):
        return (super().show_info()+ f'\nEngine_capacity:{self.engine_capacity}'
                                     f'\nMotorcycle_type:{self.motorcycle_type}')
                                     
class ParkingSlot:
    def __init__(self,slot_number,vehicle_type,is_occupied=False):
        self.slot_number=slot_number
        self.vehicle_type=vehicle_type
        self.is_occupied=is_occupied
        self.parked_vehicle=None
    def park_vehicle(self,vehicle):
        if self.is_occupied==False:
            self.is_occupied=True
            self.parked_vehicle=vehicle
            print('Vehicle parked successfully!')
        else:
            print('This parking slot is already occupied!')
    def remove_vehicle(self):
        if self.is_occupied==True:
            self.is_occupied=False
            self.parked_vehicle=None
            print('Vehicle removed successfully!')
        else:
            print('This parking slot is already empty!')
    def show_info(self):
        if self.parked_vehicle is not None:
            return(f'Slot_Number:{self.slot_number}\nVehicle_Type:{self.vehicle_type}\nIs_Occupied:{self.is_occupied}\nVehicle Information:{self.parked_vehicle.show_info()}')
        else:
            return(f'Slot_Number:{self.slot_number}\nVehicle_Type:{self.vehicle_type}\nIs_Occupied:{self.is_occupied}')
class ParkingLot:
    def __init__(self):
        self.slots=[]
    def add_slot(self,slot):
        self.slots.append(slot)
    def show_slots(self):
        for i in self.slots:
            print(i.show_info())
    def empty_slot(self):
        for i in self.slots:
            if i.is_occupied==False:
                print(i.show_info())
    def parking_vehicle(self,slot_number,vehicle):
        found=False
        for i in self.slots:
            if i.slot_number==slot_number:
                found=True
                if i.vehicle_type==vehicle.vehicle_type:
                    (i.park_vehicle(vehicle))
                    break
                else:
                    print('Vehicle type does not match this parking slot!')
                    break
        if found==False:
            print('Parking slot not found!')
    def removing_vehicle(self,slot_number):
        found=False
        for i in self.slots:
            if i.slot_number==slot_number:
                (i.remove_vehicle())
                found=True
                break
        if found==False:
            print('Parking slot not found!')
    def find_vehicle(self,plate_number):
        for i in self.slots:
            if i.is_occupied==True:
                if i.parked_vehicle.plate_number==plate_number:
                        return(f' Vehicle Information:{i.parked_vehicle.show_info()}')
        return('This vehicle not found!')
    def count_vehicle(self):
        c=0
        for i in self.slots:
            if i.is_occupied==True:
                c+=1
        return c
    def count_empty_slots(self):
        c=0
        for i in self.slots:
            if i.is_occupied==False:
                c+=1
        return(f'Count_empty_slots:{c}')
    def parking_capacity(self):
        return(f'Parking_capacity:{len(self.slots)}')
    def occupancy_rate(self):
        try:
           rate=(self.count_vehicle()/len(self.slots))*100
        except(ZeroDivisionError):
             print('no slots')
        else:
            return rate
parking = ParkingLot()

parking.add_slot(ParkingSlot(1, 'Car'))
parking.add_slot(ParkingSlot(2, 'Car'))
parking.add_slot(ParkingSlot(3, 'Motorcycle'))
parking.add_slot(ParkingSlot(4, 'Car'))
print(parking.occupancy_rate())
        
