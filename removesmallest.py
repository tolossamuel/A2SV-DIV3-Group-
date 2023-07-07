t = int(input())  # Read the number of test cases

for y in range(t):
    n = int(input())  # Read the length of the array
    a = list(map(int, input().split()))  # Read the elements of the array
    a.sort()  # Sort the array in non-decreasing order
    possible = True

    for i in range(n-1):
        if abs(a[i] - a[i+1]) > 1:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")
