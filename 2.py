a=[]
b=[]
c=[]
number_a=int(input("введите количество чисел в массиве A: "))
print("Введите элементы массива А: ")
for i in range(number_a):
    a.append(input())

number_b=int(input("введите количество чисел в массиве B: "))
print("Введите элементы массива B: ")
for j in range(number_b):
    b.append(input())

for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c.append(a[i])
print(c)
            