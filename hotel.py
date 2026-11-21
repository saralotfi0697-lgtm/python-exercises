class Room:
    def __init__(self,room_number,room_type,price,is_reserved):
        self.room_number=room_number
        self.room_type=room_type
        self.price=price
        self.is_reserved=is_reserved
    def show_info(self):
        return(f'Room_Number:{self.room_number}\nRoom_type:{self.room_type}\nPrice:{self.price}\nIs_Reserved:{self.is_reserved}')
    def reserve(self):
        self.is_reserved=True
    def cancel_reservation(self):
        self.is_reserved=False
class Hotel:
    def __init__(self):
        self.rooms=[]
    def add_room(self,r):
        self.rooms.append(r)
    def show_all_room(self):
        for i in self.rooms:
            print(i.show_info())
    def show_available_rooms(self):
        for i in self.rooms:
            if i.is_reserved==False:
                print(i.show_info())
    def find_room(self,r_n):
        for i in self.rooms:
            if i.room_number==r_n:
             return(i)
        return None
    def total_income(self):
        c=0
        for i in self.rooms:
            if i.is_reserved==True:
             c+=int(i.price)
        return (f'total_income:{c}')
r1=Room(101,'Single',800,False)
r2=Room(102,'Double',1200,True)
r3=Room(103,'VIP',2500,False)
r4=Room(104,'Single',800,True)
r5=Room(105,'Double',1200,False)
r6=Room(106,'VIP',3000,True)       
r7=Room(107,'Single',900,False)
r8=Room(108,'Double',1500,False)
h=Hotel()
h.add_room(r1)
h.add_room(r2)
h.add_room(r3)
h.add_room(r4)
h.add_room(r5)
h.add_room(r6)
h.add_room(r7)
h.add_room(r8)
c1='1. Add Room — اضافه کردن اتاق'
c2='2. Show All Rooms — نمایش تمام اتاق‌ها'
c3='3. Show Available Rooms — نمایش اتاق‌های آزاد'
c4='4. Find Room — جست‌وجوی اتاق با شماره'
c5='5. Reserve Room — رزرو اتاق'
c6='6. Cancel Reservation — لغو رزرو'
c7='7. Total Income — محاسبه درآمد هتل'
c8='8. Exit — خروج از برنامه'
while True:
    n=input(f'please choose one:\n{c1}\n{c2}\n{c3}\n{c4}\n{c5}\n{c6}\n{c7}\n{c8}')
    if n=='1':
        a=int(input('enter number of room:(108>)'))
        b=input('enter type of room:(Single/Double/VIP)')
        c=int(input('enter price of room:'))
        d=(input('enter reservation of room(False/True):')).lower()=='true'
        r=Room(a,b,c,d)
        h.add_room(r)
        print('added!')
    elif n=='2':
        h.show_all_room()
    elif n=='3':
        h.show_available_rooms()
    elif n=='4':
        sh=int(input('enter number of room:'))
        room=(h.find_room(sh))
        if room is None:
            print('room not found.')
        else:
            print(room.show_info())
    elif n=='5':
        sh=int(input('enter number of room:'))
        room=(h.find_room(sh))
        if room is None:
            print('room not found.')
        elif room.is_reserved==False:
          print(room.show_info())
          y=input('are you ok?(yes/no)')
          if y=='yes':
            room.reserve()
            print('reserved!')
          else:
            print('ok,nice to see u!!') 
        else:
            print('room if por')
    elif n=='6':
        sh=int(input('enter number of room:'))
        room=(h.find_room(sh))
        if room is None:
            print('room not found')
        elif room.is_reserved==True:
            room.cancel_reservation()
            print('canceld')
        else:
            print('this room is not reserved.')
    elif n=='7':
        print(h.total_income())
    elif n=='8':
        print('have a good day!')
        break
    else:
        print('error!')