def countSwaps(a):
    numSwaps=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                numSwaps = numSwaps + 1
    print("Array is sorted in " + str(numSwaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)