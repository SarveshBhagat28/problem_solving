n,m,a,b=map(int,input().split())
x=n*a
y=(n//m)*b+(n%m)*a
z=((n+m-1)//m)*b
print (min(x,y,z))