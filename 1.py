a=[]
number=int(input("введите количество чисел в массиве: "))
print("введите элементы массива: ")
for i in range(number):
    a.append(float(input()))
maxa=a[0]
for i in range(len(a)-1):
    m=i
    for j in range(i+1, len(a)):
        if a[j]>a[m] or a[m]==a[j]:
            maxa=max(maxa,a[j])
            m=j
        else:
            maxa=max(maxa,a[i])
    for h in range(m, len(a)):
        if a[h]<maxa:
            a[h]=0
print(a)

