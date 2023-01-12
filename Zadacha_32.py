print('Введите через пробел элементы списка:')
input_list = input().split()
def get_unique_numbers(n):
    unique = []
    for number in n:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique
print('Уникальные элементы списка:' ) 
print(*get_unique_numbers(input_list),sep=', ')           