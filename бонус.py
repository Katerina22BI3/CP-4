a=[]
k=0
delta=int(input("введите значение delta: "))
number=int(input("введите количество чисел в массиве: "))
print("введите элементы массива: ")
for i in range(number):
    a.append(int(input()))
for i in range(len(a)-1):
    m=i
    for j in range(i+1, len(a)):
        if a[m]>a[j]:
            m=j
    a[m],a[i]=a[i],a[m]

for i in range(len(a)):
    if a[i]-delta==a[0]:
        k+=1
print(k)
    
