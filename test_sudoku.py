text=[]
i=0
while len(text)!=9:
    text.append(input())
    if text[i].isnumeric() and len(text[i])==9:
        i+=1
        continue
    else:
        print("Invalid input")
        del text[i]
total=1+2+3+4+5+6+7+8+9
print(text)

for i in range(9):
    rowtotal=0
    for j in range(9):
        rowtotal+=int(text[i][j])
    if rowtotal!=total:
        print("NO,rowtotal is wrong")
        exit(0)
for j in range(9):
    coltotal=0
    for i in range(9):
        coltotal+=int(text[i][j])
    if coltotal!=total:
        print("No,coltotal is wrong")
        exit(0)
l_p=[0,3,6]

l_q=[0,3,6]
for p in l_p:
    for q in l_q:
        ele=0
        i=p
        endi=i+3
        for i in range(i,endi):
            j=q
            endj=j+3
            for j in range(j,endj):
                # print("p=",p," q=",q," i=",i," j=",j)
                ele+=int(text[i][j])
        if ele!=total:
            print("NO,3*3 is wrong")
            exit(0)

print("YES")
        
    

