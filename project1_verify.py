import sys
# Reads file and cleans input to make other parts simpler
# Modified from project1_calculate verify algo
def fileReader(filename):
    testinput = list()
    with open(filename) as f:
        testinput = f.read().splitlines() # split the line
    for i in range(0, len(testinput)):
        testinput[i] = list(map(int, testinput[i].split())) # split the string

    return testinput

def main():
    userInput = input("Enter file path for test case:  ")
    inp = fileReader(userInput)
    n = len(inp)
    m = len(inp[0])
    # initiate output to all internal events
    out = [['i']*m for _ in range(n)] 
    # two dict will store LC-value as key, and location in input (row, col) as values
    rloc = {}
    sloc = {}
    send = []
    receive = []
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            s_value = 0	
            # event is null
            if inp[i][j] == 0:
                out[i][j] = "NULL"
            # receive event
            # first event is not 1
            elif j == 0 and inp[i][j] != 1: 
                receive.append(inp[i][j])
                s_value = inp[i][j] - 1
                send.append(s_value)
                rloc[inp[i][j]] = [i, j]
                # first event is not 1 and the even following it is also a receive event
                if j+1 < len(inp[i]) and inp[i][j+1] > inp[i][j] + 1:
                    receive.append(inp[i][j+1])
                    s_value = inp[i][j+1] - 1
                    send.append(s_value)
                    rloc[inp[i][j+1]] = [i, j+1]
            # avoid checking outside array size
            elif j+1 < len(inp[i]) and inp[i][j+1] > inp[i][j] + 1:
                receive.append(inp[i][j+1])
                s_value = inp[i][j+1] - 1
                send.append(s_value)
                rloc[inp[i][j+1]] = [i, j+1]
            # an internal event. 
            else:
                continue

            # find the send if it exists
            find = False
            for x in range(len(inp)):
                if find == True: # end search when found
                    break
                for y in range(len(inp[x])):
                    if inp[x][y] == s_value:
                        sloc[inp[x][y]] = [x, y]
                        find = True
                        break
            if find == False:	# send value d.n.e
                fi = open("out.txt", "a")
                print("Result of Verify Algo: OUTPUT IS INCORRECT\n", file=fi)
                fi.close()
                sys.exit('OUTPUT IS INCORRECT')
    # sort the values (increasing) and update output with send/receive events
    send.sort()
    receive.sort()
    s_count = 1
    r_count = 1
    for s in send:
        s_out = sloc.get(s)
        s_row = s_out[0]
        s_col = s_out[1]
        out[s_row][s_col] = "s" + str(s_count)
        s_count += 1
    for r in receive:
        r_out = rloc.get(r)
        r_row = r_out[0]
        r_col = r_out[1]
        out[r_row][r_col] = "r" + str(r_count)
        r_count += 1
    
    # print the result
    fi = open("out.txt", "a")
    print("Result of Verify Algo: \n", file=fi)
    for i in range(0, len(out)):
        print(out[i], file=fi)
    print("\n", file=fi)
    fi.close()
    
if __name__ == "__main__":
    main()