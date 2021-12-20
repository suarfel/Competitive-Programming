(m,n,a) = [int(i) for i in input().split()]
if m%a == 0:
    m = m//a
else:
    m = m//a + 1
if n%a == 0:
    n = n//a
else:
    n = n//a +1
print(m*n)