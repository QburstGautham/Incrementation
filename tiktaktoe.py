def out(a):
    #prints the board
    print (' ------------')
    print (f'| {a[0][0]} | {a[0][1]} | {a[0][2]} |')
    print (' ------------')

    print (f'| {a[1][0]} | {a[1][1]} | {a[1][2]} |')
    print (' ------------')

    print (f'| {a[2][0]} | {a[2][1]} | {a[2][2]} |')
    print (' -----------')


def inp(a,li):
    #give input to board by taking player number and position
    while (True):
        b=int(input(f'Give the position [1-9] for player {a} : '))
        b=b-1
        x=int(b/3)
        y=int(b%3)
        if li[x][y]!=" ":
            print ("Position Already Filled. TRY AGAIN!")
        else :
            break

    if(a)==1:
        li[x][y]='X'
    else:
        li[x][y]='O'

    return li

def endcheck(a,li):
    flag=0
    full=1
    for i in range(3):
        if (li[i][i]!=" ") and ((li[i][0]==li[i][1] and li[i][0]==li[i][2]) or (li[0][i]==li[1][i] and li[0][i]==li[2][i])):
            flag=1
    if (li[1][1]==li[0][0] and li[1][1]==li[2][2] and li[1][1]!=" " ) or (li[1][1]==li[0][2] and li[1][1]==li[2][0] and li[1][1]!=" "):
        flag=1
    if flag==1:
        return f'PLAYER {a} has won'
    for i in li:
        for j in i:
            if j==" ":
                full=0
    if full==1:
        return f'NO MORE TRIES ARE POSSIBLE!'
    
            
    return 0

 
while(True):
    base=[[" "]*3 for _ in range(3)]  
    print("Player 1 has X and Player 2 is O")
    player=1


    while (True):
        base=inp(player,base)
        out(base)
        end=endcheck(player,base)
        if end!=0:
            print(end)
            print("Game ENDED!")
            break
        #after each try change player number
        
        if player==1:
            player=2
        else:
            player=1
    again=(input("Enter Y to play again : ")).lower()
    if again!="y":
        break
print("THANK YOU!")
        

        
        
        
    
    