N = int (input('введение кол числ (мин 2):'))
if N < 2:
    print('ошибка')
else:
    numbers =[]
    print(f'введите {N}целых чисел(каждое с новой строки):')
    for _ in range(N):
        num = int(input())
        numbers.append(num)
    sorted_numbers = sorted(numbers)
    second_elem = sorted_numbers[1]
    penultimate_elem = sorted_numbers[-2]
    difference = second_elem - penultimate_elem
    abs_difference = abs(difference)
    print(f'{sorted_numbers}')
    print(f'{second_elem}')
    print(f'{penultimate_elem}')
    print(f'{second_elem} - {penultimate_elem} = {difference}') 
    print(f"{abs_difference}")