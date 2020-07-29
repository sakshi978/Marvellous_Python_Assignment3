arr = list()

num = int(input("Enter number of elements: "))
print("Enter numbers: ")

for i in range(0, num):
    no = int(input())

    arr.append(no)

iSum = 0
for i in range(0, num):
    iSum = iSum+arr[i]

print("Entered numbers are ",arr)
print("Sum of all elements is ", iSum)