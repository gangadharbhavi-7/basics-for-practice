l=[]
n=int(input("Enter the number of elements in a list: "))
for i in range(n):
    x=int(input(""))
    l.append(x)
print(l)
mean=sum(l)/len(l)
variance=sum((x-mean)**2 for x in l)/len(l)
sd=variance**0.5
print("Mean: "+str(mean))
print("variance: "+str(variance))
print("standard deviation "+str(sd))