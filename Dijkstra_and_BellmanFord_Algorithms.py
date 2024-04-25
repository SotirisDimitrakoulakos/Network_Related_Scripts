class Edge():
    def __init__(self, s, f, c):
        self.cost = c
        self.s = Node(s)
        self.f = Node(f)

class Node():
    def __init__(self,name):
        self.Name=name
        self.Edges=[]
    def appendEdge(self, edge):
        self.Edges.append(edge)

Edges = []
Nodes = {}
file1 = input("File Name with Network Status: ")
f = open(file1, "r").read().splitlines()
for l in f:
    l = l.strip().split()
    nodeA = l[0]
    nodeB = l[1]
    cost = int(l[2])
    inedge = Edge(nodeA, nodeB, cost)
    Edges.append(inedge)
if inedge.s.name not in list(Nodes.keys()):
    Nodes[inedge.s.name] = [inedge]
else:
    Nodes[inedge.s.name].append(inedge)
if inedge.f.name not in list(Nodes.keys()):
    Nodes[inedge.f.name] = [inedge]
else:
    Nodes[inedge.f.name].append(inedge)
startpoint = input("Κόμβος <<Αφετηρία>>: ")
while startpoint not in list(Nodes.keys()):
    startNode = input("Node doesn't exist!\nΚόμβος αφετηρίας: ")
alg=input("Select Algorithm: \n (1 for Link-state (Dijkstra) / 2 for  Distance Vector (Bellman-Ford) / 3 for Both Algorithms): ")
while ((alg!="1") and (alg!="2") and (alg!="3")):
    print("Enter Valid Input: ")
    alg = input("Select Algorithm: \n (1 for Link-state (Dijkstra) / 2 for  Distance Vector (Bellman-Ford) / 3 for Both Algorithms): ")
if ((alg == "1") or (alg == "3")):
    FullStepTable = []
    HopTable = []
    VisitedNodes = []
    CostHelpTable = []
    CostHelpTable.append([])
    CostHelpTable.append([])
    for n in Nodes:
        CostHelpTable[0].append(n)
        if n==startpoint:
            CostHelpTable[1].append(0)
        else:
            CostHelpTable[1].append(float("inf"))
    CostHelpTable[0].sort()
    helpl = ["h"]
    helpl.append(range(0, len(Nodes)+1))
    FullStepTable.append(helpl)
    FullStepTable.append(CostHelpTable[0].copy())
    FullStepTable[0].append("P")
    FullStepTable.append(CostHelpTable[1].copy())
    HopTable.append(CostHelpTable[0].copy())
    HopTable.append(CostHelpTable[1].copy())
    curr1= startpoint
    while True:
        pos1=CostHelpTable[0].index(curr1)
        for edge in Nodes[curr1]:
            if (edge.s.name != curr1):
                fin1 = edge.s.name
            else:
                fin1 = edge.f.name
            if fin1 not in VisitedNodes:
                pos2=CostHelpTable[0].index(fin1)
                if CostHelpTable[-1][pos2] > edge.cost+CostHelpTable[-1][pos1]:
                    CostHelpTable[-1][pos2] = edge.cost+CostHelpTable[-1][pos1]
                    HopTable[-1][pos2]=CostHelpTable[0][pos1]
        VisitedNodes.append(curr1)
        FullStepTable.append(CostHelpTable[1].copy())
        FullStepTable[-1].append([curr1] if curr1 == startpoint else FullStepTable[-2][-1]+[curr1])
        pos2=-1
    print("\nTable with All Steps: ", FullStepTable[0][-1])
    for i in FullStepTable:
        print('\t'.join([str(j) for j in i[:-1]]), "\t" + ','.join(i[-1]) if type(i[-1]) == list else "\t%s" % i[-1])
    HopTable2 = []
    print("\nPaths: ")
    for i in range(len(Nodes)):
        r1=[CostHelpTable[0][i]]
        while r1[-1] != startpoint:
            r1.append(HopTable[1][HopTable[0].index(r1[-1])])
        print("%s->%s: %s" % (startpoint, CostHelpTable[0][i], ','.join(r1)))
        HopTable2.append(r1[-2] if len(r1)>1 else r1[0])
    print("\nRouting table: ")
    print("Destination Node\tNext-Hop\tCost")
    for i in range(len(CostHelpTable[0])):
        print("%s\t\t\t%s\t\t%s"%(CostHelpTable[0][i], HopTable2[i], CostHelpTable[-1][i]))
if ((alg=="2") or (alg=="3")):
    FullStepTable2 = []
    HopTable3 = []
    CostHelpTable2 = []
    CostHelpTable2.append([])
    CostHelpTable2.append([])
    for n in Nodes:
        CostHelpTable2[0].append(n)
        CostHelpTable2[1].append(float("inf"))
    CostHelpTable2[0].sort()
    CostHelpTable2[1][CostHelpTable2[0].index(startpoint)] = 0
    helpl2 = ["h"]
    helpl2.append(range(0, len(Nodes) + 1))
    FullStepTable2.append(helpl2)
    FullStepTable2.append(CostHelpTable2[0].copy())
    FullStepTable2.append(CostHelpTable2[1].copy())
    HopTable3.append(CostHelpTable2[0].copy())
    HopTable3.append(CostHelpTable2[1].copy())
    count=0
    flag=True
    while flag:
        count=count+1
        flag=False
        for n1 in Nodes:
            curr2=n1
            pos3 = CostHelpTable2[0].index(curr2)
            for edge in Nodes[curr2]:
                if (edge.s.name != curr2):
                    fin2 = edge.s.name
                else:
                    fin2=edge.f.name
                pos4 = CostHelpTable2[0].index(fin2)
                if CostHelpTable2[-1][pos4] > edge.cost + CostHelpTable2[-1][pos3]:
                    flag = True
                    CostHelpTable2[-1][pos4] = edge.cost + CostHelpTable2[-1][pos4]
                    HopTable3[-1][pos4] = CostHelpTable2[0][pos3]
            if (CostHelpTable2[-1] != FullStepTable2[-1]):
                FullStepTable2.append(CostHelpTable2[-1].copy())
    print("\nTable with All Steps: ", FullStepTable2[0][-1])
    for i in FullStepTable:
        print('\t'.join([str(j) for j in i[:-1]]), "\t" + ','.join(i[-1]) if type(i[-1]) == list else "\t%s" % i[-1])
    HopTable4 = []
    print("\nPaths: ")
    for i in range(len(Nodes)):
        r2 = [CostHelpTable2[0][i]]
        while r2[-1] != startpoint:
            r1.append(HopTable3[1][HopTable3[0].index(r2[-1])])
        print("%s->%s: %s" % (startpoint, CostHelpTable2[0][i], ','.join(r2)))
        HopTable4.append(r2[-2] if len(r2) > 1 else r2[0])
    print("\nRouting table: ")
    print("Destination Node\tNext-Hop\tCost")
    for i in range(len(CostHelpTable2[0])):
        print("%s\t\t\t%s\t\t%s" % (CostHelpTable2[0][i], HopTable4[i], CostHelpTable2[-1][i]))

    stay = input("Press Enter to end the Sequence.")
