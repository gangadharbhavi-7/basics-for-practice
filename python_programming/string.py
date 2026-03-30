# with open("C:\\Users\\Gangadhar\\OneDrive\\03_Projects\\14_practice_playground\\basics-for-practice\\python_programming\\sample.txt", "r") as infile:
#     lines = infile.readlines()

# cleaned_lines = []
# for line in lines:
#     cleaned_lines.append(line.strip())
# # cleaned_lines.sort()

# with open("output.txt", "a") as outfile:
#     for line in cleaned_lines:
#         outfile.write(line + "\n")
x=[1,2,1,0,4,5]
y=x.copy()
x.sort()
print(x)
print(y)