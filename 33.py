def fact(x):
	f=1
	for i in range(x,1,-1):
		f=f*i
	return f
n=input("Enter n")
r=input("Enter r")
d=n-r
nf=fact(n)
rf=fact(r)
df=fact(d)
ans=nf/(rf*df)
print "Binomial coefficient is",ans
