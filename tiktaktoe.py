def out(a):
    #prints the board
    print (' ------------')
    print (f'| {a[0][0]} | {a[0][1]} | {a[0][2]} |')
    print (' ------------')

    print (f'| {a[1][0]} | {a[1][1]} | {a[1][2]} |')
    print (' ------------')

    print (f'| {a[2][0]} | {a[2][1]} | {a[2][2]} |')
    print (' ------------')


def input(a,b,li):
    #give input to board by taking player number and position
    b=b-1
    x=b/3
    y=b%3

    if(a)==1:
        li[x][y]=='X'
    else:
        li[x][y]=='O'
    return li

def endcheck(a,li):
    flag=0
    for i in li:
        if i[0]==i[1] and i[0]==i[2] and i[0]!=" ":
            flag=1
    if (li[1][1]==li[0][0] and li[1][1]==li[2][2] and li[1][1]!=" " ) or (li[1][1]==li[0][2] and li[1][1]==li[2][0] and li[1][1]!=" "):
        flag=1
    if flag==1:
        return f'PLAYER {a} has won'
    return None

print (endcheck(2,base))
 
while(True):
    base=[[" "]*3]*3

    player1=input("Choose The Symbol for Player 19")