
try:
    L = int(input("Packet Size (bits): "))
except ValueError:
    print("Invalid Input!")
    L=-10
while(L<=0):
    try:
        L = int(input("Packet Size (bits - Enter Valid Input [>0]): "))
    except ValueError:
        print("Invalid Input!")
        L = -10

try:
    NodesNumber = int(input("Number of Nodes between T1 and T2: "))
except ValueError:
    print("Invalid Input!")
    NodesNumber = -10
while(NodesNumber<0):
    try:
        NodesNumber = int(input("Number of Nodes between T1 and T2 (Enter Valid Input [>=0]): "))
    except ValueError:
        print("Invalid Input!")
        NodesNumber = -10

try:
    R = int(input("Bit Rate for each link (bits per second): "))
except ValueError:
    print("Invalid Input!")
    R = -10
while(R<=0):
    try:
        R = int(input("Bit Rate for each link (bits per second - Enter Valid Input [>0]): "))
    except ValueError:
        print("Invalid Input!")
        R = -10

try:
    F = int(input("Fragment Size (bits / Fragment Size=0 means no fragmentation): "))
except ValueError:
    print("Invalid Input!")
    F = -10
while(F<0 or F>L/2):
    try:
        F = int(input("Fragment Size (bits - Enter Valid Input [>=0 AND <=PacketSize/2] / Fragment Size=0 means no fragmentation): "))
    except ValueError:
        print("Invalid Input!")
        F = -10

try:
    h = int(input("Headers Size (bits / Headers Size=0 means no headers): "))
except ValueError:
    print("Invalid Input!")
    h = -10
while(h<0 or h > F):
    try:
        h = int(input("Headers Size (bits - Enter Valid Input [>=0 AND <Fragment Size] / Headers Size=0 means no headers): "))
    except ValueError:
        print("Invalid Input!")
        h = -10

N = NodesNumber+2 #All Nodes with T1 and T2
TotalDelay=0

if (F!=0):
    if(h==0):
        TotalDelay = (L/R) + (N-2)*(F/R)
        print("Total Delay with Fragmentation and without Headers: ", TotalDelay, " seconds.")
    else:
        TotalDelay = ((L/F)*(F+h)/R) + (N-2)*((F+h)/R)
        print("Total Delay with Fragmentation and with Headers: ", TotalDelay, " seconds.")
else:
    TotalDelay = (N-1)*(L/R)
    print("Total Delay without Fragmentation: ", TotalDelay, " seconds.")

End = input("Press Enter to end the sequence.")