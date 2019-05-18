ch='1'
while(ch=='1'):
    lst=list(map(int,input().split()))
    temp,c=[],[]
    while(len(lst)>0):
        count = 0
        temp = [i-min(lst) for i in lst if i-min(lst)>0]
        c.append(len(lst))
        lst=temp
    print (c)
    ch=input("enter 1 to continue :")
