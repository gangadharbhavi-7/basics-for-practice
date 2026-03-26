num=input("Enter the multi digit number(use strictly numbers): ")
g={}
for i in num:
    if i.isdigit():
        g[i]=g.get(i, 0)+1

print("Digit frequencies")
for x in g:
    print(f"Digit {x} occurs {g[x]} time(s)")