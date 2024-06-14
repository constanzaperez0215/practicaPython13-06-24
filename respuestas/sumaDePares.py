numeros= [1, 2, 3, 4, 5, 6, 7, 8]

def sum_pares(numeros):
    total=0
    for num in numeros:
        if num%2 == 0:
            total += num
    print(total)
sum_pares(numeros)