t=int(input("enter the number of test case"))
for i in range(0,t):
    n=int(input("enter the number of boxes"))
    list1=[]
    list2=[]
    print("ente number of candies in each boxes")
    for i in range(0,n):
        list1.append(int(input()))
    
    list1.sort()
    cout=list1[0]
    for i in range(1,n):
        cout=cout+list1[i]
        list2.append(cout)
    
    print(sum(list2))



   
