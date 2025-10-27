import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000 and min <= quantity <= max):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers

# Приклад використання
# Випадкові числа для лотерейного квитка від 1 до 49 (6 чисел)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

# Створення екзаменаційних квитків: 5 чисел від 1 до 100
exam_paper = get_numbers_ticket(1, 100, 5)
print("Екзаменаійні питання:", exam_paper)

# Приклад з невалідними даними
invalid_lottery = get_numbers_ticket(1, 10, 15)
print("Невалідний запит (повинен повернути порожній список):", invalid_lottery)