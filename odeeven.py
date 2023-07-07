n = int(input())  # Read the number of elements

a = list(map(int, input().split()))  # Read the elements of the array

odd = []  # List to store odd elements
even = []  # List to store even elements

for x in a:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

odd.sort()  
even.sort()  
result = odd + even  

print(*result)  
