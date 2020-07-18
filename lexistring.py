N=int(input("no of test case"))

while(N>0):
    p=input("enter the 26 alphbet")
    s=input("enter your string")

    list1=[]
    for i in s:
        list1.append(p.find(i))
        print(p.find(i))

    list1.sort()
    for i in list1:
        print(p[i],end='')
        N=N-1
