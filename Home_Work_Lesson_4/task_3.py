"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите
задание в одну строку.
Подсказка: используйте функцию range() и генератор.
"""
print(
    f'От 20 до 240 найдены числа, кратные 20 или 21:'
    f' {[i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]}')
