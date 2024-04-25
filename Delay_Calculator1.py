

L = int(input("Insert Average Size of Packet (Bits): "))
while(L<=0):
    L = int(input("Insert Average Size of Packet (Bits) - Insert Valid Input [Size of Packet>0 bits]): "))

D_max = float(input("Insert Maximum Delay between Nodes (Seconds): "))
while(D_max<=0):
    D_max = float(input("Insert Maximum Delay between Nodes (Seconds - Insert Valid Input [Maximum Delay between Nodes>0]): "))

Prop = float(input("Insert Propagation Delay (Seconds): "))
while(Prop<=0):
    Prop = float(input("Insert Propagation Delay (Seconds - Insert Valid Input [Propagation>0]): "))

TransmissiondDealy = D_max - Prop

R= int(abs(L / TransmissiondDealy))

print("Bit Rate R should be at least " + str(R) + " bits per second, in order for the Delay between the Nodes to be " + str(D_max) + " seconds or less.\n")

print("Bits in Time Frame: \n")

One_Bit_Transmission_Delay = 1/R

First_Bit_Delivery_Time = One_Bit_Transmission_Delay + Prop

t1 = float(input("Insert Beginning of Time Frame (Seconds): "))
while(t1<0 or t1>D_max):
    t1 = float(input("Insert Beginning of Time Frame (Seconds - Insert Valid Input [Beginning of Time Frame>=0 and Beginning of Time Frame<=Delay between Nodes]): "))

t2 = float(input("Insert End of Time Frame (Seconds): "))
while(t1>t2 or t2>D_max):
    t1 = float(input("Insert End of Time Frame (Seconds - Insert Valid Input [End of Time Frame>=Beginning of Time Frame and End of Time Frame<=Delay between Nodes]): "))

t11=t1
t22=t2

BitNumber=0
flag=False
if(t1>0 and t1<=First_Bit_Delivery_Time):
    t1=First_Bit_Delivery_Time
    if(t2>=First_Bit_Delivery_Time):
        BitNumber += 1
else:
    if(t1!=0):
        m1 = t1//One_Bit_Transmission_Delay
        t1= m1*One_Bit_Transmission_Delay

if(t2>0 and t2<First_Bit_Delivery_Time):
    t2=0
else:
    if(t2!=0):
        m2 = t2//One_Bit_Transmission_Delay
        t2= m2*One_Bit_Transmission_Delay



newt1=t1

if(t2-t1<0):
    BitNumber=0
elif(t2-t1==0):
    BitNumber = 1
else:
    if(t1==0):
        BitNumber+=1
        newt1= First_Bit_Delivery_Time

BitNumber = int(BitNumber + ((t2-newt1)*R))

print("Number of Bits Delivered in Time Frame ["+ str(t11) + ", "+ str(t22) +"]: " + str(BitNumber))

end= input("Press any key to end sequence.")
