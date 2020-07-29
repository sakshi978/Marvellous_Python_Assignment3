arr = list()

num = int(input("Enter number of elements: "))
print("Enter numbers: ")

for i in range(0, num):
    no = int(input())

    arr.append(no)

no1 = int(input("Enter number whose frequency you want to know: "))

iCnt = 0

for i in range(num):
    if (arr[i] == no1):
        iCnt = iCnt+1

print("Entered numbers are ",arr)
print("Frequency: ", iCnt)
