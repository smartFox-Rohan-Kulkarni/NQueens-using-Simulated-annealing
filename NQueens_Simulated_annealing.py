#hey there I am Rohan Kulkarni and I love probem solvings.
#you can pin me on my Email if you have any doubts.


import math
import random
import itertools


n=None
glbcnt=0
def disboard(state):
    for i in range(n-1):
    #print("|",state[0],"|",state[1],"|",state[2],"|",state[3],"|")
        print(" |", state[i],end="")
    print(" |")

def compute_heuristic(board):
    #number of queens under attack
    global n
    heuristic_value=0
    for col_i in range(0,n-1):
        for col_j in range(col_i+1,n-1):
            #same row
            #print(col_i,col_j,board[col_j])
            if board[col_i]==board[col_j]:
                heuristic_value+=1
            #diagonal
            diag=col_j-col_i
            if (board[col_i]==board[col_j]+diag) | (board[col_i]==board[col_j]-diag) :
                heuristic_value+=1
    return heuristic_value



def random_sol(board,temp):
    global n
    random_box=[]
    tCurrent_heuristic=compute_heuristic(board)
    possible_candidate=None
    phantonbox=None
    phanton=100000
    if temp<=1:
        return None
    for x in range(n - 1):
        temp = board.copy()
        for y in range(n - 1):
            if board[x] == 1 + y:
                continue
            # print(y+1)
            temp[x] = 1 + y
            print("explored\t\t\t->",temp)
            if compute_heuristic(temp) <= tCurrent_heuristic:
                possible_candidate = temp.copy()
                tCurrent_heuristic = compute_heuristic(temp)
            if compute_heuristic(temp)<phanton:
                phanton=compute_heuristic(temp)
                phantonbox=temp.copy()


            #random_box.extend([temp])
    #lenth=len(random_box)
    #rn= random.randint(0, lenth-1)
    #rn= random.sample(range(0, lenth-1), 1)
    #print(random_box[rn])
    #return random_box[rn]
    #print(possible_candidate,phantonbox)
    if possible_candidate==None:
        possible_candidate=phantonbox.copy()

    print("exploring next->",possible_candidate)
    return possible_candidate

def stimulateA(board,bored,tempMax):
    global n,glbcnt
    #First we need set the initial temperature and create a random initial solution.
    initial_temp=tempMax
    solCurrent=board
    solBest=solCurrent
    tempCur = tempMax
    zoomb=None
    #Then we begin looping until our stop condition is met.
    # Usually either the system has sufficiently cooled, or a good-enough solution has been found.
    for i in range(1,bored):
        # From here we select a neighbour by making a small change to our current solution.

        tempSol=random_sol(solCurrent,tempCur)
        if tempSol==None:
            break
        # We then decide whether to move to that neighbour solution.
        zoom =compute_heuristic(tempSol)
        if zoom<=compute_heuristic(solCurrent):
            solCurrent=tempSol
            if zoom<=compute_heuristic(solBest):
                solBest=tempSol
                zoomb=zoom


        elif math.exp(compute_heuristic(solCurrent)-compute_heuristic(tempSol))> (random.randint(0,4)*0.3):
            print("elif2",math.exp(compute_heuristic(solCurrent)-compute_heuristic(tempSol)))
            solCurrent=tempSol
        # Finally, we decrease the temperature and continue looping
        tempCur=calTemp(i, tempMax)  # (temp and change in tem t * temp_change)

    if ((zoomb!=0) and (zoomb!=None)):
        print("in",zoomb,solBest)
        return stimulateA(solBest,bored,tempMax-(zoomb*100))
    else:
        return solBest

def calTemp(intrest,temp):
    return (intrest/3)*temp

def random_inputs():
    global n
    sudo=[]
    t = list(itertools.product(list(range(1,n)), repeat=n-1))
    for i in range(256):
         sudo.append(list(t[i]))
    return sudo
def makememain():

    global n,local_bfs_mode,plateu_mode
    input_state=[]

    n = int(input("Enter size of queen problem"))+1
    disboard(list(range(1,n)))
    print("Enter start position")
    for i in range(1, n):
        print("Enter row no for queen", i, ":")
        #only row no as column is fixed for each queen Q1 goes in col 1, Q2 in col 2 so on..
        item = int(input())
        if (item<1) | (item>n):
            print("invalid choice try again..")
            return
        input_state.append(item)
    disboard(input_state)
    #disboard(apply_simple_HillClimbing(input_state))
    #apply_simple_HillClimbing(input_state)
    x=stimulateA(input_state,n-1,105000)
    disboard(x)
    print(compute_heuristic(x))

def tester():
    global n
    n = int(input("Enter size of queen problem")) + 1
    sudo=random_inputs()
    data={}
    data1={}
    cnt=0
    err=None
    err1=None
    for i in range(len(sudo)):
        temp=stimulateA(sudo[i], n - 1, 10500000000000500)
        disboard(temp)
        data[i]=sudo[i]
        data1[i]=temp
        cnt += 1
        if int(compute_heuristic(temp))!=0:
            err=temp.copy()
            err1=sudo[i]
            break
    print(cnt,len(sudo))
    if err!=None:
        print("ERROR:",err1,"val:",err)
    for i in range(cnt):
        print(1+i,"->",data[i],":",data1[i])

#makememain()
tester()
