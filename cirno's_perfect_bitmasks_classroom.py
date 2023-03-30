
n = int(input())
for i in range(n):
    k = int(input()) 
    for j in range(64):
        if k & 1 << j:
            if k ^ 2**j:
                print(2**j)
            else:
                for z in range(64):
                    if not (k & 1 << z ):
                        print(2**j + 2**z)
                        break
            break
        else:
            continue
