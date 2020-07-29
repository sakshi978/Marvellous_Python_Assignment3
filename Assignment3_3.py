arr = list()

num = int(input("Enter number of elements: "))
print("Enter numbers: ")

for i in range(0, num):
    no = int(input())

    arr.append(no)

iMin = arr[0]
for i in range(0, num):
    if (iMin > arr[i]):
        iMin = arr[i]

print("Entered numbers are ",arr)
print("Maximum of all elements is ", iMin)