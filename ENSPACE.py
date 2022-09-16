# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    x=b*1
    y=c*2
    if (x+y)<=a:
        print("YES")
    else:
        print("NO")