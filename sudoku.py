import random

base=[[["0"]*3 for _ in range(3)] for _ in range(9)]
# base[8][2][0]=7
# print (base)

for i in range(len(base)):
    for j in range(len(base[i])):
        print(base[i][j],i,j)


st=" 1 2 3 \n 4 5 6 \n 7 8 9"
print(st)
def out(a):
    st=""
    for i in a:
        st+="new row \n"
        for j in i:
            st+="X"
            for k in j:
                st+=" 1 "
                
        st+="X \n"
    return st
# base[0][0]=random.sample(range(1, 10), 9)

# print(base)

print (out(base))
# print(random.sample(range(1, 10), 9))