import os

def printb(t3):
    os.system('cls')
    for i in range(3):
        for j in range(3):
            print(t3[i][j],end=" ")
        print()
    
def check(e,m):
    try:
        if(m[e-1][0]==e):
            return True
        else:
            return False
    except:
        return False

def iswin(p,t):
    hc=True
    if(t[0][0]==p and t[1][1]==p and t[2][2]==p):
        return True
    elif(t[0][2]==p and t[1][1]==p and t[2][0]==p):
        return True
  
    for i in range(3):
        hc=True
        for j in range(3):
            if(t[i][j]!=p):
                hc=False
        if(hc):
            return hc
    vc=True
    for i in range(3):
        vc=True
        for j in range(3):
            if(t[j][i]!=p):
                vc=False
        if(vc):
            return True            
    return False
                        

def play():
    t3=[]
    for i in range(3):
        tl=[]
        for j in range(3):
            tl.append('#')
        t3.append(tl)
    m=[]
    r,c=0,0
 
    for i in range(9):
        tl=[]
        tl.append(i+1)
        tl.append(r)
        tl.append(c)
        c=c+1
        if(c==3):
            c=0
            r=r+1
        m.append(tl)
    pl1,pl2=False,False
    res=False
    p2=False
    p1=True
    mv=0
    ob=False

    while(res!=True):
        printb(t3)
        if(p1):
            print('Player 1 move')
            try:
                n=int(input())
                vm=check(n,m)
            except:
                vm=False
            while(vm!=True):
                print('\nPlease Enter a valid move')
                try:
                    n=int(input())
                    vm=check(n,m)
                except:
                    vm=False
            r,c=m[n-1][1],m[n-1][2]
            t3[r][c]='X'
            m[n-1]=None
            if(mv>=5):
                res=iswin('X',t3)
                if(res):
                    pl1=True
                    break
            p1=False
        else:
            print('Player 2 move')
            try:
                n=int(input())
                vm=check(n,m)
            except:
                vm=False
            while(vm!=True):
                print('\nPlease Enter a valid move')
                try:
                    n=int(input())
                    vm=check(n,m)
                except:
                    vm=False
            r,c=m[n-1][1],m[n-1][2]
            t3[r][c]='0'
            m[n-1]=None
            if(mv>=5):
                res=iswin('0',t3)
                if(res):
                    pl2=True
                    break
            p1=True
        mv=mv+1
        if(mv<9):
            pass
        else:
            ob=True
            break
    printb(t3)
    if(pl1):
        print('Player 1 Wins')
    elif(pl2):
        print('Player 2 Wins')
    else:
        print('Game Draws')

    input('\n Press any key to continue')
    os.system('cls')
    res=False
    play()


play()

