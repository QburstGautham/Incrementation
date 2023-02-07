board = [
    [0, 0, 0, 8, 0, 0, 4, 0, 3],
    [2, 0, 0, 0, 0, 4, 8, 9, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 2, 9, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 6, 5, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 6, 2, 7, 0, 0, 0, 0, 1],
    [4, 0, 3, 0, 0, 6, 0, 0, 0]
]

def showboard(b):
    hflag=0
    vflag=0
    hline=" ----------------------------"
    print(hline)
    print("|",end="")
    for i in b:
        if hflag==3:
            hflag=0
            print(hline)
        for j in i:
            if vflag==3:
                vflag=0
                print("|",end="")
            print(f' {j} ',end = "")
            vflag+=1
        print("|")
        hflag+=1
    print(hline)

showboard(board)