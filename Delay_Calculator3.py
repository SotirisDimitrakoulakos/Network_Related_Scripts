class CalculateTotalDelay():

    def __init__(self):
        self.P = 0.0
        self.newP = 0
        self.C = 0.0
        self.newC = 0.0
        self.Prop = 0.0
        self.Prop2 = 0.0
        self.D_total = 0.0
        self.BEP = 0.0
        self.timeout = 0.0
        self.max_wrong_bits = 0

    def insertion(self):
        self.P = float(input("Insert Average Size of Packet (Kbytes): "))
        while (self.P <= 0):
            self.P = float(input("Insert Average Size of Packet (Kbytes) - Insert Valid Input [Size of Packet>0 bits]): "))
        self.newP = int(round(self.P * 8 * 1000))

        self.C = float(input("Insert Bit Rate between Nodes (Kbps): "))
        while (self.C <= 0):
            self.C = float(input("Insert Bit Rate between Nodes (Kbps - Insert Valid Input [Bit Rate between Nodes>0]): "))
        self.newC = self.C * 1000

        self.Prop = float(input("Insert Propagation Delay (msec): "))
        while (self.Prop <= 0):
            self.Prop = float(input("Insert Propagation Delay (msec - Insert Valid Input [Propagation>0]): "))
        self.Prop2 = self.Prop / 1000

        self.BEP = float(input("Insert Bit Error Probability (float from 0 to 1): "))
        while ((self.BEP < 0) or (self.BEP > 1)):
            self.BEP = float(input("Insert Bit Error Probability (float from 0 to 1 - Insert Valid Input): "))

        self.max_wrong_bits = int(input("Insert Max Wrong Bits (integer 0 or 1 or 2): "))
        while ((self.max_wrong_bits != 0) and (self.max_wrong_bits != 1) and (self.max_wrong_bits != 2)):
            self.max_wrong_bits= int(input("Insert Max Wrong Bits (integer 0 or 1or 2 - Insert Valid Input): "))

    def calculation(self):

        if self.max_wrong_bits != 0 :
            self.timeout = 1 - float(1 - self.BEP) ** (self.P / self.max_wrong_bits)
        else:
            self.timeout=1

        p_s= (1- self.BEP) ** (self.P - self.max_wrong_bits)

        D_S = float(float(self.newP / self.newC) + self.Prop2)
        D_E = float(self.timeout * ((1-p_s) / p_s ))

        self.D_total = float(D_S + D_E)

    def show(self):
        print(f"\nAppropriate TIMEOUT value: {self.timeout} seconds. \nDelay between nodes: {self.D_total} seconds.")

        end = input("\nPress any key to end sequence.")


def main():
    NetD1 = CalculateTotalDelay()
    NetD1.insertion()
    NetD1.calculation()
    NetD1.show()

main()
