n=int(input("enter the number "))
five=two=one=0
if(n<5):
    if(n==1):
        five=two=0
        one=1
    elif(n==2):
        five=one=0
        two=1
    elif(n==3):
        five=0
        one=two=1
    else:
        five=0
        one=2
        two=1
else:
    r=n%5
    q=n//5
    if(r>3):
         five=q   
    else:
        five=q-1
    if(r==4):
         two=1
    elif(r==0 or r==1):
        two=2
    else:
        two=3
    if(r==4 or r==1 or r==3):
         one=2
    else:
        one=1  
        
sum=five+two+one
print(sum,end=' ')
print(five,end=' ')
print(two,end=' ')
print(one)
