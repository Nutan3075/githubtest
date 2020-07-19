n=int(input("enter the end number"))
list1=[1]
list2=[]
list3=[]
list4=[]
sum=0
cout=0
for i in range(1,n):
    list2.append(i)
    for j in range(2,i):
        if(i%j==0):
            list1.append(i)
            break
        
for i in list2:
    if i not in list1:
        list3.append(i)
print("prime no in range")
print(list3)
for i in range(2,len(list3)+1):
    sum=0
    for j in range(0,i):
        sum=sum+list3[j]
    list4.append(sum)
print("this is the sum of all consecutive prime number")
print(list4)
for i in list3:
    if i in list4:
        print(i)
        cout=cout+1
print("our output")
print(cout)
        
  
    

    
    
        
