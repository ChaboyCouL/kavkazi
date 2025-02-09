def vvod():

    n = int(input('Введи размерность массива = > '))
    A = []

    if n > 0:

        for c in range(n):

            print('Введите элемент масива по номером', c+1)
            number = int(input('Число => '))
            A.append(number)

    else:
        print('Ошибка, размер должен быть больше 0')

    return A

def proccess(A):

    B = []

    for i in A:
        if i % 3 == 0: 
            B.append(i)

    razmer_B = len(B)

    return B, razmer_B

def vivod(A, B, razmer_B):
    print('Изначальный массив ', A)
    print('Новый массив ',B)
    print('Размер нового масива = ', razmer_B)

A = vvod()
B, razmer_B = proccess(A)
vivod(A, B, razmer_B)
