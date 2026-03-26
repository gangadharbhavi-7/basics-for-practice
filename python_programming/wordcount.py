with open("C:\\Users\\Gangadhar\\OneDrive\\03_Projects\\14_practice_playground\\basics-for-practice\\python_programming\\sample.txt ", "r") as f:
    text=f.read()
g={}
words=text.split()
for i in words:
    g[i]=g.get(i,0)+1
print(g)