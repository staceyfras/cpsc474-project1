# Reads file and cleans input to make other parts simpler
def fileReader(filename):
    testinput = list()
    with open(filename) as f:
        testinput = f.read().splitlines()
    # fill lists with events
    for i in range(0, len(testinput)):
        testinput[i] = testinput[i].split()
    for i in range(0, len(testinput)):
        for j in range(0, len(testinput[i])):
            if len(testinput[i][j]) == 1:
                testinput[i][j] = 'i'
    # sets max length of row
    maxlen = len(testinput[0])
    for i in range(0, len(testinput)):
        if len(testinput[i])>maxlen:
            maxlen = len(testinput[i])
    # fills empty spots with null
    for i in range(0, len(testinput)):
        if len(testinput[i]) != maxlen:
            testinput[i].append("NULL")

    return testinput

#class for each queue of events and their clocks
class process:
    send_clock = 0
    clock = 0
    input = list()

    def __init__(self, listInput):
        if listInput == 'z':
            self.input.append(None)
            self.output = list()
            self.output.append(None)
        else:
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
        if self.output[0] != None:
            print(self.output)


#main

userInput = input("Enter file path for test case:  ")
testinput = fileReader(userInput)
send = [0]*9
num = len(testinput)
if num == 1:
    p1 = process(testinput[0])
    p2 = process("z") # the z is just a placeholder to make an empty process
    p3 = process("z")
    p4 = process("z")
    p5 = process("z")
elif num == 2:
    p1 = process(testinput[0])
    p2 = process(testinput[1])
    p3 = process("z")
    p4 = process("z")
    p5 = process("z")
elif num == 3:
    p1 = process(testinput[0])
    p2 = process(testinput[1])
    p3 = process(testinput[2])
    p4 = process("z")
    p5 = process("z")
elif num == 4:
    p1 = process(testinput[0])
    p2 = process(testinput[1])
    p3 = process(testinput[2])
    p4 = process(testinput[3])
    p5 = process("z")
elif num == 5:
    p1 = process(testinput[0])
    p2 = process(testinput[1])
    p3 = process(testinput[2])
    p4 = process(testinput[3])
    p5 = process(testinput[4])


while p1.input[0] != None or  p2.input[0] != None or p3.input[0] != None or  p4.input[0] != None or p5.input[0] != None:
    # internal section
    if p1.input[0] == 'i' :
        p1.internal()
    if p2.input[0] == 'i' :
        p2.internal()
    if p3.input[0] == 'i' :
        p3.internal()
    if p4.input[0] == 'i' :
        p4.internal()
    if p5.input[0] == 'i' :
        p5.internal()
    # send section
    # p1 send
    if p1.input[0] == 's1':
        p1.send()
        send[0] = p1.send_clock
    elif p1.input[0] == 's2':
        p1.send()
        send[1] = p1.send_clock
    elif p1.input[0] == 's3':
        p1.send()
        send[2] = p1.send_clock
    elif p1.input[0] == 's4':
        p1.send()
        send[3] = p1.send_clock
    elif p1.input[0] == 's5':
        p1.send()
        send[4] = p1.send_clock
    elif p1.input[0] == 's6':
        p1.send()
        send[5] = p1.send_clock
    elif p1.input[0] == 's7':
        p1.send()
        send[6] = p1.send_clock
    elif p1.input[0] == 's8':
        p1.send()
        send[7] = p1.send_clock
    elif p1.input[0] == 's9':
        p1.send()
        send[8] = p1.send_clock
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
    elif p2.input[0] == 's4':
        p2.send()
        send[3] = p2.send_clock
    elif p2.input[0] == 's5':
        p2.send()
        send[4] = p2.send_clock
    elif p2.input[0] == 's6':
        p2.send()
        send[5] = p2.send_clock
    elif p2.input[0] == 's7':
        p2.send()
        send[6] = p2.send_clock
    elif p2.input[0] == 's8':
        p2.send()
        send[7] = p2.send_clock
    elif p2.input[0] == 's9':
        p2.send()
        send[8] = p2.send_clock

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
    elif p3.input[0] == 's4':
        p3.send()
        send[3] = p3.send_clock
    elif p3.input[0] == 's5':
        p3.send()
        send[4] = p3.send_clock
    elif p3.input[0] == 's6':
        p3.send()
        send[5] = p3.send_clock
    elif p3.input[0] == 's7':
        p3.send()
        send[6] = p3.send_clock
    elif p3.input[0] == 's8':
        p3.send()
        send[7] = p3.send_clock
    elif p3.input[0] == 's9':
        p3.send()
        send[8] = p3.send_clock
    #p4 send
    if p4.input[0] == 's1':
        p4.send()
        send[0] = p4.send_clock
    elif p4.input[0] == 's2':
        p4.send()
        send[1] = p4.send_clock
    elif p4.input[0] == 's3':
        p4.send()
        send[2] = p4.send_clock
    elif p4.input[0] == 's4':
        p4.send()
        send[3] = p4.send_clock
    elif p4.input[0] == 's5':
        p4.send()
        send[4] = p4.send_clock
    elif p4.input[0] == 's6':
        p4.send()
        send[5] = p4.send_clock
    elif p4.input[0] == 's7':
        p4.send()
        send[6] = p4.send_clock
    elif p4.input[0] == 's8':
        p4.send()
        send[7] = p4.send_clock
    elif p4.input[0] == 's9':
        p4.send()
        send[8] = p4.send_clock

    #p5 send
    if p5.input[0] == 's1':
        p5.send()
        send[0] = p5.send_clock
    elif p5.input[0] == 's2':
        p5.send()
        send[1] = p5.send_clock
    elif p5.input[0] == 's3':
        p5.send()
        send[2] = p5.send_clock
    elif p5.input[0] == 's4':
        p5.send()
        send[3] = p5.send_clock
    elif p5.input[0] == 's5':
        p5.send()
        send[4] = p5.send_clock
    elif p5.input[0] == 's6':
        p5.send()
        send[5] = p5.send_clock
    elif p5.input[0] == 's7':
        p5.send()
        send[6] = p5.send_clock
    elif p5.input[0] == 's8':
        p5.send()
        send[7] = p5.send_clock
    elif p5.input[0] == 's9':
        p5.send()
        send[8] = p5.send_clock
    #recieve section
    #p1 receive
    if p1.input[0] == 'r1' or p1.input[0] == 'r2' or p1.input[0] == 'r3' or p1.input[0] == 'r4' or p1.input[0] == 'r5'  or p1.input[0] == 'r6' or p1.input[0] == 'r7'  or p1.input[0] == 'r8' or p1.input[0] == 'r9':
        if p1.input[0] == 'r1' and send[0]!= 0:
            p1.receive(send[0])
        elif p1.input[0] == 'r2' and send[1]!= 0:
            p1.receive(send[1])
        elif p1.input[0] == 'r3' and send[2]!= 0:
            p1.receive(send[2])
        elif p1.input[0] == 'r4' and send[3]!= 0:
            p1.receive(send[3])
        elif p1.input[0] == 'r5' and send[4]!= 0:
            p1.receive(send[4])
        elif p1.input[0] == 'r6' and send[5]!= 0:
            p1.receive(send[5])
        elif p1.input[0] == 'r7' and send[6]!= 0:
            p1.receive(send[6])
        elif p1.input[0] == 'r8' and send[7]!= 0:
            p1.receive(send[7])
        elif p1.input[0] == 'r9' and send[8]!= 0:
            p1.receive(send[8])

    #p2 receive
    if p2.input[0] == 'r1' or p2.input[0] == 'r2' or p2.input[0] == 'r3' or p2.input[0] == 'r4' or p2.input[0] == 'r5'  or p2.input[0] == 'r6' or p2.input[0] == 'r7'  or p2.input[0] == 'r8' or p2.input[0] == 'r9':
        if p2.input[0] == 'r1' and send[0]!= 0:
            p2.receive(send[0])
        elif p2.input[0] == 'r2' and send[1]!= 0:
            p2.receive(send[1])
        elif p2.input[0] == 'r3' and send[2]!= 0:
            p2.receive(send[2])
        elif p2.input[0] == 'r4' and send[3]!= 0:
            p2.receive(send[3])
        elif p2.input[0] == 'r5' and send[4]!= 0:
            p2.receive(send[4])
        elif p2.input[0] == 'r6' and send[5]!= 0:
            p2.receive(send[5])
        elif p2.input[0] == 'r7' and send[6]!= 0:
            p2.receive(send[6])
        elif p2.input[0] == 'r8' and send[7]!= 0:
            p2.receive(send[7])
        elif p2.input[0] == 'r9' and send[8]!= 0:
            p2.receive(send[8])

    #p3 receive
    if p3.input[0] == 'r1' or p3.input[0] == 'r2' or p3.input[0] == 'r3' or p3.input[0] == 'r4' or p3.input[0] == 'r5'  or p3.input[0] == 'r6' or p3.input[0] == 'r7'  or p3.input[0] == 'r8' or p3.input[0] == 'r9':
        if p3.input[0] == 'r1' and send[0]!= 0:
            p3.receive(send[0])
        elif p3.input[0] == 'r2' and send[1]!= 0:
            p3.receive(send[1])
        elif p3.input[0] == 'r3' and send[2]!= 0:
            p3.receive(send[2])
        elif p3.input[0] == 'r4' and send[3]!= 0:
            p3.receive(send[3])
        elif p3.input[0] == 'r5' and send[4]!= 0:
            p3.receive(send[4])
        elif p3.input[0] == 'r6' and send[5]!= 0:
            p3.receive(send[5])
        elif p3.input[0] == 'r7' and send[6]!= 0:
            p3.receive(send[6])
        elif p3.input[0] == 'r8' and send[7]!= 0:
            p3.receive(send[7])
        elif p3.input[0] == 'r9' and send[8]!= 0:
            p3.receive(send[8])
    #p4 receive
    if p4.input[0] == 'r1' or p4.input[0] == 'r2' or p4.input[0] == 'r3' or p4.input[0] == 'r4' or p4.input[0] == 'r5'  or p4.input[0] == 'r6' or p4.input[0] == 'r7'  or p4.input[0] == 'r8' or p4.input[0] == 'r9':
        if p4.input[0] == 'r1' and send[0]!= 0:
            p4.receive(send[0])
        elif p4.input[0] == 'r2' and send[1]!= 0:
            p4.receive(send[1])
        elif p4.input[0] == 'r3' and send[2]!= 0:
            p4.receive(send[2])
        elif p4.input[0] == 'r4' and send[3]!= 0:
            p4.receive(send[3])
        elif p4.input[0] == 'r5' and send[4]!= 0:
            p4.receive(send[4])
        elif p4.input[0] == 'r6' and send[5]!= 0:
            p4.receive(send[5])
        elif p4.input[0] == 'r7' and send[6]!= 0:
            p4.receive(send[6])
        elif p4.input[0] == 'r8' and send[7]!= 0:
            p4.receive(send[7])
        elif p4.input[0] == 'r9' and send[8]!= 0:
            p4.receive(send[8])
    #p5 receive
    if p5.input[0] == 'r1' or p5.input[0] == 'r2' or p5.input[0] == 'r3' or p5.input[0] == 'r4' or p5.input[0] == 'r5'  or p5.input[0] == 'r6' or p5.input[0] == 'r7'  or p5.input[0] == 'r8' or p5.input[0] == 'r9':
        if p5.input[0] == 'r1' and send[0]!= 0:
            p5.receive(send[0])
        elif p5.input[0] == 'r2' and send[1]!= 0:
            p5.receive(send[1])
        elif p5.input[0] == 'r3' and send[2]!= 0:
            p5.receive(send[2])
        elif p5.input[0] == 'r4' and send[3]!= 0:
            p5.receive(send[3])
        elif p5.input[0] == 'r5' and send[4]!= 0:
            p5.receive(send[4])
        elif p5.input[0] == 'r6' and send[5]!= 0:
            p5.receive(send[5])
        elif p5.input[0] == 'r7' and send[6]!= 0:
            p5.receive(send[6])
        elif p5.input[0] == 'r8' and send[7]!= 0:
            p5.receive(send[7])
        elif p5.input[0] == 'r9' and send[8]!= 0:
            p5.receive(send[8])

    #NULL section
    if p1.input[0] == 'NULL':
        p1.null()
    if p2.input[0] == 'NULL':
        p2.null()
    if p3.input[0] == 'NULL':
        p3.null()
    if p4.input[0] == 'NULL':
        p4.null()
    if p5.input[0] == 'NULL':
        p5.null()


p1.result()
p2.result()
p3.result()
p4.result()
p5.result()
