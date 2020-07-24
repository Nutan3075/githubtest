n=int(input("enter the number of monkeyz"))
pos=[]
monkey=[]
monkey1=[]
for i in range(0,n):
     pos.append(int(input())    
     monkey1.append(input())
     monkey2.append(i)
    
p=0
for i in pos:
    monkey2[i]=monkey1[p]
    p=p+1
print(monkey2)

def jump(monkey1,monkey2):
    j=0
    for i in pos:
        monkey2[i]=monkey1[j]
        j=j+1
        

cout=0
for i in range(0,7):
    if(monkey==monkey2):
        print(cout+1)
        break
    else:
        m=0
        for i in monkey2:
            monkey1[m]=i
            m=m+1
        monkey2=[1,2,3,4,5,6]
        jump(monkey1,monkey2)
    cout=cout+1
    
