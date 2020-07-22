n=int(input("enter the length of the string"))
s=input("enter  the string")
t=int(input("enter the number of test case"))
for i in range(0,t):
    cout=0
    p=int(input("enter the position"))
    z=s[p-1]
    for j in range(0,p-1):
        if(s[j]==z):
            cout=cout+1
    print(cout)
            

