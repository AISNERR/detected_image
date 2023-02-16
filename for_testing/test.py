a = [1, 4, 2, 10, 9]
maxW = 0
i = 0
j = 0
while i < (len(a) - 1):
    while j < (len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j+1] = a[j+1], a[j]
        j += 1
    i += 1
print(a)
