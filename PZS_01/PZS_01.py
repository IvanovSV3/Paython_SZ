# Подсчитать количество натуральных чисел, не превосходящих заданного числа n, которые
# делятся на k, но не на l
# делятся хотябы на k или на l
# не делятся на (k + l)

num = int(input("веедите число n  "))
k = 3
l = 2
def num_1(k,l,num):
    count = 0
    for i in range(0,num + 1):
        #print(i)
        if (i%k == 0) and (i%l!= 0):
            count = count + 1
            #10
            # print(count)
    return count


print('условие 1 = ')
print(num_1(k,l,num))

def num_2(k,l,num):
    count = 0
    for i in range(0,num + 1):
        #print(i)
        if (i%k == 0) or (i%l== 0):
            count = count + 1
            #print(count)
    return count

print('условие 2 = ')
print(num_2(k,l,num))

def num_3(k,l,num):
    count = 0
    for i in range(0,num + 1):
        #print(i)
        if i%(k+l) != 0:
            count = count + 1
            #print(count)
    return count

print('условие 3 = ')
print(num_3(k,l,num))