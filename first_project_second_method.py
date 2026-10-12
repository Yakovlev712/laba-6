a = input("Вводи сюда свою строку ")

result = []

for i in range(len(a)):
    for n in range(i + 2 , len(a) + 1 ):
        part = a[i : n ]

if part == part[::-1]:
    result.append(part)

print(result)
        