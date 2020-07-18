n=int(input("number of test case"))
while(n>0):
    m=int(input("enter the money that you want to convert to the minimun"))
    for i in range(0,m):
        if(m<=2**i):
            print(i)
            print("the number which can represent are:")
            for j in range(0,i):
                 print(2**j)
               
           
            break
    n=n-1
