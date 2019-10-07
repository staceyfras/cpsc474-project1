#Reads file and cleans input to make other parts simpler
def fileReader(filename):
    testinput = list()
    with open(filename) as f:
        testinput = f.read().splitlines()

    for i in range(0, len(testinput)):
        testinput[i] = testinput[i].split()
    for i in range(0, len(testinput)):
        for j in range(0, len(testinput[i])):
            if len(testinput[i][j]) == 1:
                testinput[i][j] = 'i'
    return testinput

#class for each queue of events and their clocks
class process:
    send_clock = 0
    clock = 0
    input = list()

    def __init__(self, listInput):
        self.input = listInput
        self.output = list()

    def internal(self):
        self.clock += 1
        self.output.append(self.clock)
        self.input.pop(0)
        self.input.append(None)
    def send(self):
        self.clock +=1
        self.send_clock = self.clock
        self.output.append(self.clock)
        self.input.pop(0)
        self.input.append(None)
    def receive(self,k):
        self.clock= max(self.clock,k)+1
        self.output.append(self.clock)
        self.input.pop(0)
        self.input.append(None)
    def null(self):
        self.output.append(0)
        self.input.pop(0)
        self.input.append(None)
    def result(self):
       print(self.output)

#main
send = [0,0,0,0]
userInput = input("Enter file name for test case:  ")
testinput = fileReader(userInput)


p1 = process(testinput[0])
p2 = process(testinput[1])
p3 = process(testinput[2])
while p1.input[0] != None or p2.input[0] != None or p3.input[0] != None:
    #internal section
    if p1.input[0] == 'i' :
        p1.internal()
    if p2.input[0] == 'i' :
        p2.internal()
    if p3.input[0] == 'i' :
        p3.internal()
    #send section
    #p1 send
    if p1.input[0] == 's1':
        p1.send()
        send[0] = p1.send_clock
    elif p1.input[0] == 's2':
        p1.send()
        send[1] = p1.send_clock
    elif p1.input[0] == 's3':
        p1.send()
        send[2] = p1.send_clock
    #p2 send
    if p2.input[0] == 's1':
        p2.send()
        send[0] = p2.send_clock
    elif p2.input[0] == 's2':
        p2.send()
        send[1] = p2.send_clock
    elif p2.input[0] == 's3':
        p2.send()
        send[2] = p2.send_clock
    #p3 send
    if p3.input[0] == 's1':
        p3.send()
        send[0] = p3.send_clock
    elif p3.input[0] == 's2':
        p3.send()
        send[1] = p3.send_clock
    elif p3.input[0] == 's3':
        p3.send()
        send[2] = p3.send_clock
    #recieve section
    #p1 receive
    if p1.input[0] == 'r1' or p1.input[0] == 'r2' or p1.input[0] == 'r3':
        if p1.input[0] == 'r1' and send[0]!= 0:
            p1.receive(send[0])
        elif p1.input[0] == 'r2' and send[1]!= 0:
            p1.receive(send[1])
        elif p1.input[0] == 'r3' and send[2]!= 0:
            p1.receive(send[2])
        #else: break
    #p2 receive
    if p2.input[0] == 'r1' or p2.input[0] == 'r2' or p2.input[0] == 'r3':
        if p2.input[0] == 'r1' and send[0]!= 0:
            p2.receive(send[0])
        elif p2.input[0] == 'r2' and send[1]!= 0:
            p2.receive(send[1])
        elif p2.input[0] == 'r3' and send[2]!= 0:
            p2.receive(send[2])
        #else: break
    #p3
    if p3.input[0] == 'r1' or p3.input[0] == 'r2' or p3.input[0] == 'r3':
        if p3.input[0] == 'r1' and send[0]!= 0:
            p3.receive(send[0])
        elif p3.input[0] == 'r2' and send[1]!= 0:
            p3.receive(send[1])
        elif p3.input[0] == 'r3' and send[2]!= 0:
            p3.receive(send[2])
        #else: break
    #NULL section
    if p1.input[0] == 'NULL':
        p1.null()
    if p2.input[0] == 'NULL':
        p2.null()
    if p3.input[0] == 'NULL':
        p3.null()


p1.result()
p2.result()
p3.result()
