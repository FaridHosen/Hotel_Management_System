class hotelfarecal:
    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=105):
        print("\n\n***Welcome to Hotel Radison***\n")
        self.rt = rt
        self.r = r
        self.t = t
        self.p = p
        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno
    
    def inputdata(self):
        self.name = input("\n Enter your name:")
        self.address = input("\n Enter your address:")
        self.cindate = input("\n Enter your check in data:")
        self.coutdate = input("\n Enter your check out date:")
        print("Your room no:",self.rno,"\n")

    def roomrent(self):
        print("We have the following rooms for you:")
        print("1. type A---->Tk 5000 pn\-")
        print("2. type B---->Tk 4000 pn\-")
        print("3. type B---->Tk 3000 pn\-")
        print("4. type B---->Tk 2000 pn\-")
        x = int(input("Enter your choice please->"))
        n = int(input("For How many nights did you stay:"))

        if(X==1):
            print ("you have opted room type A")
            self.s = 5000*n
        
        elif (x==2):
            print("you have opted room type B")
            self.s=4000*n
        
        elif (x==3):
            print("you have opted room type C")
            self.s=3000*n
        
        elif (x==4):
            print("you have opted room type D")
            self.s=2000*n
        else:
            print("please choose a room")
        print ("your room rent is =",self.s,"\n")
    
    def restaurentbill(self):
        print("***Restaurant Menu****")
        print("1.water---->Tk 15","2.tea---->Tk 5","3.breakfast---->Tk 100","4.lunch---->Tk 115","5.dinner---->Tk 130","6.Exit")

        while (1):
            c= int(input("Enter your choice:"))

            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r = self.r+15*d


            elif (c==2):
                d=int(input("Enter the quantity:"))
                self.r= self.r+5*d
            elif (c==3):
                d=int(input("Enter the quantity:"))
                self.r= self.r+100*d
            elif (c==4):
                d=int(input("Enter the quantity:"))
                self.r= self.r+115*d
            elif (c==5):
                d=int(input("Enter the quantity:"))
                self.r= self.r+130*d
            elif (c==6):
                break
            else:
                print("Invalid option")
        print("total food cost=Tk",self.r,"\n")

    def laundrybill(self):
        print("*** Laundry menu ***")
        print("1.shorts---->Tk5","2.Trousers---->Tk8","3.Shirt---->Tk10","4.jeans---->Tk12","5.Girlsuit--->Tk15","6.Exit")

        while(1):
            e= int(input("Enter your choice:"))
            if (e==1):
                f= int(input("Enter the quantity:"))
                self.t=self.t+5*f
            elif(e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+8*f
            elif(e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+10*f
            elif(e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+12*f
            elif(e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+15*f
            elif(e==6):
                break;
            else:
                print("Invalid option")
        
        print("Total Laundry Cost=Rs",self.t,"\n")

    def gamebill(self):
        print("***Game Menu***")
        print("1.Table tennis ---->Tk 50","2.Bowling---->Tk60","3.Snooker---->Tk70","4.video game--->80","5.pool--->90","6.Exit")

        while(1):
            g=int(input("Enter your choice:"))

            if (g==1):
                h=int(input("no. of hours:"))
                self.p=self.p+50*h
            if (g==2):
                h=int(input("no. of hours:"))
                self.p=self.p+60*h

            if(g==3):
                h=int(input("no.of hours:"))
                self.p=self.p=70*h
            if(g==4):
                h=int(input("no. of hours:"))
                self.p=self.p+80*h
            if(g==5):
                h= int(input("no. of hours:"))
                self.p=self.p+90*h
            elif(g==6):
                break;
            else:
                print("Invalid option")
        print("Total Game Bill=Tk",self.p,"\n")


    def display(self):
        print("***Hotel Bill***")
        print("Customer details:")
        print("Customer Name:",self.name)
        print("Customer Address:",self.address)
        print("Check in date:",self.cindate)
        print("Check out date:",self.coutdate)
        print("Room NO.",self.rno)
        print("your room rant is:",self.s)
        print("your food bill is:",self.r)
        print("your laundary bill is:",self.t)
        print("your game bill is:",self.p)

        self.rt = self.s+self.t+self.p+self.r

        print("your sub total bill is:",self.rt)
        print("Additional service Charges is:",self.a)
        print("your grandtotal bill is:",self.rt+self.a,"\n")
        self.rno+=1

def main():
    a = hotelfarecal()

    while(1):
        print("1.Enter Customer Data")
        print("2.Calculate Rommrent")
        print("3.Calculate Restaurant bill")
        print("4.Calculate Laundry bill")
        print("5.Calculate gamebill")
        print("6.show total cost")
        print("7.Exit")

        b=int(input("/n Enter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):
            a.roomrent()

        if (b==3):
            a.restaurentbill()
        
        if (b==4):
            a.laundrybill()

        if (b==5):
            a.gamebill()

        if (b==6):
            a.display()

        if (b==7):
            quit()


main()
        











































