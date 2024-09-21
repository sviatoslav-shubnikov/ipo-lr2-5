num = input("Введите число, состоящие из 8 разрядов: ")

if len(num) != 8:

    print("Введите корректное число, состоязие из 8 разрядов!")

else: 

    sum_numbers_in_num = sum(int(i) for i in num)
    print(f"Сумма всех цифр числа: {sum_numbers_in_num}")