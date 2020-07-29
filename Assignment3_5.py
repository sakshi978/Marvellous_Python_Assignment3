from MarvellousNum import *

arr = list()

num1 = int(input("Enter number of elements: "))

def main():
    for i in range(0, num1):
        no = int(input("Enter element: "))
        arr.append(no)

    ListPrime()

def ListPrime():
    iRet = ChkPrime(arr)
    print(iRet)

if __name__ == "__main__":
    main()