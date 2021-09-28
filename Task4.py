# Task 4:
# Find the series of Fibonacci numbers using lambda function

# lambda arguments: expression



fabLst = [0,1]
n = int(input("Enter the lenght of fabnicio Series"))

for i in range(2,n):
    value = lambda a,b: a+b
    fabLst.append(value(fabLst[i-2],fabLst[i-1]))

print(fabLst)