import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= 1000 and 
            1 <= max <= 1000 and 
            min < max and
            quantity > 0 and 
            quantity <= (max - min + 1)):
        return []
    range_of_numbers = list(range(min, max + 1))
    selected_numbers = random.sample(range_of_numbers, quantity)
    selected_numbers.sort()
        
    return selected_numbers

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

# Приклад з числами, які не починаються з 1
mid_five_random_number = get_numbers_ticket(10, 20, 5)
print("П'ять випадкових чисел від 10 до 20:", mid_five_random_number)